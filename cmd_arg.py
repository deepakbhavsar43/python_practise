import sys

arguments = len(sys.argv) -1

#print("the script has the name %s" %(sys.argv[0]))
#print("the script has the name %s" %(arguments))
position = 1
while (arguments >= position):
    print ("parameter %i: %s" % (position, sys.argv[position]))
    position = position + 1