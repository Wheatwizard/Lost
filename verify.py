import argparse
from interpreter import Interpreter
from KleinException import KleinException

parser = argparse.ArgumentParser(description="Klein Interpreter")

parser.add_argument(
	"-a",
	"--ASCII-in",
	action = "store_true",
	help = "Takes input as ASCII code points"
)

parser.add_argument(
	"-A",
	"--ASCII-out",
	action = "store_true",
	help = "Outputs as ASCII code points"
)

parser.add_argument(
	"-c",
	"--ASCII",
	action = "store_true",
	help = "Takes input and outputs by ASCII code points"
)

parser.add_argument(
	"source",
	metavar = "Source",
	help = "The name of the file from which the source is read."
)

parser.add_argument(
	"input",
	metavar = "Input",
	nargs = "*",
	help = "Integer input."
)

args = parser.parse_args()

with open(args.source) as file:
	source = file.read()

maxX = len(source.strip().split("\n"))
maxY = max(map(len,source.strip().split("\n")))

for x in range(maxX):
	for y in range(maxY):
		if args.ASCII or args.ASCII_in:
			a=Interpreter(source,map(ord," ".join(args.input)),x,y)
		else:
			a=Interpreter(source,map(int,args.input),x,y)

		while a.direction != [0,0]:
			a.action()
			a.move()
		print [x,y],':',

		if args.ASCII or args.ASCII_out:
			print "".join(map(chr,a.memory))
		else:
			print " ".join(map(str,a.memory))
