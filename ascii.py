#!/usr/bin/env python

'''
Simple Image to ASCII Art conversion.
'''

import os
import sys
import click
from PIL import Image

DENSITY = '¶@ØÆMåBNÊßÔR#8Q&mÃ0À$GXZA5ñk2S%±3Fz¢yÝCJf1t7ªLc¿+?(r/¤²!*;"^:,\'.` '


def _frame_to_ascii(im, low=10, high=10, columns=80, inverse=False):
    density_map = '¶' * high + DENSITY + ' ' * low
    if inverse:
        density_map = density_map[::-1]
    if im.mode != 'RGB':
        im = im.convert('RGB')
    width, height = im.size
    height = height * columns // 2 // width
    width = columns
    im = im.resize((width, height))
    pixels = [min(sum(i)//3, 254) for i in im.get_flattened_data()]
    ascii = []
    while pixels:
        ascii.append(
            ''.join(density_map[-1 - p * len(density_map) // 255]
            for p in pixels[:columns])
        )
        pixels = pixels[columns:]
    return '\n'.join(ascii)


def to_ascii(filepath, low=10, high=10, columns=80, inverse=False):
    '''
    Converts an image to ASCII Art. Returns text.
    - filepath: the image itself
    - low: how much to enhance dark areas
    - high: how much to enhance light areas
    - inverse: inverse colors
    '''
    im = Image.open(filepath)
    return _frame_to_ascii(im, low, high, columns, inverse)


def gif_to_ascii_folder(filepath, folder, low=10, high=10, columns=80, inverse=False):
    '''
    Extracts each frame of an animated GIF and writes ASCII text files
    named 0001.txt, 0002.txt, ... into folder.
    '''
    os.makedirs(folder, exist_ok=True)
    im = Image.open(filepath)
    for i in range(im.n_frames):
        im.seek(i)
        text = _frame_to_ascii(im, low, high, columns, inverse)
        with open(os.path.join(folder, f'{i + 1:04d}.txt'), 'w') as f:
            f.write(text)


@click.command()
@click.argument('filepath')
@click.argument('folder', required=False)
@click.option('--low', default=10, help='Enhance dark areas of the image')
@click.option('--high', default=5, help='Enhance bright areas of the image')
@click.option('--columns', default=80, help='ASCII text width')
@click.option('--inverse', is_flag=True, help='Inverse colors')
def to_ascii_cmd(filepath, folder, low, high, columns, inverse):
    if folder:
        im = Image.open(filepath)
        if getattr(im, 'is_animated', False):
            gif_to_ascii_folder(filepath, folder, low, high, columns, inverse)
            return
    print(to_ascii(filepath, low, high, columns, inverse))


if __name__ == "__main__":
    to_ascii_cmd()
