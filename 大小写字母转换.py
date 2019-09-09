def main():
    with open('E:/成都/Codes/python\\temp.py', 'rt', encoding='UTF-8') as f:
        txtList = list(f.read())
        for i in range(len(txtList)):  # 字符串是不可变对象；迭代元素（此处为i）在该轮迭代开始时在内存中创建，该轮迭代结束后清除
            if ord(txtList[i]) in range(0x0041, 0x005a):
                txtList[i] = chr(ord(txtList[i]) + (0x0061 - 0x0041))
            elif ord(txtList[i]) in range(0x0061, 0x007a):
                txtList[i] = chr(ord(txtList[i]) - (0x0061 - 0x0041))
    newTxt = ''.join(txtList)  # list -> str 基操
    print(newTxt)


if __name__ == "__main__":
    main()
