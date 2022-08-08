import argparse


def parser():
    pars = argparse.ArgumentParser(description='Compares two configuration \
    files and shows a difference.')
    pars.add_argument('first_file')
    pars.add_argument('second_file')
    pars.add_argument('-f', '--format', help='set format of output',
                      default='stylish')
    args = pars.parse_args()

    return args.first_file, args.second_file, args.format
