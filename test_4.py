flat = 1
while flat:
    temperature = input("请输入温度：")
    temperature = float(temperature)
    unit = input("请输入单位：")
    if unit == "°F":
        T=(temperature-32)/1.8
        print("转为摄氏温度为：")
        print(T)
        flat=0
    elif unit =="°C":
        T=32+temperature*1.8
        print("转为华氏温度为：")
        print(T)
        flat=0
    else:
        print("输入有误，请重新输入")