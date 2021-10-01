import typer

app = typer.Typer()


@app.command()
def password(password: str = typer.Option(..., prompt=True, hide_input=True)):
    typer.echo(f"Your password: {password}")


@app.callback()
def callback():
    """
    pwned CLI
    """


if __name__ == "__main__":
    app()
