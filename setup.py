#!/usr/bin/env python3
"""
This python script creates the TLS certs that will be used by vault.  In addition, it will also generate
a data directory where vault will store all of its data (any secrets will be encrypted).
"""

import os
import pathlib
import subprocess


def main():
    # create the certs directory
    certs_dir = pathlib.Path.cwd().joinpath("certs")
    certs_dir.mkdir(exist_ok=True)

    # create the data directory where the vault data will be stored
    data_dir = pathlib.Path.cwd().joinpath("data")
    data_dir.mkdir(exist_ok=True)

    print("This may take some time, please be patient...")

    # create the certs in the certs directory
    os.chdir(str(certs_dir.absolute()))
    my_ip = (
        subprocess.run(
            "hostname -I | cut -d' ' -f1", check=True, capture_output=True, shell=True
        )
        .stdout.decode()
        .strip()
    )
    subprocess.run(
        f"openssl req -x509 -newkey rsa:4096 -nodes -keyout vault.key -out "
        f'vault.crt -days 365 -subj "/C=/ST=/L=/O=/CN={my_ip}" -addext "subjectAltName = IP:{my_ip}"',
        check=True,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    # generate the Diffie-Hellman parameter
    subprocess.run(
        f"openssl dhparam -out dhparam.pem 2048",
        check=True,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    print("All done!")


if __name__ == "__main__":
    main()
