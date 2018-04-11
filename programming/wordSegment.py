"""

这一部分主要完成给未分词文本进行分词

"""
import jieba
from gensim.models import word2vec
import logging


class WordSegment:

    def word_segment(self, in_txt_name, seg_out_txt_name, vec_out_txt_name):

        # 打开文件，并返回句柄
        input_txt = open(in_txt_name)
        output_txt = open(seg_out_txt_name, 'a')
        vec_out_txt = open(vec_out_txt_name, 'a')

        # 开始读取文本进行分词处理，并将分词结果写入txt文件
        lines = input_txt.readlines()  # 读出整个文本
        for line in lines:
            line.replace('\t', '').replace('\n','').replace(' ', '')
            seg_list = jieba.cut(line, cut_all=False)
            output_txt.write(" ".join(seg_list))

        # 对分词加过进行word2vec操作，得到词向量训练结果
        logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
        sentences = word2vec.Text8Corpus(seg_out_txt_name)
        model = word2vec.Word2Vec(sentences, size=200)
        print(model)
        # vec_out_txt.write(model)

        # 关闭文件句柄
        input_txt.close()
        output_txt.close()
        vec_out_txt.close()