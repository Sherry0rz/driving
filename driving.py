country = input('國家：')
age = input('年齡：')
age = int(age)

if country == '台灣' or country == '臺灣' or country == 'Taiwan':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不可以考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不可以考駕照')
else:
	print('你只能輸入 台灣/美國')