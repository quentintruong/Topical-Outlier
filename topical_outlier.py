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