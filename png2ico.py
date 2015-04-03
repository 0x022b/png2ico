#!/usr/bin/python3
import os, subprocess, sys, tempfile
from argparse import ArgumentParser

def main():
	description = "Creates a multisize Microsoft Windows icon file"
	parser = ArgumentParser(description=description)
	parser.add_argument("--convert", action="store", type=str, metavar="PATH",
		default="/usr/bin/convert",
		help="path to convert (default: %(default)s)")
	parser.add_argument("--filter", action="store", type=str, metavar="FILTER",
		default="Lanczos2",
		help="filter used by convert (default: %(default)s)")
	parser.add_argument("input", action="store", type=str, metavar="INPUT",
		help="source file")
	parser.add_argument("output", action="store", type=str, metavar="OUTPUT",
		help="target file")
	args = parser.parse_args()

	outputs = []
	base = os.path.splitext(os.path.basename(args.input))[0]
	for size in [16, 32, 64, 128, 256]:
		output = os.path.join(
			tempfile.gettempdir(),
			"{0}-{1}x{1}.png".format(base, size)
		)
		outputs.append(output)
		subprocess.call([
			args.convert, "-quiet", args.input, "-colorspace", "RGB",
			"-filter", args.filter, "-resize", "{0}x".format(size),
			"-colorspace", "sRGB", output
		])

	subprocess.call([args.convert] + outputs + [args.output])

	for output in outputs:
		if os.path.exists(output):
			os.remove(output)

if __name__ == "__main__":
	try:
		sys.exit(main())
	except KeyboardInterrupt:
		sys.exit(1)
