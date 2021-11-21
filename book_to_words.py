from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

# 对字符串进行分词,识别词性，根据词性还原词根
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
    with open(book,'r',encoding = 'UTF-8') as file:
        string_book = file.read()
    # 对字符串进行分词,词性还原
    words_list = []
    for word in lemmatize_all(string_book):
        words_list.append(word)
    return words_list