import click

import os

from ..tui.tui import app


@click.command()
@click.option('--auth', '-a', required=False, type=str,
              help='Service name (.auth file with this name should exist in workdir)')
@click.option('--identity', '-i', required=False, type=str,
              help='Identity username '
                   '(.id file with this name should exist in workdir)')
def cli(auth: str | None, identity: str | None):
    if auth is not None and os.path.isfile(f'{auth}.auth'):
        from ..tui.authentication.utils.results import ServiceAuthResult
        app._pre_service_auth = ServiceAuthResult(f'{auth}.auth')

    app.run()
