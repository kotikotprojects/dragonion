import sys

from .authentication import authentication
from .authentication.utils.results import ServiceAuthResult


def auth_tui() -> ServiceAuthResult:
    service_auth: ServiceAuthResult = authentication.app.run()

    if isinstance(service_auth, ServiceAuthResult):
        return service_auth
    else:
        print('Error in service auth. Exiting.')
        sys.exit(1)
