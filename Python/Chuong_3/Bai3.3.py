# For..else
# for i in range(1,4):
#     print('Lần lặp: ',i)
# else:
#     print('Vòng lặp kết thúc')
    
# for i in range(10,14):
#     print(f'Kiểm tra {i}...')
#     if i % 7 == 0:
#         print(f"Tìm thấy: {i} chia hết cho 7")
#         break
# else:
#     print("Không có số nào chia hết cho 7")

# Tính tổng 1! + 2! +...+ 10!
tong = 0
for i in range(1,11):
    giai_thua = 1
    for j in range(1, i+1):
        giai_thua += j
    tong += giai_thua
print("Tổng 1! + 2! + ... + 10!: ",tong)