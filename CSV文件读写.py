def myCSVWriter(dataList, filename):
    file = open(filename, 'w')
    writeList = []
    for line in range(len(dataList)):
        writeList.append([])
        for item in dataList[line]:
            if (isinstance(item, str) and (',' in item or '\n' in item)) or (
                    isinstance(item, (list, set, dict, tuple))
                    and len(item) > 1):  # 连接的两个语句从左到右执行
                if '"' in item:
                    item = item.replace('"', '""')
                writeList[line].append(
                    "\"" + str(item) + "\""
                )  # Microsoft Excel的规则：当csv被表格化时，双引号括起来的解析为一个元素，双引号被扔掉;在元素被双引号括起来的情况下，若元素中本来就有双引号，应使每个双引号用两个代替
            else:
                writeList[line].append(str(item))
    for row in range(len(writeList)):
        if row != len(writeList) - 1:
            file.write(','.join(writeList[row]) +
                       '\n')  # 一行数据列表的一般写入形式：先把每个元素转换成str，再用,join，使行末可以没有逗号
        else:
            file.write(','.join(writeList[row]))
    file.close()


def myCSVReader(CSVFilename):
    """ transform csv string to list """
    readF = open(CSVFilename, 'r')
    string = readF.read()
    quatationCon = -1
    readyQuatationCon = False
    commaPos = -1
    line = 0
    readList = [[]]
    for i in range(len(string)):
        if string[i] == '"':
            if i == 0 or (quatationCon == -1 and string[i - 1] in ',\n'):
                if i == len(string) - 1:
                    readList[line].append('"')
                else:
                    quatationCon = i
                    commaPos = -1
            elif quatationCon >= 0:
                if readyQuatationCon is True:
                    readyQuatationCon = False
                elif i == len(string) - 1 or string[i + 1] in ',\n':
                    readList[line].append(string[quatationCon + 1:i].replace(
                        '""', '"'))
                    quatationCon = -1
                elif string[i + 1] == '"':
                    readyQuatationCon = True
        elif string[i] == ',' and quatationCon == -1:
            if commaPos == -1:
                if i == len(string) - 1:
                    readList[line].append([])
                else:
                    commaPos = i
            elif commaPos != -1:
                readList[line].append(string[commaPos + 1:i])
                commaPos = i
                if i == len(string) - 1:
                    readList[line].append([])
        elif string[i] == '\n' and quatationCon == -1:
            if commaPos != -1 and string[i - 1] != '\n':
                readList[line].append(string[commaPos + 1:i])
            commaPos = i
            readList.append([])
            line += 1
        elif i == len(string) - 1:
            if quatationCon == -1:
                readList[line].append(string[commaPos + 1:])
            else:  # quatation not close, from quatation's position read again by the rule of comma
                tempList = string[quatationCon:].split('\n')
                for j in range(len(tempList)):
                    if not (j == len(tempList) - 1 and tempList[j] == ''):
                        readList[line] += tempList[j].split(',')
                    if j != len(tempList) - 1:
                        readList.append([])
                        line += 1
    for i in range(len(readList)):
        for j in range(len(readList[i])):
            try:
                readList[i][j] = eval(readList[i][j])
            except:
                continue
    readF.close()
    return readList


def main():
    testList = [[(5, 6), 1, 2.2, 1 + 2j, True, [1, 2, 3], {1, 2, 3}, (4, 5, 6),
                 {
                     'q': 4,
                     'e': 0
                 }, 'a\ns\td\t/f', '"a\"sd\nfs\tf,re""ter', '"",', '""""uu,',
                 '"","'], [], [1, 2, 3, '"""c']]
    filename = 'test.csv'
    myCSVWriter(testList, filename)
    readList = myCSVReader(filename)
    print(readList)


if __name__ == "__main__":
    main()
