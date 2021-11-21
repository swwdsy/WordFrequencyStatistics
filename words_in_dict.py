import pandas

words = pandas.Series(['a', 'b', 'c', 'd', 'e', 'f', 'i'])
dict = pandas.Series(['a', 'e', 'i', 'o', 'u'])

words = pandas.DataFrame({'word':words.values,'inDict': False})

for i in range(0,len(words['word'])):
    for j in dict:
        if words['word'].loc[i] == j:
            words['inDict']=words['inDict'].copy() #避免警告
            words['inDict']=True
            break
result = words['inDict']

print(result)

# 判断是否为字典中的单词，返回bool Series
def is_inDict(words, dict):
    words = pandas.DataFrame({'word':words.values,'inDict': False})

    for i in range(0,len(words['word'])):
        for j in dict:
            if words['word'].loc[i] == j:
                words['inDict'].loc[i] = True
                break
    return words['inDict']