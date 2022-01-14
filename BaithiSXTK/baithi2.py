#Vũ Duy Khương 1451020130

#nhập vào tên của mình và đếm

duykhuong=len(input("Mời nhập tên đệm và tên của bạn: "))

#xuat ra man hinh
print("Độ dài tên của mình là: ", duykhuong)

#tính tổng các chữ số

tong = 0
for i in range(len(str(duykhuong))):
    chu=duykhuong%10
    tong = tong + chu
    duykhuong= duykhuong//10

#in ra màn hình
print("tổng các chữ số của n là: ", tong)