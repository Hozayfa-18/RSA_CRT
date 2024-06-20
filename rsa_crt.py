import math

N = 14351
m = 52
e = 65537
s = 2435
s1 = 22
s2 = 62
rsa_crt = 2435
faulted_s2 = 63
faulted_crt_signature = 1419

# Calculate q from faulted RSA-CRT signature
h = (faulted_crt_signature - faulted_s2) % N
q = math.gcd(N, h)

# Calculate p
p = N // q

print("Found primes p and q:")
print("h =", h)
print("p =", p)
print("q =", q)



