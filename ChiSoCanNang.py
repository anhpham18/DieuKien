
can_nang = float(input("Nhập cân nặng (tính bằng kg): "))
chieu_cao = float(input("Nhập chiều cao (tính bằng m): "))

BMI = can_nang / (chieu_cao * chieu_cao)

if BMI > 40:
    print ('Béo phì cấp độ III')
elif 35 <= BMI < 40:
    print ('Béo phì cấp độ II')
elif 30 <= BMI < 35:
    print ('Béo phì cấp độ I')
elif 25 <= BMI < 30:
    print ('Thừa cân')
elif 18.5 <= BMI < 25:
    print ('Bình thường')
elif 17 <= BMI < 18.5:
    print ('Gầy cấp độ I')
elif 16 <= BMI < 17:
    print ('Gầy cấp độ II')
elif BMI < 16:
    print ('Gầy cấp độ III')