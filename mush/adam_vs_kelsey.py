#!usr/bin/env python

import random
from pyprocessing import *

DIFFICULTY = 5

class Game():
	def __init__(self):
		self.adam = loadImage("adam.jpg")
		self.kels = loadImage("kels.jpg")
		self.adamX = None
		self.adamY = None
		self.kelsX = None
		self.kelsY = None
		self.ballX = width/2
		self.ballY = height/2
		self.ballX_dir = None
		self.ballY_dir = None
		self.startup = True		
		self.adamScore = 0
		self.kelsScore = 0
		self.winner = None
		self.gameOver = False
		self.running = False

	def initLocations(self):
		self.adamX = 50
		self.adamY = height/2
		self.kelsX = width-50
		self.kelsY = height/2
	
	def startGame(self):
		self.ballX = width/2
		self.ballY = height/2
		self.ballX_dir = random.randint(0,1)
		self.ballY_dir = random.randint(0,1)
		self.running = True

def setup():
	imageMode(CENTER)
	rectMode(CENTER)
	textAlign(CENTER)
	size(fullscreen = True)
	game.initLocations()
	noStroke()

def draw():
	background(0)
	if game.startup == True:
		fill(random.randint(0,255),50,100)
		textSize(60)
		text("ADAM VS KELSEY!", width/2,height/2)
		fill(255)
		textSize(25)
		text("press any key to start", width/2,(height/2)+80)
		if key.pressed:
			game.startup = False
			game.startGame()

	elif game.running == True:
		fill(random.randint(0,255),50,100)
		rect(game.ballX,game.ballY,25,25)
		image(game.adam, game.adamX, game.adamY) 
		image(game.kels, game.kelsX, game.kelsY) 
		if key.pressed:
			if key.char == "w":
				if game.adamY > 110:
					game.adamY -= 10
			elif key.char == "s":
				if game.adamY < height-50:
					game.adamY += 10
			elif key.char == "i":
				if game.kelsY > 110:
					game.kelsY -= 10
			elif key.char == "k":
				if game.kelsY < height-50:
					game.kelsY += 10
		if game.ballX_dir == 0:
			if game.ballX < width-85:
				game.ballX += DIFFICULTY
			else:
				redir = False
				kelsLocs = [x+game.kelsY for x in range(60)] + [game.kelsY-x for x in range(60)]
				for loc in kelsLocs:
					if game.ballY == loc:
						redir = True
				if redir == True:
					game.ballX_dir = 1
					game.ballX -= DIFFICULTY
				else:
					game.adamScore += 1
					game.startGame()
		else:
			if game.ballX > 85:
				game.ballX -= DIFFICULTY
			else:
				redir = False
				adamLocs = [x+game.adamY for x in range(60)] + [game.adamY-x for x in range(60)]
				for loc in adamLocs:
					if game.ballY == loc:
						redir = True
				if redir == True:
					game.ballX_dir = 0
					game.ballX += DIFFICULTY
				else:
					game.kelsScore += 1
					game.startGame()
		if game.ballY_dir == 0:
			if game.ballY < height:
				game.ballY += DIFFICULTY
			else:
				game.ballY_dir = 1
				game.ballY -= DIFFICULTY
		else:
			if game.ballY > 65:
				game.ballY -= DIFFICULTY
			else:
				game.ballY_dir = 0
				game.ballY += DIFFICULTY
	
		fill(255)
		rect(0,30,width*2,65)
		rect(width/2,0,3,height*2)
		fill(255,50,100)
		textSize(60)
		text(str(game.adamScore),(width/4),60)
		fill(0,50,100)
		text(str(game.kelsScore),(width/4)*3,60)
		if game.adamScore == 5:
			game.gameOver = True
			game.winner = "Adam"
			game.running = False
		if game.kelsScore == 5:
			game.gameOver = True
			game.winner = "Kelsey"
			game.running = False

	elif game.gameOver == True:
		textSize(60)
		fill(random.randint(0,255),50,100)
		text(game.winner+" wins!",width/2,height/2)
		textSize(25)
		fill(255)
		text("press any key to play again",width/2,(height/2)+80)
		if key.pressed:
			game.gameOver = False
			game.adamScore = 0
			game.kelsScore = 0
			game.winner = None	
			game.initLocations()
			game.startGame()

def main():
	run()

if __name__=="__main__":
	game = Game()
	main()
