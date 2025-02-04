# MISPSight

A client that retrieves vulnerability observations from a [MISP](https://github.com/MISP/MISP) server and pushes them to a
[Vulnerability-Lookup](https://github.com/vulnerability-lookup/vulnerability-lookup) instance.


## Installation


[pipx](https://github.com/pypa/pipx) is an easy way to install and run Python applications in isolated environments.
It's easy to [install](https://github.com/pypa/pipx?tab=readme-ov-file#on-linux).


```bash
$ pipx install MISPSight
$ export MISPSight_CONFIG=~/conf.py
```

The configuration should be defined in a Python file (e.g., ``~/.MISPSight/conf.py``).
You must then set an environment variable (``MISPSight_CONFIG``) with the full path to this file.


## Usage

```bash
$ MISPSight --help
usage: FediVuln-Stream [-h] [--since SINCE]

Allows access to the streaming API.

options:
  -h, --help     show this help message and exit
  --since SINCE  Maximum timestamp of the MISP attribute.
```

### Publishing sightings to Vulnerability-Lookup

```bash
$ MISPSight
Querying MISP…
Query completed successfully.
Pushing sightings to Vulnerability-Lookup…
```


## License

[MISPSight](https://github.com/vulnerability-lookup/MISPSight) is licensed under
[GNU General Public License version 3](https://www.gnu.org/licenses/gpl-3.0.html)

~~~
Copyright (c) 2024-2025 Computer Incident Response Center Luxembourg (CIRCL)
Copyright (C) 2024-2025 Cédric Bonhomme - https://github.com/cedricbonhomme
~~~
