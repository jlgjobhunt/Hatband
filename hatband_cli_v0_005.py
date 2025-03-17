import click
import sys
import pickle
import os
import shlex


from hatband_v0_005 import Hatband
from hatband_cli_multiprocessing_mgmt import HatbandCommunicatorCLI
from hatband_multiprocessing_mgmt import HatbandCommunicator
import hatband_multithreading_mgmt


version = "v0.005"
HATBAND_FILE = 'hatband.pkl'


@click.group()
def hatband_group():
    """
    Hatband CLI v0.005
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
def list_records(hatband_name, storage_dir):
    """
    Lists records in a Hatband category.
    """
    try:
        hatband = Hatband(storage_dir=storage_dir)
        records = hatband.categories.get(hatband_name)
        if records:
            for record in records:
                click.echo(record)
        
        else:
            click.echo("No records found.")
    except Exception as e:
        click.echo(f"DEBUGGING | Error: {e}")

# Nest the multiprocessing CLI command group.
hatband_group.add_command(HatbandCommunicatorCLI.multicpu_utilities)


def run_interactive_cli():
    hatband = Hatband()
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
        
