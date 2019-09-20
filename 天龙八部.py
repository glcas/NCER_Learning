import jieba


def cal(filename):
    f = open(filename, 'r', encoding='UTF-8')
    result = {}
    for line in f:
        for char in line:
            if char not in ' \n':
                result[char] = result.get(char, 0) + 1
    f.close()
    return result


def output(filename, sth):
    f = open(filename, 'w', encoding='UTF-8')
    ls = list(sth.items())
    ls.sort(key=lambda x: x[1], reverse=True)  # sort是方法，sorted是函数，都是默认参数
    i = 0
    newer = [[]]
    for word in ls:
        if i % 20 == 0 and i != 0: # 0%20==0
            newer.append([])
        newer[i // 20].append('{}:{}'.format(word[0], word[1]))
        i += 1
    for j in range(len(newer)):
        if j != len(newer) - 1:
            f.write(','.join(newer[j]) + '\n')
        else:
            f.write(','.join(newer[j]))
    f.close()


def newCal(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        string = f.read()
        wordCal = jieba.cut(string)
    res = {}
    for word in wordCal:
        if word not in '\n~·！@￥……*（）——+=}{【】|、：；“‘”’《，》。？/\t':
            res[word] = res.get(word, 0) + 1
    return res


calDict = cal('天龙八部-网络版.txt')
output('天龙八部-汉字统计.txt', calDict)
calWord = newCal('天龙八部-网络版.txt')
output('天龙八部-词语统计.txt', calWord)
