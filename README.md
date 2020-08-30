# pipterate

pipterate is a tiny CLI application to install and reinstall a local python module.

Depending of the packaging, `pip install -e .` may not work for some python modules. This script helps in the process of reinstalling during development for those cases.

An option is provided to run [pytest](https://docs.pytest.org) after the reinstallation, which obviously requires pytest.

## Installation
1. Clone this repository:
```shell
git clone https://github.com/carrascomj/pipterate.git
cd pipterate
```
2. Put the script under your path. For instance:
```shell
mv pipterate.py ~/.local/bin/pipterate
```
Personally, I prefer to remove the extension.

## Run the application:

    usage: pipterate.py [-h] [--dir <PATH>] [--test]

    Simple CLI to reinstall the a local Python package.

    optional arguments:
      -h, --help    show this help message and exit
      --dir <PATH>  Path to directory. Default: '.'
      --test        Run pytest after this.
