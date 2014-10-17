#!/usr/bin/python

def gcm(a, b):
	""" Returns greatest common divisor using Euclid's Algorithm """
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
	""" Returns lowest common multiple """
	return a * b // gcm(a, b)

def lcmm(*args):
	""" Returns lcm of args """
	return reduce(lcm, args)

def fibonacci():
	""" Calculates and yields the Fibonacci numbers one at a time """
	a, b = 0, 1
	yield 0
	while True:
		a, b = b, a + b
		yield a

def primes(n):
	""" Calculates and yields primes < n """
	sieve = [True] * n
	yield 2
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i]:
			yield i
			sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
	for i in xrange(i+2,n,2):
		if sieve[i]: yield i

def digit_sum(n):
	""" Sums the digits of n """
	return sum(int(c) for c in str(n))

def sum_numbers(n):
	""" Sums n numbers """
	return sum(i for i in range(n + 1))

def sum_square_of_numbers(n):
	""" Sums n numbers """
	return sum(i ** 2 for i in range(n + 1))

def factorial(n):
	""" Returns n! """
	if n == 0:
		return 1
	return n * factorial(n-1)

def reverse(num):
	rev = 0
	while num > 0 :
		rev = (10 * rev) + num % 10
		num //= 10
	return rev

def highest_palindrome(start, end = 1, step = -1):
	max = 0
	for i in range(start, end, step):
		for j in range(start, end, step):
			n = i * j
			if n == reverse(n) and n > max:
				max = n
	return max

if __name__ == "__main__":
	# Find the sum of all the multiples of 3 or 5 below 1000.
	print "Problem   1:", sum( [ i for i in range(1000) if i % 3 == 0 or i % 5 == 0 ] )

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

	# Find the largest palindrome made from the product of two 3-digit numbers.
	print "Problem   4:", highest_palindrome(999, 100)

	# What is the smallest positive number that is evenly divisible by all of
	# the numbers from 1 to 20?
	print "Problem   5:", lcmm(*range(1, 20))

	# Find the difference between the sum of the squares of the first one
	# hundred natural numbers and the square of the sum.
	print "Problem   6:", sum_numbers(100) ** 2 - sum_square_of_numbers(100)

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
