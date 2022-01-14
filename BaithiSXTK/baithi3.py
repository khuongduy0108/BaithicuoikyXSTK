#Vũ Duy Khương 1451020130

# gọi hàm thuận nghịch

def vuduykhuong(number):

    str1 = str(number);

    # ep kieu so n thanh chuoi
    str2 = str1[::-1];

    # dao nguoc chuoi str1
    if (str1 == str2):
        return ("là số thuận nghịch")
    else:
        return ("không là số thuận nghịch")


# nhập vào họ tên đệm và

vu = input("Mời nhập vào Họ của bạn: ")
duy = input("Mời nhập vào tên đệm của bạn: ")
khuong = input("Mời nhập vào Tên của bạn: ")

# hàm đếm chuỗi họ và tên

ho = str(len(vu))
dem = str(len(duy))
ten = str(len(khuong))
number = ho + dem + ten

# xuat  ra màn hình
print("Họ và tên:  ", vu + " " + duy + " " + khuong)
print('n = ',number, vuduykhuong(number))