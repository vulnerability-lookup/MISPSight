import argparse
import re

from pymisp import MISPAttribute, PyMISP
from pyvulnerabilitylookup import PyVulnerabilityLookup

from mispsight import config
from mispsight.monitoring import heartbeat, log


def remove_case_insensitive_duplicates(input_list: list[str]) -> list[str]:
    """Remove duplicates in a list, ignoring case.
    This approach preserves the last occurrence of each unique item based on
    lowercase equivalence. The dictionary keys are all lowercase to ensure
    case-insensitive comparison, while the original case is preserved in the output.
    """
    return list({item.lower(): item for item in input_list}.values())


def push_sighting_to_vulnerability_lookup(attribute, vulnerability_ids):
    """Create a sighting from a MISP attribute and push it to the Vulnerability-Lookup instance."""
    print("Pushing sightings to Vulnerability-Lookup…")
    vuln_lookup = PyVulnerabilityLookup(
        config.vulnerability_lookup_base_url, token=config.vulnerability_auth_token
    )
    for vuln in vulnerability_ids:
        # Set the creation timestamp for the sighting
        creation_timestamp = ""
        if hasattr(attribute, "first_seen") and attribute.first_seen:
            creation_timestamp = attribute.first_seen
        else:
            creation_timestamp = attribute.timestamp
        if not creation_timestamp:
            log("warning", "push_sighting_to_vulnerability_lookup: no creation_stamp")
            continue

        # Determine source string dynamically
        attr_name = getattr(config, "source_attribute", "event_uuid")
        attr_value = getattr(attribute, attr_name, None)

        if not attr_value:
            # Fallback if attribute doesn’t exist
            attr_value = getattr(attribute, "event_uuid", "unknown")

        source_prefix = getattr(config, "source_prefix", "MISP")

        # Create the sighting
        sighting = {
            "type": "seen",
            "source": f"{source_prefix}/{attr_value}",
            "vulnerability": vuln,
            "creation_timestamp": creation_timestamp,
        }

        # Post the JSON to Vulnerability-Lookup
        try:
            r = vuln_lookup.create_sighting(sighting=sighting)
            if "message" in r:
                print(r["message"])
                if "duplicate" in r["message"].lower():
                    level = "info"
                else:
                    level = "warning"
                log(level, f"push_sighting_to_vulnerability_lookup: {r['message']}")
        except Exception as e:
            print(
                f"Error when sending POST request to the Vulnerability-Lookup server:\n{e}"
            )
            log(
                "error",
                f"Error when sending POST request to the Vulnerability-Lookup server: {e}",
            )


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="MISPSight",
        description="A client that retrieves vulnerability observations from a MISP server and pushes them to a Vulnerability-Lookup instance.",
    )
    parser.add_argument(
        "--since",
        default="1d",
        help="Maximum timestamp of the MISP attribute.",
    )

    arguments = parser.parse_args()

    # Log the launch of the script
    log("info", "Starting MISPSight…")

    # Sends a heartbeat when the script launches
    heartbeat()

    misp = PyMISP(config.misp_url, config.misp_key, config.misp_verifycert)
    print("Querying MISP…")
    attributes = misp.search(
        controller="attributes",
        type_attribute="vulnerability",
        timestamp=arguments.since,
        include_event_uuid=True,
        pythonify=True,
    )
    vulnerability_pattern = re.compile(
        r"\b(CVE-\d{4}-\d{4,})\b"  # CVE pattern
        r"|\b(GHSA-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4})\b"  # GHSA pattern
        r"|\b(PYSEC-\d{4}-\d{2,5})\b"  # PYSEC pattern
        r"|\b(GSD-\d{4}-\d{4,5})\b"  # GSD pattern
        r"|\b(wid-sec-w-\d{4}-\d{4})\b"  # CERT-Bund pattern
        r"|\b(cisco-sa-\d{8}-[a-zA-Z0-9]+)\b"  # CISCO pattern
        r"|\b(RHSA-\d{4}:\d{4})\b"  # RedHat pattern
        r"|\b(msrc_CVE-\d{4}-\d{4,})\b",  # MSRC CVE pattern
        re.IGNORECASE,
    )
    print("Query completed successfully.")
    for attribute in attributes:
        if not isinstance(attribute, MISPAttribute):
            continue
        matches = vulnerability_pattern.findall(attribute.value)
        vulnerability_ids = [
            match for match_tuple in matches for match in match_tuple if match
        ]
        vulnerability_ids = remove_case_insensitive_duplicates(vulnerability_ids)
        if vulnerability_ids:
            push_sighting_to_vulnerability_lookup(attribute, vulnerability_ids)

    # Log the end of the script
    log("info", "MISPSight execution completed.")


if __name__ == "__main__":
    # Point of entry in execution mode.
    main()
