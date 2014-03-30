
# According to recommendation on page, I implemented FNV-1a.
def FNV_hash(input):
    FNV_prime_32 = 16777619
    offset_basis = 2166136261

    hash = offset_basis
    for char in input:
        hash *= FNV_prime_32
        hash ^= ord(char)
    return hash

print(FNV_hash('abcdefg'))