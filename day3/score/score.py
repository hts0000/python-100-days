# 要求：
# 输入的成绩在90分以上（含90分）输出A；
# 80分-90分（不含90分）输出B；
# 70分-80分（不含80分）输出C；
# 60分-70分（不含70分）输出D；
# 60分以下输出E。

score = float(input("请输入你的成绩: "))
level = ""

if score >= 90:
    level = "A"
elif score >= 80:
    level = "B"
elif score >= 70:
    level = "C"
elif score >= 60:
    level = "D"
else:
    level = "E"

print(f"你的等级是: {level}")
print("你的等级是: %s" % level)
