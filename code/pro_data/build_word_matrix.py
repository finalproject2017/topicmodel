import json
import textmining
import numpy as np
import unicodedata


tdm = textmining.TermDocumentMatrix()
thefile = open('wordBags.txt', 'w')

with open('cleanDoc.txt') as line:
    document = line.read().splitlines()
words = set()


len_doc = len(document)

cutoff_thredhold = int(len_doc * 0.0004)

for doc in document:
    tdm.add_doc(doc)


j = 1
for row in tdm.rows(cutoff=cutoff_thredhold):
    len_words = len(row)
    for item in row:
        thefile.write("%s\n" % item)
    if j == 1:
        break
thefile.close()


print(len_doc)
print(len_words)


doc_word_matrix = np.ndarray(shape=(len_doc,len_words), dtype=np.intc)

j = -1
for row in tdm.rows(cutoff=cutoff_thredhold):
    if j == -1:
        j = j + 1;
        continue

    doc_word_matrix[j] = row
    j = j + 1
    print(j)


np.save('doc_word_matrix.npy', doc_word_matrix)



