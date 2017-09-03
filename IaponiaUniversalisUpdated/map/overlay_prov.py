#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import codecs, sys, re, subprocess, scipy.misc
#usage: ./tagcheck.py <mod's 00_countries.txt> <vanilla's 00_countries.txt>

def main():
	provinces = codecs.open("definition.csv", encoding="utf-8").readlines()
	provinces = [x.strip().split(";") for x in provinces[1:]]

	provMap = scipy.misc.imread('provinces.bmp')
	colorMap = {}
	for line in range(1, len(provMap)-1):
		if line%50 == 0:
			print("line", line, "of", len(provMap))
		for col in range(1, len(provMap[0])-1):
			thisColor = (int(provMap[line][col][0]), int(provMap[line][col][1]),
			 int(provMap[line][col][2]))
			if thisColor in colorMap:
				colorMap[thisColor].append((line, col))
			else:
				colorMap[thisColor] = [(line, col)]


	subprocess.check_output(['convert', 'provinces.bmp', '-scale', '200%', 'newprov.png'])
	numbers = ['convert', 'newprov.png', '-font', 'FreeSans-Bold', '-pointsize','20']
	for prov in provinces:
		if (int(prov[1]), int(prov[2]), int(prov[3])) in colorMap.keys():
			thisColor = colorMap[(int(prov[1]), int(prov[2]), int(prov[3]))]
			y = sum([c[0] for c in thisColor])//len(thisColor) * 2
			x = abs(sum([c[1] for c in thisColor])//len(thisColor) *2 - 4)
			print(prov[0], provMap[y/2][x/2-2], (int(prov[1]), int(prov[2]), int(prov[3])))
			if len(thisColor) > 400:
				numbers += ['-pointsize', '16']
			else:
				numbers += ['-pointsize', '10']
			numbers += ['-draw', "fill white text "+str(x)+","+str(y)+" '"+prov[0]+"'"]
			numbers += ['-draw', "fill black text "+str(x+1)+","+str(y-1)+" '"+prov[0]+"'"]
			#print(int(prov[1]), int(prov[2]), int(prov[3]),
				#colorMap[(int(prov[1]), int(prov[2]), int(prov[3]))])

	subprocess.check_output(numbers + ['newprov.png'])
	#subprocess.check_output(['convert', 'provinces.bmp', '-font', 'FreeSans-Regular', '-pointsize', '12', '-draw', "fill black text 400,400 '1'", 'newprov.png'])
	#for color in colorMap:
		#print((sum([x[0] for x in colorMap[color]])//len(colorMap[color])),
		#sum([x[1] for x in colorMap[color]])//len(colorMap[color]))


	#print(colorMap)
	#scipy.misc.imsave('newprov.png', newMap)

def neighbors(x, y):
	return ((x-1, y),(x+1, y),(x,y-1),(x,y+1))
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
