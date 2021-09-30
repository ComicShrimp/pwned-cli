import typer


def main(password: str = typer.Option(..., prompt=True, hide_input=True)):
    typer.echo(f"Your password: {password}")


if __name__ == "__main__":
    typer.run(main)
