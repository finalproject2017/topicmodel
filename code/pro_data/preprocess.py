import json
import re
import numpy as np

from gensim import corpora, models

from stop_words import get_stop_words
en_stop = get_stop_words('en')
es_stop = get_stop_words('es')

from nltk.stem.porter import PorterStemmer
p_stemmer = PorterStemmer()

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

with open('enDoc.txt') as line:
    document = line.read().splitlines()

time = 0

texts = []

# loop through document list
thefile = open('cleanDoc.txt', 'w')
for i in document:

    print(time)
    time = time + 1
    # clean and tokenize document string
    cleanString = re.sub('(http://\S+|\S*[^\w\s]\S*)', '', i)

    raw = cleanString.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens_en = [i for i in tokens if not i in en_stop]
    #stopped_tokens = [i for i in stopped_tokens_en if not i in es_stop]

    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens_en]

    # add tokens to list
    str1 = ' '.join(stopped_tokens_en)
    thefile.write(str1)
    thefile.write('\n')


thefile.close()






