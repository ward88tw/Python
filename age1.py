driving = input('請問你有沒有開過車?')
age = input('請問你的年齡?')
age = int(age)

if driving == 'Yes':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('你怎麼會有開過車')
elif driving == 'No':
	if age >= 18:
		print('你可以考駕照了')
	else:
		print('你需要滿18才可以考駕照')
else:
	print('只能輸入Yes or No')