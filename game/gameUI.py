import pyxel

class Game:
	def __init__(self):
		pyxel.init(160, 120)
		self.x = 80
		self.y = 60
		pyxel.run(self.update, self.draw)

	def update(self):
		if pyxel.btn(pyxel.KEY_Q):
			pyxel.quit()
		if pyxel.btn(pyxel.KEY_LEFT):
			self.x -= 1
		if pyxel.btn(pyxel.KEY_RIGHT):
			self.x += 1
		if pyxel.btn(pyxel.KEY_UP):
			self.y -= 1
		if pyxel.btn(pyxel.KEY_DOWN):
			self.y += 1

	def draw(self):
		pyxel.cls(0)
		pyxel.circ(self.x, self.y, 5, 7)

if __name__ == "__main__":
    Game()
