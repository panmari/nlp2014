
# FNV-1 hash method
def hash(input):
    FNV_prime_32 = 16777619
    offset_basis = 2166136261

    hash = offset_basis
    for char in input:
        hash *= FNV_prime_32
        hash %= (2**32)
        hash ^= ord(char)
    return hash