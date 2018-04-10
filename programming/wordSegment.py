"""

这一部分主要完成给定未分词文本的分词

"""



import jieba

class WordSegment:

    def word_segment(self, in_txt_name, out_txt_name):
        input_txt = open(in_txt_name)
        output_txt = open(out_txt_name, 'a')
        lines = input_txt.readlines() #读出整个文本
        for line in lines:
            line.replace('\t', '').replace('\n','').replace(' ', '')
            seg_list = jieba.cut(line, cut_all=False)
            output_txt.write(seg_list)

        input_txt.close()
        output_txt.close()
