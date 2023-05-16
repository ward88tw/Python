hight = input('請輸入身高(cm): ')
weight = input('請輸入體重(kg): ')

hight_m = float(hight) / 100
bmi = float(weight) / (hight_m * hight_m)

print('你的BMI為:', bmi)

if bmi < 18.5:
    print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('標準體重')
else:
    print('異常範圍')