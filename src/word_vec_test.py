import pandas as pd
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(common_texts)]
model = Doc2Vec(documents, seed=42, vector_size=5, window=2, min_count=1, workers=4)

print("inferrence...")
vector = model.infer_vector(["Angela", "killed", 'a', 'cat'])

print(vector)