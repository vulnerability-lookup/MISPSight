# Changelog

## Release 1.1.0 (2025-10-24)

Add two new optional configuration values to support multi-instance deployments:

- `source_prefix` (default: "MISP")
- `source_attribute` (default: "event_uuid")

The sighting `source` is now built dynamically as:

    f"{source_prefix}/{attribute.<source_attribute>}"

If the configured attribute is missing, the code falls back to `event_uuid`.

This preserves existing behaviour by default while allowing per-instance configuration (e.g. "MISP-Paris/event_id", "MISP-Lyon/orgc_id"), making it easier to distinguish sightings originating from different MISP servers.

by @DocArmoryTech <https://github.com/DocArmoryTech>


## Release 1.0.2 (2025-02-19)

Improved monitoring.


## Release 1.0.1 (2025-02-13)

Added logging for process start and end.


## Release 1.0.0 (2025-02-13)

This release introduces the capability to report errors, warnings,
and heartbeats to a Valkey datastore, facilitating centralized monitoring.


## Release 0.4.1 (2024-12-09)

Updated PyVulnerabilityLookup.


## Release 0.4.0 (2024-11-19)

- The client PyVulnerabilityLookup is now used in order to communicate with the API of the Vulnerability-Lookup instance.
- When a duplicate sighting is detected a message is printed.
- Improved management of UTC aware Datetime objects.


##  Release 0.3.0 (2024-11-13)

First working prototype - production ready.
