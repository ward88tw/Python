i = 3

while i > 0:
	i = i - 1
	pwd = input('請輸入密碼:')
	if pwd == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼輸入錯誤')
		if i > 0:
			print('還有', i, '次機會')