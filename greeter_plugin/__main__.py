from pulumi.provider.experimental import component_provider_host

from greeter import Greeter

if __name__ == "__main__":
    component_provider_host(
        components=[Greeter],
        name="greeter",
    )
