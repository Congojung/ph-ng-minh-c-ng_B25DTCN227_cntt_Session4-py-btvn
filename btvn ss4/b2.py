print("--- BAO CAO DOANH THU TUAN RIKKEI STORE ---")

# Chuc nang 1: Vong lap nhap doanh thu 7 ngay
total_revenue = 0        # tong doanh thu
target_days = 0          # so ngay dat muc tieu
days = 7                 # co dinh 7 ngay

for day in range(1, days + 1):
    revenue = int(input(f"Nhap doanh thu Ngay {day}: "))
    total_revenue += revenue   # cong don doanh thu
    
    # Kiem tra muc tieu >= 5,000,000
    if revenue >= 5000000:
        target_days += 1

# Chuc nang 2: Tinh doanh thu trung binh
average_revenue = total_revenue / days

# Chuc nang 3: In ket qua
print("\n--- BAO CAO DOANH THU TUAN RIKKEI STORE ---")
print("Tong doanh thu ca tuan:", total_revenue, "VND")
print("Doanh thu trung binh moi ngay:", int(average_revenue), "VND")
print("So ngay dat doanh thu muc tieu (>= 5,000,000 VND):", target_days, "ngay")
