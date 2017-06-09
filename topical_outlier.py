# Quentin Truong
# Solution to "The Phamtom Intern Challenge: #3" 
#
# Challenge Statement:
# 3. Given a set of ten words identify a topical outlier. For example in the following set, sausage is an outlier: “red green blue orange white black sausage purple pink”
#
# Requires: 
# python3.5 
# gensim
# a pretrained word2vec model (For example: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit)

import gensim

#Load Google's pretrained word2vec model
print("Start loading Google's pretrained word2vec model, this may take a while")
model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)
print("Finished loading")

#Find outlier in set using gensim and word2vec
mySet = "red green blue orange white black sausage purple pink"
mySet = mySet.split()
print("Find topical outlier in", mySet)
print("Topical outlier: ", model.doesnt_match(mySet))