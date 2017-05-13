#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs, sys, re
#usage: ./tagcheck.py <mod's 00_countries> <vanilla 00_countries>

def main(myFile, vanillaFile):
	tagRegex = re.compile('[A-Z]{3}\s*=\s*"countries/.*\.txt"')
	mytags = codecs.open(myFile, encoding="utf-8").readlines()
	mytags = [x.strip() for x in mytags]
	myTagList = {}
	for x in mytags:
		matched = tagRegex.match(x)
		if matched:
			tagAndName = matched.group(0).split('=')
			myTagList[tagAndName[0].strip()] = tagAndName[1].strip()
	
	vanillatags = codecs.open(vanillaFile, encoding="utf-8").readlines()
	vanillatags = [x.strip() for x in vanillatags]
	vanillaTagList = {}
	for x in vanillatags:
		matched = tagRegex.match(x)
		if matched:
			tagAndName = matched.group(0).split('=')
			vanillaTagList[tagAndName[0].strip()] = tagAndName[1].strip()
	
	for x in myTagList.keys():
		try:
			if myTagList[x] != vanillaTagList[x]:
				print ("ERROR:", x, "is", myTagList[x], "in mod, but", vanillaTagList[x], "in vanilla")
		except KeyError:
			pass
	
		
if __name__ == "__main__":
	if len(sys.argv) == 3:
		main(sys.argv[1], sys.argv[2])
	else:
		print("Usage: ./tagcheck.py <mod's 00_countries.txt> <vanilla's 00_countries.txt>")
