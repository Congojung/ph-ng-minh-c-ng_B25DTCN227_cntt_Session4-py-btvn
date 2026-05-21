# Nhap so luong hoa don
n = int(input(" Nhap so luong hoa don trong ca: "))
# Nhap hoa don dau tien 
hoa_don = float(input("Nhap gia tri hoa don thu 1:"))
# Gan max va min ban dau 
max_hd = hoa_don
min_hd = hoa_don
# Nhap cac hoa don con lai
for i in range(2, n+1):
    hoa_don=float(input(f"Nhap gia tri hoa don thu {i}:"))
    if hoa_don>max_hd:
        max_hd=hoa_don
    if hoa_don<min_hd:
        min_hd=hoa_don
# Hien thi ket qua 
print("\n Ket qua cuoi ca")
print("Hoa don co gia tri cao nhat:", max_hd, "VND")
print("Hoa don co gia tri thap nhat:", min_hd,"VND")    
