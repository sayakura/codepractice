class A:
	x = "HAHA"
	def yell(self):
		print("WTFFFFFFFF!!")

class B(A):
	field = None
	def __init__(self, field):
		self.field = field
	def print_field(self):
		print(self.field)

a = A()
a.yell()
b = B(" = =")
b.yell()
b.print_field()
print(b.field)
print(b.x)