# DO_SOI = 100

# # gán nhiều biến
# x = y = z = 0
# print(x,y,z)
# a,b,c = 1,2,3
# print(a,b,c)

# # Hoán đổi 2 biến không cần biến tạm
# a,b = b,a
# print(a,b)

# Bài tập 1: Tìm 2 số khi biết tổng và hiệu
S = int(input("Nhập vào tổng (S): "))
D = int(input("Nhập vào hiệu (D): "))
a = (S+D)/2
b = (S-D)/2

print(f'Số thứ nhất: {a}')
print(f'Số thứ hai: {b}')

# Bài tập 2: Tìm 2 số khi biết tổng và tỉ số
S2 = int(input('Nhập vào tổng (S): '))
R = int(input('Nhập vào tỉ số (R): '))

b = S / (R+1)
a = b * R
print(f'Số a: {a}')
print(f'Số b: {b}')