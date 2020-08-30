#!/usr/bin/python3
"""Reinstall and run tests."""
import argparse
import configparser
import re
import subprocess

import os


def get_package(path_dir: str = ".") -> str:
    """Look for the package name."""
    os.chdir(path_dir)
    if os.path.isfile("setup.cfg"):
        cfg = configparser.ConfigParser()
        cfg.read("setup.cfg")
        name = cfg.get("metadata", "name")
    else:
        pat_setup_name = re.compile(r"name=(.+)")
        with open("setup.py", "r") as file:
            for line in file:
                setup_name = pat_setup_name.search(line)
                if setup_name:
                    name = setup_name[1]
                    break
    return name


def parse_arguments() -> argparse.Namespace:
    """Get CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Simple CLI to reinstall a local Python package."
    )
    parser.add_argument(
        "--dir",
        metavar="<PATH>",
        type=str,
        default=".",
        help="Path to directory. Default: '.'",
    )
    parser.add_argument(
        "--test", action="store_true", help="Run pytest after this.",
    )
    args = parser.parse_args()

    return args


def run_cmd_reinstall(dir: str = ".", pytest: bool = False):
    """Run the command line args."""
    name = get_package(dir)
    try:
        print(f"Uninstalling {name}")
        subprocess.check_output(
            ["pip", "uninstall", name, "-y"]
        )
        print(f"Installing {name}")
        subprocess.check_output(["pip", "install", "."])
        print(f"Successfully installed {name}")
    except subprocess.CalledProcessError as exc:
        print("Status : FAIL", exc.returncode, exc.output)
    if pytest:
        print("Running pytest")
        print(
            subprocess.check_output(["python", "-m", "pytest"]).decode("utf-8")
        )


if __name__ == "__main__":
    args = parse_arguments()

    run_cmd_reinstall(args.dir, args.test)
