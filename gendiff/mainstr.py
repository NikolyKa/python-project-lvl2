import argparse


def parser():
    pars = argparse.ArgumentParser(description='Compares two configuration \
    files and shows a difference.')
    pars.add_argument('first_file')
    pars.add_argument('second_file')
    pars.print_help()
