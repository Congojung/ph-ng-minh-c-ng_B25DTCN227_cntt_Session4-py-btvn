print("--- HOA DON THANH TOAN RIKKEI STORE ---")

# Chuc nang 1: Nhap tong tien hoa don ban dau
bill_amount = int(input("Nhap tong tien hoa don ban dau (VND): "))

# Chuc nang 2: Tinh so tien giam gia
if bill_amount >= 500000:
    discount = bill_amount * 0.1   # Giam 10%
else:
    discount = 0                   # Khong giam gia

# Chuc nang 3: Tinh tong tien phai tra
final_amount = bill_amount - discount

# In ket qua
print("So tien duoc giam gia:", int(discount), "VND")
print("Tong tien khach phai tra:", int(final_amount), "VND")
