import click
import json
import logging
import os
import shlex
import sys


from hatband_v0_009 import Hatband
from hatband_record_v0_009 import Record
from hatband_cli_multiprocessing_mgmt_v0_009 import HatbandCommunicatorCLI
from hatband_multiprocessing_mgmt_v0_009 import HatbandCommunicator
import hatband_multithreading_mgmt_v0_009


version = "v0.005"
HATBAND_FILE = 'hatband.pkl'


@click.group()
def hatband_group():
    """
    Hatband CLI v0.005
    """
    pass


@hatband_group.command()
@click.option('--hatband-name', required=True, help="Name of the Hatband.")
@click.option('--key', required=True, help="Key of the record.")
@click.option('--value', required=True, help="Value of the record.")
def create_record(hatband_name, key, value):
    """Creates a new record in the Hatband."""
    hatband = Hatband(hatband_name)
    record = hatband.add_record(key, value)
    hatband.save_hatband_to_file(hatband.name, hatband.categories[record.short_index_key])

    # DEBUGGING | REMOVE LATER
    hatband_data = load_hatband_data(hatband_name)
    logging.debug(f"DEBUGGING | Loaded data from hatband_storage/{hatband_name}.json | {json.dumps(hatband_data)}")

def load_hatband_data(hatband_name):
    hatband_file = os.path.join("hatband_storage", f"{hatband_name}.json")
    if os.path.exists(hatband_file):
        with open(hatband_file, 'r') as f:
            return json.load(f)
    return []

def save_hatband_data(hatband_name, data):
    hatband_file = os.path.join("hatband_storage", f"{hatband_name}.json")
    with open(hatband_file, 'w') as f:
        json.dump(data, f, indent=4)

@hatband_group.command()
@click.option('--hatband-name', required=True, help='Hatband category')
@click.option('--key', required=True, help='Record key')
@click.option('--value', required=True, help='Record value')
@click.option('--storage-dir', default='hatband_storage', help='Storage directory')
def insertl(hatband_name, key, value, storage_dir):
    """
    Insert record at the left.
    """
    try:
        hatband = Hatband(storage_dir=storage_dir)
        record = {'hatband': hatband_name, 'key': key, 'value': value}
        index = hatband.hatband_insertL(record)
        click.echo(f"Inserted at index: {index}")
    except Exception as e:
        click.echo(f"DEBUGGING | Error: {e}")

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
@click.option('--hatband-name', required=True, help='Hatband category name')
@click.option('--key', required=True, help='Record key')
@click.option('--index', type=int, help='Record index (optional)')
@click.option('--storage-dir', default='hatband_storage', help='Storage directory')
def retrieve(hatband_name, key, index, storage_dir):
    """
    Retrieve record
    """
    hatband = Hatband(hatband_name, storage_dir=storage_dir)
    record, retrieved_index = hatband.hatband_retrieve(hatband_name, key, index)
    if record:
        click.echo(f"Retrieved record: {record}, at index: {retrieved_index}")
    else:
        click.echo("Record not found.")

@hatband_group.command()
@click.option('--hatband-name', required=True, help='Hatband category')
@click.option('--storage-dir', default='hatband_storage', help='Storage directory')
def list_records(hatband_name, storage_dir):
    """
    Lists records in a Hatband category.
    """
    try:
        hatband = Hatband(hatband_name)
        records = hatband.categories.get(hatband_name)

        if records:
            for record in records:
                click.echo(json.dumps(record, indent=4))
        
        else:
            click.echo("No records found.")
    except FileNotFoundError:
        click.echo(f"Hatband '{hatband_name}' not found.")
    except Exception as e:
        click.echo(f"DEBUGGING | Error: {e.__str__()}")

# Nest the multiprocessing CLI command group.
hatband_group.add_command(HatbandCommunicatorCLI.multicpu_utilities)


def run_interactive_cli():
    hatband_name = input("Enter Hatband name: ")
    hatband = Hatband(hatband_name)
    print("Welcome to Hatband CLI (now supporting multiple CPUs)!")
    while True:
        try:
            command_str = input("> ").strip()
            if not command_str:
                continue
            if command_str.lower() == "exit":
                break


            try:

                command_list = shlex.split(command_str)

                # Special handling for --help.
                if command_list[0] == '--help':
                    with hatband_group.make_context(None, []) as ctx:
                        click.echo(hatband_group.get_help(ctx))
                    continue

                if not hatband_group.commands.get(command_list[0]) and not HatbandCommunicatorCLI.multicpu_utilities.commands.get(command_list[0]):
                    click.echo(f"DEBUGGING | Error: No such command '{command_list[0]}'.")
                    continue

                hatband_group(command_list)

            except click.exceptions.NoSuchOption as e:
                click.echo(f"DEBUGGING | Error: {e}")
            except click.exceptions.BadParameter as e:
                click.echo(f"DEBUGGING | Error: {e}")
            except click.exceptions.UsageError as e:
                click.echo(f"DEBUGGING | Error: {e}")
            except SystemExit as e:
                if e.code == 0:
                    pass
                else:
                    click.echo(f"DEBUGGING | Error: {e}")
        except Exception as e:
            click.echo(f"DEBUGGING | Error: {e}")

    click.echo("Goodbye!")


if __name__ == '__main__':
        if len(sys.argv) > 1:
            hatband_group()
        else:
            run_interactive_cli()
        
