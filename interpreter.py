from Stack import Stack
from random import randint

class Interpreter(object):
	def __init__(self,source,input,startx=None,starty=None):
		source = source.strip().split("\n")
		dim = max(map(len,source)+[len(source)])
		self.source = [list(x.ljust(dim,"."))for x in source]
		self.dim = (len(self.source),len(self.source[0]))
		self.direction = [[1,0],[0,1],[-1,0],[0,-1]][randint(0,3)]
		if (startx,starty) == (None,None):
			self.location = [randint(0,self.dim[0]-1),randint(0,self.dim[1]-1)]
		else:
			self.location = [startx,starty]
		self.memory = Stack(input)
		self.scope = Stack()
		self.read = False
		self.safety = False
	def wrapAround(self):
 		self.location[0] %= self.dim[0]
		self.location[1] %= self.dim[1]
	def move(self):
		self.location = [
			self.location[0]+self.direction[0],
			self.location[1]+self.direction[1]
		]
		#Important bit
		if self.location[0] < 0:
			self.wrapAround()
		if self.location[1] < 0:
			self.wrapAround()
		if self.location[0] >= self.dim[0]:
			self.wrapAround()
		if self.location[1] >= self.dim[1]:
			self.wrapAround()
	def character(self):
		return self.source[self.location[0]][self.location[1]]
	def action(self):
		if self.read:
			if self.character() == '"':
				self.read = False
			else:
				self.memory.append(ord(self.character()))
		elif self.character() == "/":
			self.direction = map(lambda x:-x,self.direction[::-1])
		elif self.character() == "\\":
			self.direction = self.direction[::-1]
		elif self.character() == "|":
			self.direction[1] *= -1
		elif self.character() == ">":
			self.direction = [0,1]
		elif self.character() == "<":
			self.direction = [0,-1]
		elif self.character() == "v":
			self.direction = [1,0]
		elif self.character() == "^":
			self.direction = [-1,0]
		elif self.character() == "%":
			self.safety = True
		elif self.character() == "#":
			self.safety = False
		elif self.character() == "@":
			if self.safety:
				self.direction = [0,0]
		elif self.character() == "[":
			if self.direction[1] == 1:
				self.direction[1] = -1
			if self.direction[1]:
				self.source[self.location[0]][self.location[1]] = "]"
		elif self.character() == "]":
			if self.direction[1] == -1:
				self.direction[1] = 1
			if self.direction[1]:
				self.source[self.location[0]][self.location[1]] = "["
		elif self.character() in "0123456879":
			self.memory.append(int(self.character()))
		elif self.character() == "+":
			self.memory.append(self.memory.pop()+self.memory.pop())
		elif self.character() == "*":
			self.memory.append(self.memory.pop()*self.memory.pop())
		elif self.character() == "-":
			self.memory.append(-self.memory.pop())
		elif self.character() == ":":
			self.memory.append(self.memory[-1])
		elif self.character() == "$":
			a,b=self.memory.pop(),self.memory.pop()
			self.memory.append(a)
			self.memory.append(b)
		elif self.character() == "!":
			self.move()
		elif self.character() == "?":
			if self.memory.pop():
				self.move()
		elif self.character() == "(":
			self.scope.append(self.memory.pop())
		elif self.character() == ")":
			self.memory.append(self.scope.pop())
		elif self.character() == '"':
			self.read = True
	def output(self,screen,a,b):
		try:
			import curses
			curselib = curses
		except ImportError:
			import unicurses
			curselib = unicurses

		for x in range(self.dim[0]):
			for y in range(self.dim[1]):
				try:
					if [x,y] == self.location:
						if curselib.has_colors():
							screen.addstr(a+x,b+y*2,"X",curselib.color_pair(1))
						else:
							screen.addstr(a+x,b+y*2,"X")
					else:
						screen.addstr(a+x,b+y*2,self.source[x][y])
				except:pass
