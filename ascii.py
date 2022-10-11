#!/usr/bin/env python

'''
Simple Image to ASCII Art conversion.
'''

import sys
import click
from PIL import Image

DENSITY = '¶@ØÆMåBNÊßÔR#8Q&mÃ0À$GXZA5ñk2S%±3Fz¢yÝCJf1t7ªLc¿+?(r/¤²!*;"^:,\'.` '


def to_ascii(filepath, low=10, high=10, columns=80, inverse=False):
    '''
    Converts an image to ASCII Art. Returns text.
    - filepath: the image itself
    - low: how much to enhance dark areas
    - high: how much to enhance light areas
    - inverse: inverse colors
    '''
    density_map = '¶' * high + DENSITY + ' ' * low
    if inverse:
        density_map = density_map[::-1]
    im = Image.open(filepath)
    width, height = im.size
    height = height * columns // 2 // width
    width = columns
    im = im.resize((width, height))
    pixels = [sum(i)//3 for i in im.getdata()]
    ascii = []
    while pixels:
        ascii.append(
            ''.join(density_map[-1 - p * len(density_map) // 255]
            for p in pixels[:columns])
        )
        pixels = pixels[columns:]
    return '\n'.join(ascii)


@click.command()
@click.argument('filepath')
@click.option('--low', default=10, help='Enhance dark areas of the image')
@click.option('--high', default=5, help='Enhance bright areas of the image')
@click.option('--columns', default=80, help='ASCII text width')
@click.option('--inverse', is_flag=True, help='Inverse colors')
def to_ascii_cmd(filepath, low, high, columns, inverse):
    print(to_ascii(filepath, low, high, columns, inverse))


if __name__ == "__main__":
    to_ascii_cmd()
