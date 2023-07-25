from textual.widgets import Input


def handle_input_submit():
    from dragonion.modules.tui import app

    app.query_one(
        "#chat_input_field",
        expect_type=Input
    ).value = ""
