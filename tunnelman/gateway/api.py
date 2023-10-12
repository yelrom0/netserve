from pulumi_docker import Provider as DockerProvider


class GatewayAPI:
    # TODO: Allow custom port and user name and keys
    # TODO: Make custom data type containing names and ips
    # TODO: Add ssh certs
    def create_docker(
        self,
        names: list[str],
        ips: list[str],
    ) -> list[DockerProvider]:
        # TOMORROW: Use pyinfra to install docker
        return [
            DockerProvider(
                resource_name=name,
                host=f"ssh://root@{ip}:22",
            )
            for name, ip in zip(names, ips)
        ]
