# bapt/cli.py
import click

@click.group()
def main():
    """
    bapt is a user-friendly wrapper for the apt package manager.
    """
    pass

@main.command()
def history():
    """Displays apt history from /var/log/apt/history.log."""
    click.echo("Executing history command...")

@main.command()
def rollback():
    """Rolls back the last apt transaction."""
    click.echo("Executing rollback command...")

@main.command()
@click.argument('package')
def why(package):
    """Shows which manually installed packages depend on a package."""
    click.echo(f"Executing why command for package: {package}")

# You can add search and show commands in the same way
# For now, we'll leave them out for brevity

if __name__ == "__main__":
    main()