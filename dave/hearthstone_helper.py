#usr/bin/env python

class HearthstoneHelper():
	def __init__(self,json):
		self.db = json	
		self.tempdb = json
		self.options = ["(1): Search for card by name", "(2): Search for all cards with a given attribute", "(3): Compare cards"]
		self.attributes = self.getAttributes()	

	def getAttributes(self):
		attributes = []
		for key in self.db.keys():
			for card in self.db[key]:
				for attribute in card.keys():
					if attribute not in attributes:
						attributes.append(attribute)
		return attributes	

	def search(self,card):
		for key in self.db.keys():
			for c in self.db[key]:
				#print c
				if c["name"] == card:
					return c 
		return None

	def attributeSearch(self,attribute,value):
		cards = []
		for key in self.db.keys():
			for card in self.db[key]:
				for attrib in card.keys():
					if attrib == attribute:
						if str(card[attrib]) == value:
							cards.append(card)
		return cards	


