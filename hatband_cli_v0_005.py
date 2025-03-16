import click
import sys
import pickle
import os


from hatband_v0_005 import Hatband
import hatband_multiprocessing_mgmt
import hatband_multithreading_mgmt


version = "v0.005"
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



# Due to v0.003 complications with list_records,
# it became necessary to attempt a manual equivalent.

def list_records(args):
    """Manually lists records based on command-line arguments."""

    print(args)
    hatband_name = None
    storage_dir = 'hatband_storage'

    # Isolate the problem:
    if "--hatband-name" in args:
        hatband_name_index = args.index("--hatband-name")
        if hatband_name_index + 1 < len(args):
            hatband_name = args[hatband_name_index + 1]
        else:
            print("Error: Missing value for --hatband-name")
            return

    if "--storage-dir" in args:
        storage_dir_index = args.index("--storage-dir")
        if storage_dir_index + 1 < len(args):
            storage_dir = args[storage_dir_index + 1]
        else:
            print("Error: Missing value for --storage-dir")
            return
        
    if hatband_name is None:
        print("Error: --hatband-name is required.")
        return

    print(f"hatband_name: {hatband_name}")
    print(f"storage_dir: {storage_dir}")
    
    try:
        hatband = Hatband(storage_dir=storage_dir)
        records = hatband.categories.get(hatband_name)
        if records:
            for record in records:
                print(record)
        else:
            print("No records found.")
    except Exception as e:
        print(f"Error: {e}")

    

# Main has to be at the bottom to catch
# what gooiness v0.004 has to throw at the wall.

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'list_records':
        list_records(sys.argv[2:])
    else:
        run_interactive_cli()
        print(click.get_current_context().command_path if click.has_current_context() else "No Click context")
        hatband_group()
        