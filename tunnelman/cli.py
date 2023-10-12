from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def valid_ip(ip: str) -> str:
    """
    Checks if an IP address is valid.
    If it is, returns the IP address, else raises an error.
    """
    split_ip: list[str] = ip.split(".")
    if len(split_ip) != 4:
        raise ValueError("IP address must have 4 octets.")
    for octet in split_ip:
        if int(octet) < 0 or int(octet) > 255:
            raise ValueError("Octet must be between 0 and 255.")
    return ip


def cli():
    """Command line interface for tunnelman."""

    parser: ArgumentParser = ArgumentParser(
        prog="tunnelman",
        description="Tunnelman: A tunnel manager for linking tunnels to a"
        + "gateway server.",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )

    # TODO: Add version
    # parser.add_argument(
    #     "-v",
    #     "--version",
    #     action="version",
    #     version="%(prog)s {version}".format(version=__version__),
    # )

    parser.add_argument(
        "-g",
        "--gateways",
        type=valid_ip,
        help="The IPv4 address of the gateway server to connect to.",
        required=False,
        nargs="+",
    )

    parser.add_argument(
        "-ovh",
        "--ovh",
        help="Deploy a gateway server on  new OVH instance",
        required=False,
    )

    parser.add_argument(
        "-l",
        "--linode",
        help="Deploy a gateway server on a new Linode instance",
        required=False,
    )

    parser.add_argument(
        "-d",
        "--digitalocean",
        help="Deploy a gateway server on a new DigitalOcean instance",
        required=False,
    )

    parser.add_argument(
        "-a",
        "--aws",
        help="Deploy a gateway server on a new AWS instance",
        required=False,
    )

    parser.add_argument(
        "-v",
        "--vultr",
        help="Deploy a gateway server on a new Vultr instance",
        required=False,
    )

    parser.add_argument(
        "-c",
        "--cloudflare",
        help="Deploy a gateway server on a new Cloudflare instance",
        required=False,
    )

    parser.add_argument(
        "-p",
        "--packet",
        help="Deploy a gateway server on a new Packet instance",
        required=False,
    )

    parser.add_argument(
        "-a",
        "--azure",
        help="Deploy a gateway server on a new Azure instance",
        required=False,
    )

    parser.add_argument(
        "-gcp",
        "--google",
        help="Deploy a gateway server on a new Google Cloud Platform instance",
        required=False,
    )

    if parser.parse_args().gateways:
        print("Creating gateway on Docker...")
        exit(1)
    elif parser.parse_args().ovh:
        print("Creating gateway on OVH...")
        exit(1)
    elif parser.parse_args().linode:
        print("Creating gateway on Linode...")
        exit(1)
    elif parser.parse_args().digitalocean:
        print("Creating gateway on DigitalOcean...")
        exit(1)
    elif parser.parse_args().aws:
        print("Creating gateway on AWS...")
        exit(1)
    elif parser.parse_args().vultr:
        print("Creating gateway on Vultr...")
        exit(1)
    elif parser.parse_args().cloudflare:
        print("Creating gateway on Cloudflare...")
        exit(1)
    elif parser.parse_args().packet:
        print("Creating gateway on Packet...")
        exit(1)
    elif parser.parse_args().azure:
        print("Creating gateway on Azure...")
        exit(1)
    elif parser.parse_args().google:
        print("Creating gateway on Google Cloud Platform...")
        exit(1)
    else:
        print("No gateways specified. Exiting...")
        exit(1)


if __name__ == "__main__":
    cli()
