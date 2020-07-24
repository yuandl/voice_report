from gensim.models import word2vec


print("读取格式化文本")
sentences = word2vec.Text8Corpus('baike_qa_valid_seg_0')

print("模型训练")
model = word2vec.Word2Vec(sentences, size=100, hs=1, min_count=1, window=3)

print("模型保存")
model.save("baike_qa_valid_seg_0.model")