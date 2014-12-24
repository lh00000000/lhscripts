import random
import sys

for i in range(0,int(sys.argv[2])):
	random_lines = random.choice(open(sys.argv[1]).readlines())
	print random_lines,