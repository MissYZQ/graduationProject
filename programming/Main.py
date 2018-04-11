"""
程序主函数位置，程序从这里开始运行

"""
from wordSegment import WordSegment  # 引入用于分词和将词转化为向量的类


ws = WordSegment()
ws.word_segment("in.txt", "segment_result.txt", "word2vec_result_txt")
