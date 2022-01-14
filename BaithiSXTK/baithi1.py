#Vũ Duy Khương 1451020130

# nhập vào tên của mình
khuong = input("Nhập vào tên của mình: ")

# xuất ra tên của mình
print("Tên của mình là: ", khuong)

# tính độ dài tên của mình

n = len(str(khuong))

print("Độ dài tên n = ", n)

# tạo 1 dictionary rỗng
dictionary = dict()

# dictionary có chứa (i, i*i)
for i in range(1, n + 1):
    dictionary[i] = i * i

# xuat ra màn hình
print("Dictionary độ dài của tên là: ", dictionary)