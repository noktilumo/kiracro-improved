import click
from kiracro_improved.runner import run

@click.command()
@click.option('--holdable', type=bool, default=False, help='Hold to macro')
def main(holdable):
    run(holdable)

if __name__ == "__main__":
    main()
