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

if __name__ == "__main__":
	print "Problem   1:", sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])

	generator = fibonacci()
	n = 0
	i = 0
	while i <= 4000000:
		i = next(generator)
		if i % 2 == 0:
			n += i

	print "Problem   2:", n

	n = 600851475143
	i = 2
	while i * i < n:
		 while n % i == 0:
			 n = n / i
		 i += 1

	print "Problem   3:", n

	generator = primes(1000000)
	i = 0
	n = 0
	while i <= 10001:
		i += 1
		n = next(generator)

	print "Problem   7:", n

	i = str(2 ** 1000)
	n = 0
	for char in i:
		n += int(char)
	
	print "Problem  16:", n
