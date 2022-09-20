#!/usr/bin/env python
from gendiff.engine.parser import parse
from gendiff.gendiff import generate_diff


def main():
    files = parse()
    diff = generate_diff(files.first_file, files.second_file, files.format)
    print(diff)


if __name__ == '__main__':
    main()
