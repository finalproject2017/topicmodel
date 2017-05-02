import json
import re
import numpy as np
import unicodedata
from guess_language import guess_language


with open('tripadvisor.json') as json_data:
    d = json.load(json_data)

mark = 1
thefile = open('enDoc.txt', 'w')
enDoc_len = 0
for doc in d:
    print(mark)
    mark = mark + 1
    sentence = unicodedata.normalize('NFKD', doc["body"]).encode('ascii', 'ignore')
    if guess_language(sentence) != 'en':
        continue
    enDoc_len = enDoc_len + 1
    thefile.write(sentence)
    thefile.write('\n')


print('file length with English')
print(enDoc_len)
thefile.close()









