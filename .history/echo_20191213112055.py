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


def create_parser():
    parser = argparse.ArgumentParser(
        description="Changes text case to a different type")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
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
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--upper", "-u", action="store_true",
                        help='convert text to uppercase')
    parser.add_argument("--lower", "-l", action="store_true",
                        help='convert text to lowercase')
    parser.add_argument("--title", "-t", action="store_true",
                        help='convert text to titlecase')
    parser.add_argument("-help", "--h", action="store_true",
                        help='show this help message and exit')
    args = parser.parse_args()
    if args.upper:
        print(uppercase('hello world'))
    if args.lower:
        print(lowercase('hello world'))
    if args.title:
        print(titlecase('hello world'))
    if args.help:
        print(he1p())


if __name__ == "__main__":
    main()
