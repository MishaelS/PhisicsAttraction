import math

# -------------------------------------------------------------------------------

class Vector2:
	def __init__(self, x=0, y=0, arr=None):
		if arr == None:
			self.x = x
			self.y = y
		elif arr != None:
			self.x = arr[0]
			self.y = arr[1]

	def Tget(self):
		return self.x, self.y

	def Xget(self):
		return self.x

	def Yget(self):
		return self.y


	def Vset(self, vec):
		self.x = vec.x
		self.y = vec.y

	def Tset(self, arr):
		self.x = arr[0]
		self.y = arr[1]

	def set(self, x, y):
		self.x = x
		self.y = y


	def Vadd(self, vec):
		self.x += vec.x
		self.y += vec.y

	def Tadd(self, arr):
		self.x += arr[0]
		self.y += arr[1]

	def add(self, n):
		self.x += n
		self.y += n


	def Vsub(self, vec):
		self.x -= vec.x
		self.y -= vec.y

	def Tadd(self, arr):
		self.x -= arr[0]
		self.y -= arr[1]

	def sub(self, n):
		self.x -= n
		self.y -= n


	def Vmult(self, vec):
		self.x *= vec.x
		self.y *= vec.y

	def Tadd(self, arr):
		self.x *= arr[0]
		self.y *= arr[1]

	def mult(self, n):
		self.x *= n
		self.y *= n


	def Vdiv(self, vec):
		self.x /= vec.x
		self.y /= vec.y

	def Tadd(self, arr):
		self.x /= arr[0]
		self.y /= arr[1]

	def div(self, n):
		self.x /= n
		self.y /= n


	def mag(self):
		return math.sqrt( self.x**2 + self.y**2 )

	def magSq(self):
		return (self.x**2 + self.y**2)

	def normalize(self):
		m = self.mag()
		if (m != 0 and m != 1):
			self.div(m)

	def limit(self, m):
		if (self.magSq() > m**2):
			self.normalize()
			self.mult(m)
