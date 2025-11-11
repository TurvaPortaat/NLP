import gensim.downloader as api
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
model = api.load("word2vec-google-news-300")

model.similarity("king", "queen")

# Example
print(model.most_similar(positive=["king", "woman"], negative=["man"], topn=1))

# Mine
print(model.most_similar(positive=["animal", "toy", "soft"], negative=["cat"], topn=1))

pairs = [("UFO", "alien"),("apple", "banana"),("horse", "mouse"),("car", "bicycle"),("hammer", "nail")]
for word1, word2 in pairs:
     result = model.similarity(word1, word2)
     print(f"Similarity between '{word1}' and '{word2}': ", result)
    
print(model.most_similar(positive=['king','queen'], negative=['man'], topn=1))

words = ['music', 'culture', 'engine', 'car', 'function' 'probability']
vectors = np.array([model[word] for word in words])
pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(vectors)

plt.figure(figsize=(8, 6))
plt.scatter(reduced_vectors[:, 0], reduced_vectors[:,1], edgecolors='k', c='blue')

for i, word in enumerate(words):
    plt.annotate(word, (reduced_vectors[i, 0], reduced_vectors[i,1]))

plt.xlabel("PCA Component 1")    
plt.ylabel("PCA Component 2")
plt.title("Word2Vec PCA Visualization")
plt.grid(True)
plt.show()