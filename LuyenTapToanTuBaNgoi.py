num_check = int(input("Nhập số cần kiểm tra chẵn hay lẻ:"))

# Dùng toán tử ba ngôi
loaiso = "Đây là Số chẵn (toán tử ba ngôi)" if num_check %2 == 0 else "Đây là Số lẻ (toán tử ba ngôi)"
print(loaiso)

# Dùng IF-ELSE
if(num_check%2  == 0):
    print("Đây là số chẵn (if-else)")
else:
    print ("Đây là số lẻ (if-esle)")