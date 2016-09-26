#!/bin/python
import sys
import os
import lda
import jieba
import numpy as np

def get_word_map():
    word_file = jieba.get_dict_file()
    words = word_file.readlines()
    wordmap = {}
    wordid = 0
    for word in words:
        word = word.split()[0].decode('utf-8')
        wordmap[word] = wordid
        wordid += 1
    return wordmap

def get_file_list(input_folder):
    return [os.path.join(input_folder, f) for f in os.listdir(input_folder)]

def generate_X(input_files, word_map):
    X = np.zeros((len(input_files), len(word_map)), dtype=np.int32)
    for i in range(len(input_files)):
        words = jieba.lcut(open(input_files[i]).read())
        for word in words:
            wordid = word_map.get(word)
            if wordid is None:
                continue
            X[i][wordid] = 1
        if i % 10 == 0:
            print 'Finish parsing %d documents' % i
    return X
            
def main():
    if len(sys.argv) < 2:
        sys.exit('Usage %s <input folder>' % sys.argv[0])
    input_folder = sys.argv[1]
    input_files = get_file_list(input_folder)
    word_map = get_word_map()
    X = generate_X(input_files, word_map)
    model = lda.LDA(n_topics=20, n_iter=500, random_state=1)
    print 'Begin fit model'
    model.fit(X)
    print 'Finish fit model'
    topic_word = model.topic_word_
    print("type(topic_word): {}".format(type(topic_word)))
    print("shape: {}".format(topic_word.shape))
    n = 5
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(word_map.keys())[np.argsort(topic_dist)][:-(n+1):-1]
        print('*Topic {}\n- {}'.format(i, ' '.join(topic_words)))
    for n in range(10):
        topic_most_pr = doc_topic[n].argmax()
        print("doc: {} topic: {}\n{}...".format(n,
                    topic_most_pr,
                    titles[n][:50]))

if __name__ == '__main__':
    main()

