import click

@click.group()
def hatband_group():
    pass

@hatband_group.command()
def test_command():
    click.echo("Test command executed!")

@hatband_group.command()
def list_records():
    click.echo("List records command executed!")

if __name__ == "__main__":
    hatband_group()