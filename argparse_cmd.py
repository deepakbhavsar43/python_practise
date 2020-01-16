import argparse

parse=argparse.ArgumentParse(description="mul")

parse.add_argument('-b','--base',type=int)
parse.add_argument('-p','--power',type=int)
args=parser.parse_args()


a=base
b=power

print(a*b)	