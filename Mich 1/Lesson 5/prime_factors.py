# class demo for making primes
# p is prime if Fp={1,p}
# f divides p if p MOD f != 0
MAXV = 201
primes = []

for n in range(2,MAXV+1):
    divides = False
    for primeFactor in primes:
        if primeFactor < n and n % primeFactor == 0:
            divides = True
            break
        if primeFactor > n:
            break
            
    if not divides:
        primes.append(n)
        
for p in primes:
    print(p)