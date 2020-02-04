import argparse
import math

parser=argparse.ArgumentParser(description='Calculate volume of a Cylinder')
parser.add_argument('-r', '--radius', type=int, metavar='', required=True, help='radius of cylinder')
parser.add_argument('-H', '--height', type=int, metavar='', required=True, help='height of the circle')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args=parser.parse_args()

def cylinder(r,h):
    vol = (math.pi) * (r**2) * (h)
    return vol

if __name__ ==  "__main__":
    volume = cylinder(args.radius, args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print('volume of cylinder with radius %s is %s'%args.radius,args.height,volume)