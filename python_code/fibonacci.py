#double in python
def is_double(n = 0):
	while n < 10:
		if n % 2 == 0 : yield n
		n += 1
for n in is_double():
	print(n)


print("=======================")
#while loop fibonacci in python 
x, y = 0, 1
while(y < 20):
	print(y)
	x, y = y, x+y

print("=======================")
#use yield to make a fibonacci series
class Fibonacci():
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def series(self):
		while(True):
			yield(self.b)
			self.a , self.b = self.b, self.a + self.b

f = Fibonacci(0, 1)
for r in f.series():
	if r > 20: break
	print(r)