#!usr/bin/env python

import json
from hearthstone_helper import HearthstoneHelper

def loadJson():
	with open("cards.json") as json_file:
		return json.load(json_file)

def run():
	print "\nOPTIONS:"
	for o in hearthstone_helper.options:
		print o
	option = raw_input()
	if option == "1":
		print
		card = hearthstone_helper.search(raw_input("What card would you like to search for? "))
		if card == None:
			print "Card not found. Make sure to use proper capitalization."
		else:
			for attribute in card.keys():
				print attribute+":",card[attribute]
	elif option == "2":
		print
		attribute = raw_input("What attribute would you like to search for? ")
		value = raw_input("Enter the value for '"+attribute+"' that you would like to find. ")
		cards = hearthstone_helper.attributeSearch(attribute,value)
		print
		if cards == []:
			print "Attribute not found. Make sure to use proper capitalization."
			verbose = raw_input("Would you like to print out all attributes? (y/n) ")
			if verbose == "y":
				for item in hearthstone_helper.attributes:
					print item
		else:
			print "Found "+str(len(cards))+" relevant card(s)."
			for card in cards:
				print card["name"]+":",attribute+":",card[attribute]
	elif option == "3":
		pass
	else:
		print "Unrecognized option."
	print
	if raw_input("Quit? (y/n) ") == "y":
		return
	else:
		return run()
		

if __name__=="__main__":
	hearthstone_helper = HearthstoneHelper(loadJson())
	run()
