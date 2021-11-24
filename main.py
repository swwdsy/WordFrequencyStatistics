import pandas as pd
import book_to_words

# 修改书名
file_book = 'hp1ch1'
file_dict = 'ky'
# 获取全书所有单词列表存为csv文件
book_to_words.save_words_as_csv('book/' + file_book + '.txt')

# 读取整理好的words 和 dict
file_words = 'output/words.csv'
words = pd.read_csv(file_words, index_col=0)
words[file_dict] = False
dict = pd.read_csv('dictionary/'+ file_dict + '.csv') 

# 判断是否为dict单词
words_len = len(words)
for i in range(0, len(dict)):
    try: 
        words.loc[dict['word'][i], file_dict] = True
    except:
        break
    else:
        len = len
words = words.head(words_len)

# 判断 书中dict单词 占 全部dict单词的百分比
number_of_words_in_dict = len(words.loc[words[file_dict] == True])
number_of_dict = len(dict)
output = file_book + "中的" + file_dict + "单词 占 所有" + file_dict + "单词 的" + str(round((number_of_words_in_dict/number_of_dict*100), 2)) + '%'
print(output)

words.to_csv('output/words_result.csv')
# words.loc[words[file_dict] == True, ['word', 'count']].to_csv('output\word_in_dict.csv')
# words.loc[words[file_dict] == False, ['word', 'count']].to_csv('output\word_without_in_dict.csv')
