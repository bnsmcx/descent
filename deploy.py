import typer

app = typer.Typer()


@app.command()
def deploy():
    """Begin your project here"""
    pass


if __name__ == "__main__":
    app()
