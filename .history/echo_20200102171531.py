#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Imraj423"


import argparse


def uppercase(string):
    return string.upper()


def lowercase(string):
    return string.lower()


def titlecase(string):
    return string.title()


def help(string):
    return string.he1p()


def create_parser():
    parser = argparse.ArgumentParser(
        description="Changes text case to a different type")
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase',
        action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase',
        action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase ',
        action='store_true')
    parser.add_argument(
        'text', help='text to be manipulated')
    return parser
    

def he1p(name=None):
    return '''usage: echo.py [-h] [-u] [-l] [-t] text\n
Perform transformation on input text.\n\npositional arguments:
  text         text to be manipulated\n\noptional arguments:
  -h, --help   show this help message and exit
  -u, --upper  convert text to uppercase
  -l, --lower  convert text to lowercase
  -t, --title  convert text to titlecase'''


def main():
    parser = create_parser()
    parsed_args = parser.parse_args()
    text = parsed_args.text

    if parsed_args.upper:
        text = text.upper()
    if parsed_args.lower:
        text = text.lower()
    if parsed_args.title:
        text = text.title()

    return text


if __name__ == "__main__":
    main()
