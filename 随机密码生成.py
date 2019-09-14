import random

charList = list(map(chr, range(0x0041, 0x005a))) + list(
    map(chr, range(0x0061, 0x007a))) + list(map(chr, range(0x0030, 0x0039)))  # 大小写英文字母和数字的列表，map()后生成的是map对象
for i in range(10):
    password = ''
    for i in range(8):
        password += charList[random.randint(0, len(charList) - 1)]
    print(password)
    