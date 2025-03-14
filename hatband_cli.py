import click
import pickle
import os


from hatband_v0_003 import Hatband


HATBAND_FILE = 'hatband.pkl'

def load_hatband():
    print("Loading hatband.")
    if os.path.exists(HATBAND_FILE):
        with open(HATBAND_FILE, 'rb') as f:
            print("Hatband loaded.")
            return pickle.load(f)
    else:
        print("New hatband created.")
        return Hatband()
    
def save_hatband(hatband):
    print("Saving hatband.")
    with open(HATBAND_FILE, 'wb') as f:
        pickle.dump(hatband, f)
    print("Hatband Saved")

@click.group()
def cli():
    """
    Hatband CLI
    """
    pass


@cli.command()
@click.option('--hatband-name', required=True, help='Hatband category')
@click.option('--key', required=True, help='Record key')
@click.option('--value', required=True, help='Record value')

def insertl(hatband_name, key, value):
    """
    Insert record at the left.
    """
    hatband = Hatband()
    record = {'hatband': hatband_name, 'key': key, 'value': value}
    index = hatband.hatband_insertL(record)
    click.echo(f"Inserted at index: {index}")

@cli.command()
@click.option('--hatband-name', required=True, help='Hatband category')
@click.option('--key', required=True, help='Record key')
@click.option('--value', required=True, help='Record value')

def insertr(hatband_name, key, value):
    """
    Insert record at the right.
    """
    hatband = Hatband()
    record = {'hatband': hatband_name, 'key': key, 'value': value}
    index = hatband.hatband_insertR(record)
    click.echo(f"Insert at index: {index}")

@cli.command()
@click.option('--hatband-name', required=True, help='Hatband category')
@click.option('--key', required=True, help='Record key')
@click.option('--value', required=True, help='Record value')
def insertm(hatband_name, key, value):
    """
    Insert record in the middle.
    """
    hatband = Hatband()
    record = {'hatband': hatband_name, 'key': key, 'value': value}
    index = hatband.hatband_insertM(record)
    click.echo(f"Inserted at index: {index}")

@cli.command()
@click.option('--hatband-name', required=True, help='Hatband category')
@click.option('--key', required=True, help='Record key')
@click.option('--index', type=int, help='Record index (optional)')
def retrieve(hatband_name, key, index):
    """
    Retrieve record
    """
    hatband = Hatband()
    record, retrieved_index = hatband.hatband_retrieve(hatband_name, key, index)
    if record:
        click.echo(f"Retrieved record: {record}, at index: {retrieved_index}")
    else:
        click.echo("Record not found.")

@cli.command()
@click.option('--hatband-name', required=True, help='Hatband category')
def list_records(hatband_name):
    """
    Lists all records in a given category.
    """
    hatband = load_hatband()
    print(f"Hatband Categories: {hatband.categories}")
    records = hatband.categories[hatband_name]
    save_hatband(hatband)
    if records:
        for record in records:
            click.echo(record)
    else:
        click.echo("No records found.")


if __name__ == '__main__':
    cli()