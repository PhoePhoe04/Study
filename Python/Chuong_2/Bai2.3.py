# Biến và Các kiểu dữ liệu trong Python
# Fraction: phân số chính xác

from fractions import Fraction
a = 42
b = -7
c = 0

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Fraction
f = Fraction(0.25)
print(f)
print(type(f))

# Falsy values: 0, "", [], None
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(None))
# Truthy Values: 1, "abc"
print(bool(1321))
print(bool('abcsd'))

# Ép kiểu
my_numbers = 105.97522
so_nguyen = int(my_numbers)
print(so_nguyen)

lam_tron = round(my_numbers,2)
print(lam_tron)