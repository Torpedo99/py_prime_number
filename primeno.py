print("Welcome random tester, this program will print all the prime numbers from 2 to n");
n = int(input("Enter n\n"))
primes = [True for i in range(n+1)]
p = 2
while(p*p <= n):
    if(primes[p] == True):
        for i in range(p*2, n+1, p):
            primes[i] = False
    p += 1
for x in range(2, n):
    if(primes[x]):
        print(x)