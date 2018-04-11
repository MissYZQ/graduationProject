"""

这一部分主要对提供的语料库做预处理，对未分词文本进行分词
如果分词已经完成，则不需要进行这一步
    注意：用jieba分词，中文环境下输入文本的编码应该是gbk或gb312，输出文本你的编码也应该是gbk或gb2312

"""
import jieba


class WordSegment:

    def word_segment(self, in_txt_name, seg_out_txt_name):

        # 打开文件，并返回句柄
        input_txt = open(in_txt_name)
        output_txt = open(seg_out_txt_name, 'a')

        # 开始读取文本进行分词处理，并将分词结果写入txt文件
        lines = input_txt.readlines()  # 读出整个文本
        for line in lines:
            line.replace('\t', '').replace('\n','').replace(' ', '')
            seg_list = jieba.cut(line, cut_all=False)
            output_txt.write(" ".join(seg_list))

        # 关闭文件句柄
        input_txt.close()
        output_txt.close()


"""

         # 对分词加过进行word2vec操作，得到词向量训练结果
        logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
        sentences = word2vec.Text8Corpus(u"segment_result.txt")

        model = word2vec.Word2Vec(sentences, min_count=1)
        print("1----", model)
        # vec_out_txt.write(model)
"""

ws = WordSegment()
ws.word_segment("in.txt", "segment_result.txt")
