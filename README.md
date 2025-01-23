# 🔍🔫 Sniper

## ABOUT

Sniper (sniper.py) is a simple python script that will fetch list of certificates files types (crt, pem etc), If found, will read its contents and check for its expiry date.

## USAGE

```bash
❯ python3 snipe.py --help
usage: sniper snipe file pattern [-h] --token  --owner  [--repo  | --all ]

options:
  -h, --help  show this help message and exit
  --token     authentication token
  --owner     girhub project owner
  --repo      github repo name
  --all       all repos for the given owner
```

## ENVIRONMENT SETUP

```bash
pip3 install uv
uv venv
source .venv/bin/activate
uv sync
uv run sniper
```

## EXAMPLE

```bash
❯ uv run sniper --owner psadi --repo sniper --token **********************
Sniping contents in 'psadi/sniper' repository
================================================================================

Files:

	1: .gitignore
	2: .python-version
	3: LICENSE
	4: README.md
	5: certs/exampledomain.crt
	6: certs/exampledomain.csr
	7: certs/exampledomain.key
	8: pyproject.toml
	9: snipe.py
	10: uv.lock
================================================================================

Filtered Files:

	1: certs/exampledomain.crt
================================================================================
Certificate             : certs/exampledomain.crt
Certificate Content     :
-----BEGIN CERTIFICATE-----
MIIDiTCCAnGgAwIBAgIUEcGz6tIXM2PMRY9QPKyXTlyYiPIwDQYJKoZIhvcNAQEL
BQAwbTELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExFjAUBgNVBAcM
DVNhbiBGcmFuY2lzY28xFTATBgNVBAoMDEV4YW1wbGUgQ29ycDEaMBgGA1UEAwwR
ZXhhbXBsZWRvbWFpbi5jb20wHhcNMjUwMTE1MDU0ODE0WhcNMjYwMTE1MDU0ODE0
WjBtMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwN
U2FuIEZyYW5jaXNjbzEVMBMGA1UECgwMRXhhbXBsZSBDb3JwMRowGAYDVQQDDBFl
eGFtcGxlZG9tYWluLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
ANP95CKhI3d5KcqUvBK8LEdowIg+I3FGLwkl3rHYaJYqWHYm0ZxPrikMgc4LcfK4
W/LD5hfOc5iH5h2iaIpP6qMoKmQIlSNR2Azc+C2h3uv7KVPrTs2ep0QOEMwroyVE
E06BboFY+FgoR+v05AS+WhKo2qeV9XdDC26/ItOeAyXxUZOpeQ6r119FCQYXRxTS
YZJa7i+4l2NiHRJ4dmvBjEa81MSVdjY6Qa3UTa867jVtLmOTuCNQoIjDHUjkJdUt
pg6N9Un877Fh00pRWb8pq3V6iLwGxtW/BGG3wpwIDErwtVaP1O6PG0Kpm3+IHVlu
OBoKxoM5sB0DJhLIHc0d7dkCAwEAAaMhMB8wHQYDVR0OBBYEFKHhe5ZlKbAyZ6XZ
r811dnx2wHcKMA0GCSqGSIb3DQEBCwUAA4IBAQC8vzGCa52U7Q2dj/nCXlJ7HSTH
nGsNuBQv3ZSzt5JVwHvo+SoK9H1KmVeqAC3NkLva5LrH024nQzqfhHKFUBZflLmQ
E/8EiQRl/DwyG2Ii/vNxBbaty2MSbXg6c4/34z1GB4rsk5ii5Y7LdjPIVokW+J4y
CLGu7kU3AIhESPEGnpGk0hP9qAAnnGB0kOuqi8YGYfGwPnWUletHMZc5iokLBXN5
mvB67t4mJLjOvbzqFpD06sRfsXU8Aj8SWK3kfVNyBzYTJAnIp9IZ7ZXv1VVc8lP2
dkib3CNQrVk47/YgPKoUa3Wyf7p0X3PlcfAZyVRri6PM0Zk89kOT/luw9O33
-----END CERTIFICATE-----

Certificate Expiry Date : 2026-01-15 05:48:14
================================================================================
```

**With Docker**

```bash
❯ docker run sniper:1 --owner psadi --repo sniper --token ****************************
Sniping contents in 'psadi/sniper' repository
================================================================================

Files:

	1: .gitignore
	2: .python-version
	3: Dockerfile
	4: LICENSE
	5: README.md
	6: certs/exampledomain.crt
	7: certs/exampledomain.csr
	8: certs/exampledomain.key
	9: pyproject.toml
	10: requirements.txt
	11: src/sniper/__init__.py
	12: src/sniper/api.py
	13: src/sniper/argparse.py
	14: src/sniper/httpx.py
	15: src/sniper/utils.py
	16: uv.lock
================================================================================

Filtered Files:

	1: certs/exampledomain.crt
================================================================================
Certificate             : certs/exampledomain.crt
Certificate Content     :
-----BEGIN CERTIFICATE-----
MIIDiTCCAnGgAwIBAgIUEcGz6tIXM2PMRY9QPKyXTlyYiPIwDQYJKoZIhvcNAQEL
BQAwbTELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExFjAUBgNVBAcM
DVNhbiBGcmFuY2lzY28xFTATBgNVBAoMDEV4YW1wbGUgQ29ycDEaMBgGA1UEAwwR
ZXhhbXBsZWRvbWFpbi5jb20wHhcNMjUwMTE1MDU0ODE0WhcNMjYwMTE1MDU0ODE0
WjBtMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwN
U2FuIEZyYW5jaXNjbzEVMBMGA1UECgwMRXhhbXBsZSBDb3JwMRowGAYDVQQDDBFl
eGFtcGxlZG9tYWluLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
ANP95CKhI3d5KcqUvBK8LEdowIg+I3FGLwkl3rHYaJYqWHYm0ZxPrikMgc4LcfK4
W/LD5hfOc5iH5h2iaIpP6qMoKmQIlSNR2Azc+C2h3uv7KVPrTs2ep0QOEMwroyVE
E06BboFY+FgoR+v05AS+WhKo2qeV9XdDC26/ItOeAyXxUZOpeQ6r119FCQYXRxTS
YZJa7i+4l2NiHRJ4dmvBjEa81MSVdjY6Qa3UTa867jVtLmOTuCNQoIjDHUjkJdUt
pg6N9Un877Fh00pRWb8pq3V6iLwGxtW/BGG3wpwIDErwtVaP1O6PG0Kpm3+IHVlu
OBoKxoM5sB0DJhLIHc0d7dkCAwEAAaMhMB8wHQYDVR0OBBYEFKHhe5ZlKbAyZ6XZ
r811dnx2wHcKMA0GCSqGSIb3DQEBCwUAA4IBAQC8vzGCa52U7Q2dj/nCXlJ7HSTH
nGsNuBQv3ZSzt5JVwHvo+SoK9H1KmVeqAC3NkLva5LrH024nQzqfhHKFUBZflLmQ
E/8EiQRl/DwyG2Ii/vNxBbaty2MSbXg6c4/34z1GB4rsk5ii5Y7LdjPIVokW+J4y
CLGu7kU3AIhESPEGnpGk0hP9qAAnnGB0kOuqi8YGYfGwPnWUletHMZc5iokLBXN5
mvB67t4mJLjOvbzqFpD06sRfsXU8Aj8SWK3kfVNyBzYTJAnIp9IZ7ZXv1VVc8lP2
dkib3CNQrVk47/YgPKoUa3Wyf7p0X3PlcfAZyVRri6PM0Zk89kOT/luw9O33
-----END CERTIFICATE-----

Certificate Expiry Date : 2026-01-15 05:48:14
================================================================================
```
