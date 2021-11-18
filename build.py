import typer

app = typer.Typer()


@app.callback()
def callback():
    """Generate documentation as pdf, html, or md"""


if __name__ == "__main__":
    app()
