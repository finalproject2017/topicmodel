# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import lda



with open('pro_data/wordBags.txt') as line:
    word_dic = line.read().splitlines()

vocab = tuple(word_dic)
print(type(vocab))




X = np.load('pro_data/doc_word_matrix.npy')
#Y = X[0:10000, :]

print(X.shape)



weights = np.load('pro_data/topic_voc.npy')
print(weights.shape)



model = lda.LDA(n_topics=4, n_iter=20000, random_state=1, weight = weights)
model.fit(X)  # model.fit_transform(X) is also available
topic_word = model.topic_word_  # model.components_ also works


n_top_words = 20
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))