#!/usr/bin/env python
from gendiff.engine.parser import file_parser
from gendiff.gendiff import generate_diff


def main():
    received_files = file_parser()
    diff = generate_diff(received_files.first_file,
                         received_files.second_file,
                         received_files.format)
    print(diff)


if __name__ == '__main__':
    main()
