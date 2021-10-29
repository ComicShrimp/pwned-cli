import typer
from commands import PasswordPwnedSearch

app = typer.Typer()


@app.command()
def password(password_typed: str = typer.Option(..., prompt=True, hide_input=True)):
    password_hash, count = PasswordPwnedSearch(password_typed=password_typed).verify()

    typer.echo(f"Your password hash is: {password_hash}")
    typer.echo(f"Your password was found: {count} time(s) in database")


@app.callback()
def callback():
    """
    pwned CLI
    """


if __name__ == "__main__":
    app()
