import pandas as pd
import book_to_words


book = 'book\hp1.txt'
# 获取全书所有单词列表
words_list = book_to_words.get_words_list(book)

#频率由高到低排列
words_sort_by_freq = pd.value_counts(words_list)
dict_word = {'word':words_sort_by_freq.index, 'count':words_sort_by_freq.values}
words = pd.DataFrame(dict_word)

#清除有标点符号行
words = words[~words['word'].str.contains('~|`|!|@|#|\$|%|\^|&|\*|\(|\)|-|_|\+|=|{|\[|}|]|:|;|"|\'|<|,|>|\.|/|\?')]
words.reset_index(drop=True,inplace=True)
# 添加列
words.loc[:, 'cet4'] = False
words.loc[:, 'cet6'] = False
words.loc[:, 'kaoyan'] = False

print(words.tail())
