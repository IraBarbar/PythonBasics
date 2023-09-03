str_from_user = input('Введите : ')
if str_from_user.isdigit():
    print(bin(int(str_from_user)))
    print(oct(int(str_from_user)))
    print(hex(int(str_from_user)))
elif str_from_user.isascii():
    print('Текст написан на латинице')
else:
    print('Текст не написан на латинице и это не число')
