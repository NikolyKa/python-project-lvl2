#!/usr/bin/env python

from gendiff.mainstr import parser
from gendiff.gendiff import generate_diff


def main():
    first_file, second_file, format = parser()
    diff = generate_diff(first_file, second_file, format)
    print(diff)


if __name__ == '__main__':
    main()
