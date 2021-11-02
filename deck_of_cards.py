# Deck of Cards

import turtle
import time
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(800, 600)
wn.title("Deck of Cards")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Create classes
class Card():
	symbols = {"S":"♠", "C":"♣", "H":"♥", "D":"♦"}
	
	def __init__(self, name, suit):
		self.name = name
		self.suit = suit
	
	def print_card(self):		
		print(f"{self.name}{self.symbols[self.suit]}")

	def render(self, x, y, pen):
		
		# Draw border
		pen.penup()
		pen.goto(x, y)
		pen.color("blue")
		if self.suit == "H" or self.suit == "D":
			pen.color("red")
		if self.suit == "":
			pen.color("grey")
		pen.goto(x-50, y+75)
		pen.begin_fill()
		pen.pendown()
		pen.goto(x+50, y+75)
		pen.goto(x+50, y-75)
		pen.goto(x-50, y-75)
		pen.goto(x-50, y+75)
		pen.end_fill()	
		pen.penup()

		if self.name != "":
			# Draw suit in the middle
			pen.color("white")		
			pen.goto(x-17, y-35)
			pen.write(self.symbols[self.suit], True, font=("Courier New", 48))
			
			# Draw top left
			pen.goto(x-40, y+44)
			pen.write(self.name, True, font=("Courier New", 18))
			pen.goto(x-40, y+25)
			pen.write(self.symbols[self.suit], True, font=("Courier New", 18))
			
			# Draw bottom right
			pen.goto(x+30, y-55)
			pen.write(self.name, True, font=("Courier New", 18))
			pen.goto(x+30, y-74)
			pen.write(self.symbols[self.suit], True, font=("Courier New", 18))
			pen.end_fill()	


class Deck():
	names = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
	suits = ("D", "C", "H", "S")
	
	def __init__(self):
		self.cards = []
		for name in self.names:
			for suit in self.suits:
				self.cards.append(Card(name, suit))
		
				
	def shuffle(self):
		random.shuffle(self.cards)

	def get_card(self):
		card = self.cards.pop()
		return card
		
	def reset(self):
		self.cards = []
		for name in self.names:
			for suit in self.suits:
				self.cards.append(Card(name, suit))
		
		self.shuffle()

# Create deck
deck = Deck()

# Shuffle deck
deck.reset()

# Render 5 empty cards
start_x = -250
for i in range(5):
	card = Card("","")
	card.render(start_x + 125 * i, 0, pen)

time.sleep(1)

# Render 5 cards in  a row
for i in range(5):
	card = deck.get_card()
	card.render(start_x + 125 * i, 0, pen)
	card.print_card()




wn.mainloop()
