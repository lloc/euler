#!/usr/bin/python

def fibonacci():
    a, b = 0, 1
    yield 0
    while True:
        a, b = b, a + b
        yield a

if __name__ == "__main__":
	print "Problem 1: ", sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])

	generator = fibonacci()
	n = 0
	while i <= 4000000:
		i = next(generator)
		if i % 2 == 0:
			n += i

	print "Problem 2: ", n

	n = 600851475143
	i = 2
	while i * i < n:
		 while n % i == 0:
			 n = n / i
		 i = i + 1

	print "Problem 3: ", n
