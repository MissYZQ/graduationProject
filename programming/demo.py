"""
程序主函数位置，程序从这里开始运行

    首先对已经进行分词的语料利用word2vec进行词向量转化

"""
from gensim.models import word2vec
import logging

"""

对分词加过进行word2vec操作，得到词向量训练结果

"""
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u"segment_result.txt")
model = word2vec.Word2Vec(sentences, min_count=1, size=50)
# model.save("word2vec_result.txt")  # 保存模型文件
model.wv.save_word2vec_format("word2vec_result")  # 输出词向量模型文件
# print("1----", model)


"""

通过词向量矩阵化操作将句子中的词向量组合成一个词向量矩阵

"""




