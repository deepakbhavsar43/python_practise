# include standard modules
import argparse

# define the program description
text = 'This is a test program. It demonstrates how to use the argparse module with a program description.'

# initiate the parser with a description
parser = argparse.ArgumentParser(description=text)
parser.parse_args()