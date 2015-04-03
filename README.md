# [png2ico][1]

png2ico is a [Python][2] script that automates the creation of multisize
Microsoft Windows icon files.

## Prerequisites

* [ImageMagick][3]

## Usage

	usage: png2ico.py [-h] [--convert PATH] [--filter FILTER] INPUT OUTPUT

	Creates a multisize Microsoft Windows icon file

	positional arguments:
	  INPUT            source file
	  OUTPUT           target file

	optional arguments:
	  -h, --help       show this help message and exit
	  --convert PATH   path to convert (default: /usr/bin/convert)
	  --filter FILTER  filter used by convert (default: Lanczos2)

[1]: https://bitbucket.org/scoobadog/png2ico "png2ico"
[2]: https://www.python.org/ "Python.org"
[3]: http://www.imagemagick.org/ "ImageMagick"
