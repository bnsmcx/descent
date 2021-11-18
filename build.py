import typer

app = typer.Typer()


@app.command()
def md():
    """Output as markdown"""


@app.command()
def html():
    """Output as html"""


@app.command()
def pdf():
    """Output as pdf"""


@app.callback()
def callback():
    """Generate documentation as pdf, html, or md"""


if __name__ == "__main__":
    app()
