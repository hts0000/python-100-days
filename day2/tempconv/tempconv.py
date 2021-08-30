celsius = 0.0
fahrenheit = 0.0

fahrenheit = float(input("fahrenheit = "))
celsius = (fahrenheit - 32) / 1.8

print("%.2f℉ = %.2f℃" % (fahrenheit, celsius))

#     f:这个f应该是代表format?
print(f"{fahrenheit:.1f}华氏度 = {celsius:.1f}摄氏度")
