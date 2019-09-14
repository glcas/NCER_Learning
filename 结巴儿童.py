import jieba
from wordcloud import WordCloud
file = open('千字文.txt', 'r', encoding='UTF-8')
txt = file.read()
cutter = jieba.cut(txt)  # 生成器只能遍历一次
counts = {}
for word in cutter:
    if len(word) > 1:
        counts[word] = counts.get(word, 0) + 1
countList = list(counts.items())
countList.sort(key=lambda x: x[1], reverse=True)  # sort方法无返回值，所以不能用于赋值语句中
for i in range(10):
    print('{0:'
          '<10}{1:>5}'.format(countList[i][0], countList[i][1])
          )  # 中文字符限定输出长度，如果本身不够长默认补半角空格，是全角字符一半，故对不齐；因此需设置填充全角空格（' '/chr(12288)）
wordcloud = WordCloud(
    font_path='Deng.ttf', width=1920, height=1080,
    background_color='white').generate(' '.join(jieba.lcut(txt)))  # 使用的是等线体
wordcloud.to_file('wordcloud.png')
