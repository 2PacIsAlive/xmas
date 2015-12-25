#!usr/bin/env python

import glob
import math
import random
import thread
from pyprocessing import *

class Level():
	def __init__(self,lv):
		self.lv = lv
		self.difficulty = 1
	
	def setDifficulty(self,difficulty):
		self.difficulty = difficulty

class Game():
	def __init__(self):
		self.SCORE = 0
		self.difficulty = 1
		self.CURRENT_LEVEL = 0
		self.INTEGER_LEVEL = 2
		self.CURRENT_PROBLEM = None
		self.NEW_PROBLEM = True
		self.COLORS = 0
		self.WORD = None
		self.WORDS = []
		self.CURRENT_WORD = None
		self.CURRENT_WORDS = {}
		self.WORD_STARTED = False
		self.next_level_counter = 0
		self.game_over_counter = 0
		self.HIGHSCORE = None
		self.HIGHSCORE_NAME = None
		self.NEW_COLORS = True
		self.SOUNDS = []

	def loadSounds(self):
		for sound in glob.glob("sounds/*.mp3"):
			self.SOUNDS.append(sound)

	def loadHighscore(self):
		file_ = open("highscore.txt","r")
		self.HIGHSCORE = file_.readline()
		self.HIGHSCORE_NAME = file_.readline() 
		file_.close()

	def writeHighscore(self):
		file_ = open("highscore.txt","w")
		file_.write(str(self.SCORE))
		file_.write("\n")
		name = random.choice(self.WORDS)
		file_.write(name)
		file_.close()

	def loadWords(self):
		with open("words.txt","r") as file_:
			for word in file_:
				self.WORDS.append(word[:-2])
		file_.close()

	def runGame(self):
		if self.CURRENT_LEVEL == 0:
			self.COLORS = [random.randint(0,255) for x in range(3)]
			text_size = 46
			text = "WORD BLASTA"
			text_pos = (300,300)	
			global mouse
			if mouse == 255:
				self.CURRENT_LEVEL += 1
			
		else:
			text_size = 28
			self.level()
			#colors = [random.randint(0,255) for x in range(3)]
			text = ""
			text_pos = (300,500)

		return self.COLORS, text_size, text, text_pos

	def level(self):
		if self.NEW_COLORS == True:
			self.COLORS = [random.randint(0,255) for x in range(3)]
			self.NEW_COLORS = False

	def spawnWords(self,num):
		words_lv = [x for x in self.WORDS if len(x) < self.difficulty+1]
		for word in range(num):
			self.CURRENT_WORDS[random.choice(words_lv)] = (random.randint(0,600), random.randint(0,600), random.randint(0,1), random.randint(0,1))

	def removeWord(self,word):
		for word_ in self.CURRENT_WORDS.keys():
			if word == word_: 
				del self.CURRENT_WORDS[word_]

	def getFirstLetters(self):
		words = [(x[0],x) for x in self.CURRENT_WORDS.keys()]
		return words
		#return [(x[:1],x) for x in words]

	def getNextLetter(self,key):
		if len(self.CURRENT_WORD) == 1:
			letter = self.CURRENT_WORD
		else:
			letter = self.CURRENT_WORD[1]
		if key == letter:
			self.CURRENT_WORD = self.CURRENT_WORD[1:]
			return True
		else:
			return False

def mouseClicked():
	global mouse
	if mouse == 0:
		mouse = 255
	else: 
  		mouse = 0

def setup():
	size(600,600,fullscreen=True)
	rectMode(CENTER)
	textAlign(CENTER)

def draw():
	colors, text_size, texts, text_pos = game.runGame()
	background(0)
	fill(colors[0],colors[1],colors[2])
	textSize(text_size)
	#text(texts,text_pos[0],text_pos[1])
	text(texts,width/2,height/2)
	if random.randint(0,500-game.difficulty*2) == 1:
		game.spawnWords(game.difficulty)	
	if key.pressed:
		#randomSound = random.choice(game.SOUNDS)
		#thread.start_new_thread(playSound, (randomSound,))
		if game.WORD_STARTED == True:
			if game.getNextLetter(key.char) == True:
				if game.CURRENT_WORD == '':
					game.WORD_STARTED = False
					game.SCORE += 100*game.difficulty
					game.TIME += 50
					game.removeWord(game.WORD)
					if game.CURRENT_WORDS == {}:
						game.CURRENT_LEVEL = 2
						game.NEW_COLORS = True
		else:
			#print game.getFirstLetters()
			for letter, word in game.getFirstLetters():
				if letter == key.char: 
					game.CURRENT_WORD = word
					game.WORD = word
					game.WORD_STARTED = True
	if game.CURRENT_LEVEL == 1:
		game.TIME -= 1		
		if game.WORD_STARTED == True:
			textSize(100)
			text(game.CURRENT_WORD[1:],width/2,height/2)
			fill(colors[2],colors[1],colors[0])
			textSize(20)
			fill(colors[1],colors[0],colors[2])
			text(key.char,width/2,(height/2)+50)
		for word in game.CURRENT_WORDS.keys(): 
			x = game.CURRENT_WORDS[word][0] 
			y = game.CURRENT_WORDS[word][1]
			xdir = game.CURRENT_WORDS[word][2] 
			ydir = game.CURRENT_WORDS[word][3]
			if xdir == 0:
				if x < width-100:
					newx = x+1
				else:
					newx = x-1
					xdir = 1
			else:
				if x > 100:
					newx = x-1
				else: 
					newx = x+1
					xdir = 0
			if ydir == 0:
				if y < height-100:
					newy = y+1
				else:
					newy = y-1
					ydir = 1
			else:
				if y > 100:
					newy = y-1
				else: 
					newy = y+1
					ydir = 0
			colors = [random.randint(0,255) for x in range(3)]
			fill(colors[0],colors[1],colors[2])
			text(word,newx,newy)
			game.CURRENT_WORDS[word] = (newx, newy, xdir, ydir)	

	elif game.CURRENT_LEVEL == 2:
		background(colors[1],colors[2],colors[0])
		fill(255)
		textSize(50)
		text("NEXT LEVEL!",width/2,height/2)
		if game.next_level_counter > 100:
			game.spawnWords(game.difficulty)
			game.CURRENT_LEVEL = 1
			game.difficulty += 1
			game.next_level_counter = 0
		else:
			game.next_level_counter += 1

	elif game.CURRENT_LEVEL == 3:
		background(255)
		textSize(32)
		text("GAME OVER",width/2,(height/2)-50)
		#with open("highscore.txt","rw") as highscore:
		#	high = highscore.readline()
		#	name = highscore.readline()
		#	if game.SCORE > high:
		#		name = raw_input("Enter your name: ")
		#		high = game.SCORE
		#		highscore.write(game.SCORE)
		#		highscore.write(name)
		#	highscore.close() 
		#text("HIGHSCORE:"+high+" "+name,300,320)
		if game.SCORE > int(game.HIGHSCORE):
			fill(random.randint(0,255),random.randint(0,255),random.randint(0,255))
			text("NEW HIGHSCORE!", width/2, (height/2)+20)
			textSize(28)
			#text("enter your name in the console", width/2, height-200)
			game.writeHighscore()
		else:
			text(str(game.SCORE),width/2,(height/2)+20)
		if game.game_over_counter > 100:
			exit()
			game.CURRENT_LEVEL = 1
			game.difficulty = 0
			game.SCORE = 0
			game.game_over_counter = 0
		else:
			game.game_over_counter += 1
	textSize(24)
	fill(255)
	text(str(game.TIME),40,30)
	text(str(game.SCORE),width-60,30)
	text(str(game.difficulty),width/2,30)
	if game.TIME == 0:
		game.CURRENT_LEVEL = 3	

def playSound(sound):
	os.system("mpg321 --quiet "+sound)
	thread.exit()

def main():
	game.TIME = 1000
	game.loadSounds()
	game.loadHighscore()
	game.loadWords()
	game.spawnWords(3)
	run()

if __name__=="__main__":
	global mouse
	mouse = 0
	game = Game()
	main()
