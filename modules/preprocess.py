#!coding:utf-8
# Preprocessing module
import unicodedata, re
from janome.tokenizer import Tokenizer

# Evaluate which language type English or Japanese (module: unicodedata)
def lang_judge(text):
    for ch in text:
        word = unicodedata.name(ch)
        if "CJK UNIFIED" in word or "HIRAGANA" in word or "KATAKANA" in word:
            return("Japanese")  # If "Hiragana" or "Katakana" or "Kanji" included, It's Japanese.
    return("English")  # If not, English.

# English preprocessing
def english(text):
    text = text.lower()  # replace words for lowercase.
    text = re.sub(r',', '', text)  # remove comma.
    replace = text.maketrans({  # replace symbols.
        ',':'',
        '.':'',
        '!':'',
        '?':''})
    text = text.translate(replace)  # replace.
    return text

# Japanese preprocessing (module: Janome)
def japanese(text):
    t = Tokenizer()  # generate instance .
    replace = text.maketrans({  # replace symbols. 削除(置換)対象の記号を登録.
        '　':'',
        '、':'',
        '。':'',
        '，':'',
        '．':'',
        '！':'',
        '？':'',
        '!':'',
        '?':''})
    text = text.translate(replace)  # replace. 削除(置換)を実行.
    text = t.tokenize(text, wakati=True)  # wakatigaki. 日本語を分かち書きする
    result = ' '.join(text)  # concatenate with space.
    return result
