# diskalert
A script to alert on a defined disk usage percentile

## Installation

Clone the repository, and then in the directory:

```sudo pipx install```

This will create the diskalert Python package in the default location, the diskalert binary in your path, and will install the diskalert man pages.

Alternately, install [UV](https://docs.astral.sh/uv/getting-started/installation/), then use:

```uv tool install .```

After installation, don't forget to set up the `/etc/diskalert.conf` file.

## Updating

Simply rerun the setup.py installer after cloning or pulling the repository. This will **not** update the `/etc/diskalert.conf` file.

## Manual testing

If you have UV installed, you can test the script from this directory via:

```uvx .```
