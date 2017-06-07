from gensim.models import word2vec

model = word2vec.Word2Vec.load('model/wiki.model')

results = model.most_similar(positive=["王"], negative=["男"])
for result in results:
  print(result)
