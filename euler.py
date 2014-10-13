#!/usr/bin/python

def fibonacci():
    a, b = 0, 1
    yield 0
    while True:
        a, b = b, a + b
        yield a

def primes(n):
	sieve = [True] * n
	yield 2
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i]:
			yield i
			sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
	for i in xrange(i+2,n,2):
		if sieve[i]: yield i

def digit_sum(n):
	i = 0
	for char in str(n):
		i += int(char)
	return i

def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n-1)

if __name__ == "__main__":
	# Find the sum of all the multiples of 3 or 5 below 1000.
	print "Problem   1:", sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])

	# By considering the terms in the Fibonacci sequence whose values do
	# not exceed four million, find the sum of the even-valued terms.
	generator = fibonacci()
	n = 0
	i = 0
	while i <= 4000000:
		i = next(generator)
		if i % 2 == 0:
			n += i

	print "Problem   2:", n

	# What is the largest prime factor of the number 600851475143?
	n = 600851475143
	i = 2
	while i * i < n:
		 while n % i == 0:
			 n = n / i
		 i += 1

	print "Problem   3:", n

	# What is the 10 001st prime number?
	generator = primes(1000000)
	i = 0
	n = 0
	while i <= 10001:
		i += 1
		n = next(generator)

	print "Problem   7:", n

	# What is the sum of the digits of the number 2 ** 1000?
	print "Problem  16:", digit_sum(2 ** 1000)

	# Find the sum of the digits in the number 100!
	print "Problem  20:", digit_sum(factorial(100))
