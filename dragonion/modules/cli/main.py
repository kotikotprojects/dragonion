import click

import os

from ..tui.tui import auth_tui


@click.command()
@click.option('--auth', '-a', required=False, type=str,
              help='Service name (.auth file with this name should exist in workdir)')
def cli(auth: str | None):
    if auth is not None and os.path.isfile(f'{auth}.auth'):
        from ..tui.authentication.utils.results import ServiceAuthResult
        auth_result = ServiceAuthResult(f'{auth}.auth')
    else:
        auth_result = auth_tui()

    print(auth_result)
