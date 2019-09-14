string = input('input here:')
counts = {}
for char in string:
    if (ord(char) >= 0x0061
            and ord(char) <= 0x007a) or (ord(char) >= 0x0041
                                         and ord(char) <= 0x005a):
        counts[char] = counts.get(
            char, 0) + 1  # 字典的索引格式:可修改可添加；字典的get方法：参数1为要找的key，若不存在，返回参数2
countList = list(counts.items()
                 )  # dict.items()返回dict_items类，类似list，将key-value转换为(key,value)
countList.sort(
    key=lambda x: x[1], reverse=True)  # list.sort()的参数都是可选参数，reverse=True代表降序
for info in countList:
    print('{}{:>5}'.format(info[0], info[1]))  # 冒号前为索引，其后为格式控制
