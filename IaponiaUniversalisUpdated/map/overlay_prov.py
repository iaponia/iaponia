#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import codecs, sys, re, subprocess, scipy.misc
#usage: ./tagcheck.py <mod's 00_countries.txt> <vanilla's 00_countries.txt>

def main():
	provinces = codecs.open("definition.csv", encoding="latin_1").readlines()
	provinces = [x.strip().split(";") for x in provinces[1:]]

	subprocess.check_output(['convert', 'provinces.bmp', 'provinces-numbered.png'])
	provMap = scipy.misc.imread('provinces-numbered.png')
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

	subprocess.check_output(['convert', 'provinces-numbered.png', '-scale', '200%', 'provinces-numbered.png'])
	numbers = ['convert', 'provinces-numbered.png', '-font', 'FreeSans-Bold', '-pointsize','20']
	for prov in provinces:
		if (int(prov[1]), int(prov[2]), int(prov[3])) in colorMap.keys():
			thisColor = colorMap[(int(prov[1]), int(prov[2]), int(prov[3]))]
			y = sum([c[0] for c in thisColor])//len(thisColor) * 2
			x = abs(sum([c[1] for c in thisColor])//len(thisColor) *2)
			colorOnCenter = provMap[y/2][x/2]
			if (colorOnCenter[0], colorOnCenter[1], colorOnCenter[2]) != (int(prov[1]), int(prov[2]), int(prov[3])):
				y, x = sorted(thisColor, key=lambda point: distance((point[0]*2, point[1]*2), (y, x)))[0]
				y, x = y*2, x*2
			if len(thisColor) > 400:
				numbers += ['-pointsize', '16']
			else:
				numbers += ['-pointsize', '10']
			numbers += ['-draw', "fill white text "+str(x-4)+","+str(y+4)+" '"+prov[0]+"'"]
			numbers += ['-draw', "fill black text "+str(x-3)+","+str(y+3)+" '"+prov[0]+"'"]

	subprocess.check_output(numbers + ['provinces-numbered.png'])


def distance(x, y):
	return((x[0]-y[0])**2 + (x[1]-y[1])**2)
	#no need to take the square root

def neighbors(x, y):
	return ((x-1, y),(x+1, y),(x,y-1),(x,y+1))

if __name__ == "__main__":
	main()
