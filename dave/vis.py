#usr/bin/env python

import json
import random
from pyprocessing import *

class Helper():
	def __init__(self,json):
		self.db = json	
		self.tempdb = json

	def search(self,card):
		for key in self.db.keys():
			for c in self.db[key]:
				#print c
				if c["name"] == card:
					return c 
		return None	

def loadJson():
	with open("cards.json") as json_file:
		return json.load(json_file)

def setup():
	rectMode(CENTER)
	textAlign(CENTER)
	size(600,600)

def draw():	
	#for key in helper.db.keys():
	#	print key
	#print helper.db[raw_input()]
	numCards = input("Number of cards to compare: (1-6) ")
	colors = [random.randint(0,255) for x in range(numCards*3)]
	sectionSize = 600/numCards+1
	x = 0
	y = 250
	background(0)
	color = 0
	while numCards != 0:
		card = helper.search(raw_input())
		fill(colors[color],colors[color+1],colors[color+2])
		rect(x+sectionSize/2-50,y,50,card["attack"]*20)
		text(str(card["attack"]),x+sectionSize/2-50,y-(card["attack"]*20)-10)
		fill(colors[color]-10,colors[color+1]-10,colors[color+2]-10)
		rect(x+sectionSize/2+50,y,50,card["cost"]*20)
		text(str(card["cost"]),x+sectionSize/2+50,y-(card["cost"]*20)-10)
		fill(colors[color]+10,colors[color+1]+10,colors[color+2]+10)
		name = card["name"]
		textSize(18)
		#fill(colors[color],colors[color+1],colors[color+2])
		text(name,x+sectionSize/2,350)
		x += sectionSize
		numCards -= 1
		color += 3

if __name__=="__main__":
	helper = Helper(loadJson())
	run()
