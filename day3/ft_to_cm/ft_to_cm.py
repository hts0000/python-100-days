x = float(input("请输入长度: "))
unit = input("请输入单位(ft, cm): ")

if unit == "ft":
    print(f"{x:.2f}ft = {x*2.54:.2f}cm")
elif unit == "cm":
    print(f"{x:.2f}cm = {x/2.54:.2f}ft")
else:
    print("只支持ft和cm作为单位.")
