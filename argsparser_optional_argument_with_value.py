# include standard modules
import argparse

# initiate the parser
parser = argparse.ArgumentParser()

# add long and short argument
parser.add_argument("--width", "-w", help="set output width")

# read arguments from the command line
args = parser.parse_args()

# check for --width
if args.width:
    print("set output width to %s" % args.width)