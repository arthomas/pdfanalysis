#!/usr/bin/python3
import pdf2image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--format", help="Image format, either JPEG or PNG")
parser.add_argument("-i", "--input", help="PDF to image")
parser.add_argument("-o", "--output", help="Output file name")
args = parser.parse_args()
fmt = args.format or "jpeg"
print(f"Creating image of {args.input}...")
ext = ".jpg"
if fmt != "jpeg":
	ext = ".png"

images = pdf2image.convert_from_path(args.input)
i = 0
for image in images:
	i += 1
	image.save(f"{args.output}-page{i}{ext}",fmt)

