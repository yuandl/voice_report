# encoding=utf-8
import jieba
import os
import json
import re


def segment_lines(file_list, segment_out_name):
    '''
    字词分割，对整个文件内容进行字词分割
    :param file_list:
    :param segment_out_dir:
    :param stopwords:
    :return:
    '''
    for i, file in enumerate(file_list):
        # segment_out_name=os.path.join(segment_out_dir,'segment_{}.txt'.format(i))

        result = ''
        file = '../data/' + file
        print("读入文件:" + file)
        with open(file, 'r', encoding='utf-8') as f:
            j = 0
            for line in f.readlines():
                print(j)
                dic = json.loads(line)
                # 去除非中文字符
                # pattern = re.compile(r'[^\x00-\x7f]')
                result += str(dic['answer']).replace("\r\n", "").replace("\t", "")
                j += 1

        print("分词:" + file)
        line_cut = jieba.cut(result)
        result = ' '.join(line_cut)

        print("写出文件")
        with open('../model/' + segment_out_name + "_" + str(i), "w", encoding='utf-8') as f2:
            f2.write(str(result))

            # document_cut = jieba.cut(document)
            # sentence_segment=[]
            # for word in document_cut:
            #     if word not in stopwords:
            #         sentence_segment.append(word)
            # result = ' '.join(sentence_segment)
            # result = result.encode('utf-8')
            # with open(segment_out_name, 'wb') as f2:
            #     f2.write(result)


def cut(text):
    seg_list = jieba.lcut(text, cut_all=True)
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式


if __name__ == '__main__':
    # cut("我要看，部门加班情况")
    # segment_lines(["test.json"], "test_seg")
    segment_lines(["baike_qa_train.json"], "baike_qa_train_seg")
    # segment_lines(["baike_qa_valid.json"], "baike_qa_valid_seg")
