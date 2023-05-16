import random

answer = random.randint(1,100)
count = 0
while True:
	num = input('請猜數字:')
	num = int(num)
	count = count + 1
	if num == answer:
		print('你好棒, 你猜對了, 你猜了', count, '次')
		print(answer)
		break
	elif num > answer and num <= 100:
		print('答案比較小喔')
	elif num < answer and num > 0:
		print('答案比較大喔')
	else:
		print('猜的數字請介於1~100之間')
	print('你總共猜了', count, '次')