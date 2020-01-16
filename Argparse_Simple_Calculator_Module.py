import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add', type=int, help='Addition', required=True)
parser.add_argument('-s', '--sub', type=int, help='Subtraction', required=True)
args = parser.parse_args()

def addition(x,y):
    return x+y

