# topicmodel


Part 1: Complie (Execute this command at lda file)

       # complie _lda.pyx => _lda.c => _lda.so
       
       1. _lda.pyx => _lda.c

          cython _lda.pyx

       2. gamma.c => gamma.o

          gcc -c -mtune=generic -march=x86-64 -g -O3 -fno-strict-aliasing -fwrapv -fPIC gamma.c

       3. gamma.o, _lda.c => _lda.so

           gcc -shared -mtune=generic -march=x86-64 -g -O3 -fno-strict-aliasing -fwrapv -fPIC -I/usr/include/python2.7 -o _lda.so _lda.c gamma.o




Part 2: Preprocess Data:(Execute py file)
      1. tripavisor.json => all2en.py => enDoc.txt
      2. enDoc.txt => preprocess.py => cleanDoc.txt
      3. cleanDoc.txt => build_word_matrix.py => wordBags.txt , doc_word_matrix.npy  (change cutoff: only words appear in more than cutfoo times in document)
      4. wordBags.txt = > weight.py => topic_voc.npy  (Change the parametetr weight in this file)



Part 3: LDA(Execute py file)
     
      # Load document-vocab matrix
      1. X = np.load('doc_word_matrix.npy')
      # Load topic-vocab weight matrix
      2. weights = np.load('topic_voc.npy')
      # Load vocab list
      3. with open('wordBags.txt') as line:
               word_dic = line.read().splitlines()

          vocab = tuple(word_dic)


      #fit Model with two matrix
      model = lda.LDA(n_topics=4, n_iter=500, random_state=1, weight = weights)
      model.fit(X)  # model.fit_transform(X) is also available
      topic_word = model.topic_word_  # model.components_ also works

      # choose number of words to present topic and show topic words
	    n_top_words = 20
	    for i, topic_dist in enumerate(topic_word):
	        topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
	       print('Topic {}: {}'.format(i, ' '.join(topic_words)))





Part 4: Dependencies
 
          1. Linux (gcc, any version)
          2. python 2.7: 
                   numpy, cython, pbr, gensim, stop_words, nltk, lda, textmining, guess_language
          3. Architecture:


