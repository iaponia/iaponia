#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import codecs, sys, re, subprocess
#usage: ./tagcheck.py <mod's 00_countries.txt> <vanilla's 00_countries.txt>

def main():
	provinces = codecs.open("definition.csv", encoding="utf-8").readlines()
	provinces = [x.strip().split(";") for x in provinces[1:]]
	for x in provinces:
		print(x)
	bmp = subprocess.check_output(['convert', 'provinces.bmp', '-define', 'histogram:unique-colors=true', '-format', '%c', 'histogram:info:-'])
	colorRegex = re.compile('#[0-9a-zA-Z]{6}')
	bmp = [x.strip() for x in bmp.decode("utf-8").split("\n")]

	for x in bmp:
		matched = colorRegex.match(x)
		if matched:
			print(matched.group(0))

	# vanillatags = codecs.open(vanillaFile, encoding="utf-8").readlines()
	# vanillatags = [x.strip() for x in vanillatags]
	# vanillaTagList = {}
	# for x in vanillatags:
	# 	matched = tagRegex.match(x)
	# 	if matched:
	# 		tagAndName = matched.group(0).split('=')
	# 		vanillaTagList[tagAndName[0].strip()] = tagAndName[1].strip()
	#
	# for x in myTagList.keys():
	# 	try:
	# 		if myTagList[x] != vanillaTagList[x]:
	# 			print "ERROR:", x, "is", myTagList[x], "in mod, but", vanillaTagList[x], "in vanilla"
	# 	except KeyError:
	# 		pass


if __name__ == "__main__":
	main()
