#!/usr/bin/env python3
import gimpFormats
import sys
import re
from pathlib import Path

if len(sys.argv) != 3:
	print(f"Usage: {sys.argv[0]} image.xcf output_folder/")
	sys.exit(-1)

def make_safe_path(string):
	# Regex from https://stackoverflow.com/a/71199182
	return re.sub(r"[/\\?%*:|\"<>\x7F\x00-\x1F]", "-", string)

infile = sys.argv[1]

outfolder = Path(sys.argv[2])
outfolder.mkdir(parents=True, exist_ok=True)

g = gimpFormats.GimpDocument(infile)
for layer in g.layers:
	outfile = make_safe_path(layer.name) + ".png"
	print(f"Extracting {outfile}")
	layer.image.save(outfolder / outfile)