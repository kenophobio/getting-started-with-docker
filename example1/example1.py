# example1/example1.py
from itertools import islice

import click


def fibonacci_sequence():
    i, j = 0, 1
    while True:
        yield i
        i, j = j, i + j


@click.command()
@click.option('--length', default=5, help='Length of the Fibonacci sequence.')
def example1(length):
    """Simple program that prints out LENGTH items of the Fibonacci sequence."""
    for i in islice(fibonacci_sequence(), length):
        click.echo('--> {}'.format(i))


if __name__ == '__main__':
    example1()
