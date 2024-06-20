# import math

# N = 14351
# m = 52
# e = 65537
# s = 2435
# s1 = 22
# s2 = 62
# rsa_crt = 2435
# faulted_s2 = 63
# faulted_crt_signature = 1419

# # Calculate q from faulted RSA-CRT signature
# h = (faulted_crt_signature - faulted_s2) % N
# q = math.gcd(N, h)

# # Calculate p
# p = N // q

# print("Found primes p and q:")
# print("h =", h)
# print("p =", p)
# print("q =", q)

values = {
    'V': 86,
    'Y': 89,
    'U': 85,
    'L': 76
}

# Convert the dictionary to a list for indexed access
values_list = list(values.values())

# Start of the loop
cx = 0

while cx < 4:
    bl = values_list[cx] # 89
    bl = bl - 65 # 24
    bl = (bl + 20) % 26 # 44 % 26 = 18
    bl = bl + 65 # 83
    values_list[cx] = bl #83
    cx += 1 # 2

# Convert the list back to the dictionary
for i, key in enumerate(values.keys()):
    values[key] = values_list[i]

# Get the resulting characters from the new ASCII values
decrypted_message = ''.join(chr(values[key]) for key in values)

print(decrypted_message)
