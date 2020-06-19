#! /usr/bin/env python
# -*- coding: utf-8 -*-
""" Click Sample : Hello World. """
import click


@click.command()
@click.option('--name', '-n', default='World')
def main(name):
    """ Echo Hello World. """
    click.echo(f'Hello, {name}!')
