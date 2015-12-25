#!usr/bin/env python

import json
import random
from run_tracker import RunData
from pyprocessing import *

run_data = RunData()
json_data = []
for spec in run_data.specs:
	for run_ in run_data.runs:
		if str(run_["day"]) == str(spec)[:-1]:
			run_["color"] = [random.randint(0,255) for x in range(3)]
			json_data.append(run_)

def setup():
	size(600,600)
	rectMode(CENTER)
	textAlign(CENTER)
	noStroke()

def draw():
	background(0)
	fill(255)
	textSize(20)
	longest = max(json_data, key = lambda x: x["Distance"])
	sections = width/int(longest["Distance"])
	tmp = 1
	for runs in json_data:
		sections = width/int(longest["Distance"])
		while tmp <= int(longest["Distance"]):
			try:
				fill(runs["color"][0],runs["color"][1],runs["color"][2])
				point = int(runs["Mile"+str(tmp)])
				rect(sections,(height/2)+point,5,5)
			except KeyError:
				pass
			sections += sections
			tmp += 1

	if len(json_data) == 1:
		text(json_data[0]["day"].replace("_","/"), width/2,30)
		

run()
