chitieu = int(input("Người dùng đã chi bao nhiêu tiền tại cửa hàng:"))
sotiengiam = 0
if chitieu < 75:
    sotiengiam = 0
elif chitieu < 99:
    sotiengiam = 15
elif chitieu <150:
    sotiengiam = 25
elif chitieu >=150:
    sotiengiam = 50

print ("Tổng số tiền phải thanh toán là:",chitieu-sotiengiam)