#!usr/bin/env python

import os
import time
import json
import glob
import math

class RunData():
	def __init__(self):
		self.runs = self.loadRuns()
		self.options = ["(1): Save run", "(2): View previous run", "(3): Compare runs"]
		self.specs = self.loadSpecs()
	
	def loadRuns(self):
		runs = []
		for run in glob.glob("runs/*.run"):
			with open(run, "r") as infile:
				runs.append(json.load(infile))
			infile.close()	
		return runs

	def loadSpecs(self):
		runs = []
		try:	
			with open("runs/.specs.runs", "r") as specs:
				for run in specs:
					runs.append(run)
			specs.close()
		except IOError:
			pass
		return runs 

	def saveRun(self):
		run = {}
		if raw_input("Was this run today? (y/n) ") == "y":
			run["Day"] = time.strftime("%m_%d_%Y")
		else:
			day = raw_input("Enter month: ")
			month = raw_input("Enter day: ")
			year = raw_input("Enter year: ")
			run["Day"] = day+"_"+month+"_"+year
		run["Time"] = raw_input("How long was your run in minutes? ")
		run["Distance"] = raw_input("How many miles was your run? ")
		miles = math.ceil(float(run["Distance"]))
		counter = 1
		while counter <= miles:
			run["Mile"+str(int(counter))] = raw_input("What was your rate for mile "+str(int(counter))+"? (how many minutes did this mile take) ")
			counter += 1
		outfile = open("runs/"+run["Day"]+".run", "w") 
		json.dump(run, outfile)			 
		outfile.close()
		print "Run saved.\n"

	def viewRun(self):
		self.runs = self.loadRuns()
		counter = 0
		for run in self.runs:
			print "("+str(counter)+"):", run["Day"]+":", str(run["Distance"])+" miles,", str(run["Time"])+" minutes"
			counter += 1
		print
		run = raw_input("Which run do you want to view? (Enter the corresponding number): ")
		specs = open("runs/.specs.runs", "w")
		specs.truncate()
		specs.write(self.runs[int(run)]["Day"])
		specs.close()
		#os.system("python view_run.py")	
		print	
		for key in self.runs[int(run)].keys():
			print key+":", self.runs[int(run)][key]
		print

	def compareRuns(self):
		self.runs = self.loadRuns()
		counter = 0
		for run in self.runs:
			print "("+str(counter)+"):", run["Day"]+":", str(run["Distance"])+" miles,", str(run["Time"])+" minutes"
			counter += 1
		print
		comparisons = raw_input("Which runs do you want to compare? (Enter the corresponding numbers, separated by spaces): ")
		print
		runs = []
		for letter in comparisons:
			if letter != " ":
				runs.append(self.runs[int(letter)])
		specs = open("runs/.specs.runs", "w")
		specs.truncate()
		for run in runs:
			specs.write(run["Day"])
			specs.write("\n")
		specs.close()
		#os.system("python view_run.py")
		for run in runs:
			run["Average"] = float(run["Time"]) / float(run["Distance"])
		longest = max(runs, key = lambda x: x["Distance"])
		best_pace = max(runs, key = lambda x: x["Average"])
		print "Your longest run was", longest["Distance"], "miles on", longest["Day"]
		print "Your fastest average pace was", best_pace["Average"], "mins/mile on", best_pace["Day"]
		fastest_mile_val = 0.0
		fastest_mile = None
		for i in range(int(longest["Distance"])):
			try:
				for run in runs:
					if float(run["Mile"+str(i)]) > fastest_mile_val:
						fastest_mile = (run, "Mile"+str(i))
			except KeyError:
				pass
		print "Your fastest mile was", fastest_mile[0][fastest_mile[1]], "minutes on", fastest_mile[0]["Day"]				 
		print		

def UI():
	print "Options:"
	for option in run_data.options:
		print option
	choice = raw_input("What would you like to do? (Enter the corresponding number): ")
	print
	if choice == "1":
		run_data.saveRun()
	elif choice == "2":
		run_data.viewRun()
	elif choice == "3":
		run_data.compareRuns()
	else:
		print "Unrecognized option."
	if raw_input("Quit? (y/n) ") == "y":
		return
	else:
		return UI()

def main():
	UI()

if __name__=="__main__":
	run_data = RunData()
	main()
	print "\nNice job Mike! Keep up the good work!"
