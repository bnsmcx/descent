import os

import typer

app = typer.Typer()


@app.command()
def unify():
    """Unite all the nested READMEs into a single, unified, top level file"""
    with open("unified_README.md", "x") as unified:
        for current_dir, sub_dirs, files in os.walk('.'):
            if "test_README.md" in files:
                nested_readme = f"{current_dir}/test_README.md"
                with open(nested_readme, 'r') as nested:
                    unified.writelines(nested.readlines())
                os.remove(nested_readme)


@app.callback()
def callback():
    """Transform some aspect of the current project"""


if __name__ == "__main__":
    app()
