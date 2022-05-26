from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import pandas as pd


# 对字符串进行分词,识别词性，根据词性还原单词原型
def lemmatize_all(text):
    wnl = WordNetLemmatizer()
    for word, tag in pos_tag(word_tokenize(text)):
        if tag.startswith('NNP'):
            yield wnl.lemmatize(word, pos='n')
        elif tag.startswith('NN'):
            yield wnl.lemmatize(word, pos='n').lower()
        elif tag.startswith('VB'):
            yield wnl.lemmatize(word, pos='v').lower()
        elif tag.startswith('JJ'):
            yield wnl.lemmatize(word, pos='a').lower()
        elif tag.startswith('R'):
            yield wnl.lemmatize(word, pos='r').lower()
        else:
            yield word.lower().lower()


def get_words_list(book):
    # 将文件读取为字符串
    with open(book, 'r', encoding='UTF-8') as file:
        string_book = file.read()
    # 对字符串进行分词,词性还原
    words_list = []
    for word in lemmatize_all(string_book):
        words_list.append(word)
    return words_list


def save_words_as_csv(book):
    words_list = get_words_list(book)

    #频率由高到低排列
    words_sort_by_freq = pd.value_counts(words_list)
    dict_word = {
        'word': words_sort_by_freq.index,
        'count': words_sort_by_freq.values
    }
    words = pd.DataFrame(dict_word)

    #清除有标点符号行,字母小于二的行
    words = words[~words['word'].str.contains(
        '~|\|`|!|@|#|\$|%|\^|&|\*|\(|\)|-|_|\+|=|{|\[|}|]|:|;|"|\'|<|,|>|\.|/|\?|—|（|）|1|2|3|4|5|6|7|8|9|0'
    )]
    words = words[~(words['word'].str.len() < 3)]
    words.reset_index(drop=True, inplace=True)

    words.to_csv('output/words_rank.csv', index=False)
    print('Save as output/words_rank.csv')
