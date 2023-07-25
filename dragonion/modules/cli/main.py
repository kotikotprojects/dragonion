import click

import os

from ..tui import app


def validate_username(_: click.Context, __: click.Parameter, value: str | None):
    if value is not None and not (4 <= len(value) <= 14):
        raise click.BadParameter("Username length must be from 4 to 14 symbols")
    else:
        return value


@click.command()
@click.option('--auth', '-a', required=False, type=str,
              help='Service name (.auth file with this name should exist in workdir)')
@click.option('--username', '-u', required=False, type=str,
              help='Set username', callback=validate_username)
def cli(auth: str | None, username: str | None):
    if auth is not None and os.path.isfile(f'{auth}.auth'):
        from ..tui.authentication.utils.results import ServiceAuthResult
        app._pre_service_auth = ServiceAuthResult(f'{auth}.auth')

    if username is not None:
        app._pre_username = username

    app.run()
