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
	high = 0
	for i in range(start, end, step):
		for j in range(start, end, step):
			n = i * j
			if n == reverse(n) and n > high:
				high = n
	return high

def find_adjacent_digits(num, length):
	i = 0
	high = 0
	num = str(num)
	while length <= len(num):
		prod = reduce(lambda x, y: int(x) * int(y), num[i:length])
		if prod > high:
			high = prod
		i += 1
		length += 1
	return high

def special_pythagorean_triplet(s):
	""" Calculates Pythagorean triplet using the sum of all sides """
	for a in xrange(1, s / 3):
		for b in xrange(a + 1, s - a):
			c = s - a - b;
			if a ** 2 + b ** 2 == c ** 2:
				return (a, b, c)

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

	# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
	num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
	print "Problem   8:", find_adjacent_digits(num, 13)

	# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	# Find the product abc.
	a, b, c = special_pythagorean_triplet(1000)
	print "Problem   9:", a * b * c 

	# Find the sum of all the primes below two million.
	n = 0
	for i in primes(2000000):
		n += i
	print "Problem  10:", n

	# What is the sum of the digits of the number 2 ** 1000?
	print "Problem  16:", digit_sum(2 ** 1000)

	# Find the sum of the digits in the number 100!
	print "Problem  20:", digit_sum(factorial(100))
