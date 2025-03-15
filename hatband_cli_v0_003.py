import click
import sys
import pickle
import os


from hatband_v0_003 import Hatband


version = "v0.0003"
HATBAND_FILE = 'hatband.pkl'


@click.group()
def hatband_group():
    """
    Hatband CLI
    """
    pass


@hatband_group.command()
@click.option('--hatband-name', required=True, help='Hatband category')
@click.option('--key', required=True, help='Record key')
@click.option('--value', required=True, help='Record value')
@click.option('--storage-dir', default='hatband_storage', help='Storage directory')
def insertl(hatband_name, key, value, storage_dir):    
    try:
        """
        Insert record at the left.
        """
        hatband = Hatband(storage_dir=storage_dir)
        record = {'hatband': hatband_name, 'key': key, 'value': value}
        index = hatband.hatband_insertL(record)
        click.echo(f"Inserted at index: {index}")
    except Exception as e:
        click.echo(f"Error: {e}")

@hatband_group.command()
@click.option('--hatband-name', required=True, help='Hatband category')
@click.option('--key', required=True, help='Record key')
@click.option('--value', required=True, help='Record value')
@click.option('--storage-dir', default='hatband_storage', help='Storage directory')
def insertr(hatband_name, key, value, storage_dir):
    """
    Insert record at the right.
    """
    hatband = Hatband(storage_dir=storage_dir)
    record = {'hatband': hatband_name, 'key': key, 'value': value}
    index = hatband.hatband_insertR(record)
    click.echo(f"Insert at index: {index}")


@hatband_group.command()
@click.option('--hatband-name', required=True, help='Hatband category')
@click.option('--key', required=True, help='Record key')
@click.option('--value', required=True, help='Record value')
@click.option('--storage-dir', default='hatband_storage', help='Storage directory')
def insertm(hatband_name, key, value, storage_dir):
    """
    Insert record in the middle.
    """
    hatband = Hatband(storage_dir=storage_dir)
    record = {'hatband': hatband_name, 'key': key, 'value': value}
    index = hatband.hatband_insertM(record)
    click.echo(f"Inserted at index: {index}")


@hatband_group.command()
@click.option('--hatband-name', required=True, help='Hatband category')
@click.option('--key', required=True, help='Record key')
@click.option('--index', type=int, help='Record index (optional)')
@click.option('--storage-dir', default='hatband_storage', help='Storage directory')
def retrieve(hatband_name, key, index, storage_dir):
    """
    Retrieve record
    """
    hatband = Hatband(storage_dir=storage_dir)
    record, retrieved_index = hatband.hatband_retrieve(hatband_name, key, index)
    if record:
        click.echo(f"Retrieved record: {record}, at index: {retrieved_index}")
    else:
        click.echo("Record not found.")


@hatband_group.command()
@click.option('--hatband-name', required=True, help='Hatband category')
@click.option('--storage-dir', default='hatband_storage', help='Storage directory')
def list_records(hatband_name, storage_dir='hatband_storage'):
    click.echo(f"Hatband name: {hatband_name}, Storage dir: {storage_dir}")

    try:
        """
        Lists all records in a given category.
        """
        hatband = Hatband(storage_dir=storage_dir)
        records = hatband.categories.get(hatband_name)
        if records:
                for record in records:
                    click.echo(record)
        else:
            click.echo("No records found.")

    except Exception as e:
            click.echo(f"Error: {e}")

def run_interactive_cli():
    hatband = Hatband()
    print("Welcome to Hatband CLI (Interactive Mode)!")
    while True:
        try:
            command_str = input("> ").strip()
            if not command_str:
                continue
            if command_str.lower() == "exit":
                break


            try:
                hatband_group(command_str.split())
            except click.exceptions.NoSuchOption as e:
                click.echo(f"Error: {e}")
            except click.exceptions.BadParameter as e:
                click.echo(f"Error: {e}")
            except click.exceptions.UsageError as e:
                click.echo(f"Error: {e}")
            except SystemExit:
                pass
        except Exception as e:
            click.echo(f"Error: {e}")
    click.echo("Goodbye!")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(click.get_current_context().command_path if click.has_current_context() else "No Click context")
        hatband_group()
    else:
        run_interactive_cli()

