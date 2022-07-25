#!/usr/bin/env python

from gendiff.mainstr import parser
from gendiff.diff import generate_diff


def main():
    first_file, second_file, format = parser()
    diff = generate_diff(first_file, second_file)
    print(diff)


if __name__ == '__main__':
    main()
