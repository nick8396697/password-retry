password = input('請設定你的密碼: ')
x = 3
while True:
	key = input('請輸入你的密碼')
	if key == password:
		print('登入成功!')
		break
	else:
		x = x - 1
		if x > 0:
		    print('密碼錯誤! 還有', x, '次機會')
		else:
			print('很抱歉你已經沒機會了，密碼已鎖定!')
			break
			

