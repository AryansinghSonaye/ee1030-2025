import ctypes
from ctypes import c_int, POINTER

lib = ctypes.CDLL("./libjordan.so")

lib.jordan_nonzeros.argtypes = [c_int, POINTER(c_int), c_int]
lib.jordan_nonzeros.restype  = c_int

lib.num_two_by_two_blocks.argtypes = [c_int, POINTER(c_int), c_int]
lib.num_two_by_two_blocks.restype  = c_int

lib.num_one_by_one_blocks.argtypes = [c_int, POINTER(c_int), c_int]
lib.num_one_by_one_blocks.restype  = c_int

gms = (c_int * 2)(3, 3)
n = 7

nonzeros = lib.jordan_nonzeros(n, gms, 2)
two_blocks = lib.num_two_by_two_blocks(n, gms, 2)
one_blocks = lib.num_one_by_one_blocks(n, gms, 2)

print(f"Matrix size n = {n}")
print(f"Geometric multiplicities = [3, 3]")
print(f"2x2 blocks = {two_blocks}")
print(f"1x1 blocks = {one_blocks}")
print(f"Total nonzero entries in Jordan form = {nonzeros}")


