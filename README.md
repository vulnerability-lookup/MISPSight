# Vulnerability-Lookup Sighting

A client that retrieves vulnerability observations from a [MISP](https://github.com/MISP/MISP) server and pushes them to a
[Vulnerability Lookup](https://github.com/cve-search/vulnerability-lookup) instance.

Similar to [FediVuln](https://github.com/CIRCL/FediVuln) which is using the Fediverse as a source of observations.


## Installation


[pipx](https://github.com/pypa/pipx) is an easy way to install and run Python applications in isolated environments.
It's easy to [install](https://github.com/pypa/pipx?tab=readme-ov-file#on-linux).


```bash
$ pipx install VulnerabilityLookupSighting
$ export VulnerabilityLookupSighting_CONFIG=~/conf.py
```

The configuration should be defined in a Python file (e.g., ``~/.conf.py``).
You must then set an environment variable (``VulnerabilityLookupSighting``) with the full path to this file.


## Usage

```bash
$ VulnerabilityLookupSighting --help
usage: FediVuln-Stream [-h] [--since SINCE]

Allows access to the streaming API.

options:
  -h, --help     show this help message and exit
  --since SINCE  Maximum timestamp of the MISP attribute.
```

### Publishing sightings to Vulnerability Lookup

```bash
$ VulnerabilityLookupSighting
Querying MISP...
Query completed successfully.
Pushing sightings to Vulnerability Lookup...
```

[https://github.com/MISP/VulnerabilityLookupSighting](https://github.com/MISP/VulnerabilityLookupSighting)


## License

[Vulnerability-Lookup Sighting](https://github.com/MISP/VulnerabilityLookupSighting) is licensed under
[GNU General Public License version 3](https://www.gnu.org/licenses/gpl-3.0.html)

~~~
Copyright (c) 2024 Computer Incident Response Center Luxembourg (CIRCL)
Copyright (C) 2024 Cédric Bonhomme - https://github.com/cedricbonhomme
~~~
