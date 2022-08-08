#!/usr/bin/env python
from gendiff.engine.mainstr import parser
from gendiff.gendiff import generate_diff


def main():
    first_file, second_file, format_ = parser()
    diff = generate_diff(first_file, second_file, format_)
    print(diff)


if __name__ == '__main__':
    main()
