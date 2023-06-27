import os
from .generated_auth.db import AuthFile


def create_service_auth(
        tor_data_directory_name: str,
        service_name: str = None,
        service_id: str = None,
        key: str = None
) -> str:
    """
    Creates .auth_private file to endpoint be accessible
    :param tor_data_directory_name: Current temp directory of tor
    :param service_name: Name of .auth file user got from server hoster
    :param service_id: Url part without .onion part
    :param key: base32-encoded key, user got from hoster
    :return: Returns .onion url of service
    """
    if service_name:
        auth = AuthFile(service_name)
        with open(os.path.join(os.path.join(tor_data_directory_name, 'auth'),
                               'service.auth_private'), 'w') as f:
            f.write(auth['auth'])

        return auth['host']
    elif service_id and key:
        with open(os.path.join(os.path.join(tor_data_directory_name, 'auth'),
                               'service.auth_private'), 'w') as f:
            f.write(f'{service_id}:descriptor:'
                    f'x25519:{key}')

        return f'{service_id}.onion'
