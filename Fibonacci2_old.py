class Fibonacci(object):	
	def __init__(self, start, max):
		self.start = start
		self.max = max
		
	def fibonacci(self):
		if self.max == 0 or self.max == 1:
			return self.max
		else:
			return self.fibonacci(self.max - 1) + self.fibonacci(self.max - 2)
			
	def printfib(self):
		for i in range(self.start, self.max):
			print("Fibonacci of %d %d: " % (i, self.fibonacci(i)))
			
start = int(input("enter start: "))
max = int(input("Enter maximum: "))
myfib.fibonacci()
myfib = Fibonacci(start, max)
myfib.printfib(start, max)

#http://stackoverflow.com/questions/625083/python-init-and-self-what-do-they-do