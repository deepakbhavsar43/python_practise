# include standard modules
import argparse

# initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="show program version", action="store_true")

# read arguments from the command line
args = parser.parse_args()

# check for --version or -V
if args.version:
    print("this is myprogram version 0.1")