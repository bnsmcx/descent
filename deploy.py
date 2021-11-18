import typer

app = typer.Typer()


@app.callback()
def callback():
    """Begin your project here"""
    pass


if __name__ == "__main__":
    app()
