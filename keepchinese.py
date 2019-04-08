#coding=utf-8

import jieba
import pickle
from tqdm import tqdm

# 让文本只保留汉字
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def format_str(content):
    content_str = ''
    for i in content:
        if is_chinese(i):
            content_str = content_str + i
    return content_str

def writefile(doc, filepath):
    '''
    把分好词的文本写入到文件中
    Args:
        doc：文本list
    '''
    #分隔符
    sep = ' ' 
    with open(filepath, 'w+', encoding='utf-8') as f:
        for sequence in doc:
            newsequence=sep.join(sequence)
            f.write(newsequence +"\n")
        print("write finished!")

if __name__ == "__main__":

    target_fileQ = r"./data/test/cutQ.txt"
    target_fileA = r"./data/test/cutA.txt"
    f = open("./data/xiaohuangji.pkl",'rb')
    questions, answers = pickle.load(f)

    assert len(questions) == len(answers)
    q_list = []
    a_list = []
    for idx in range(len(questions)):
        Q = questions[idx]
        A = answers[idx]
        Q = format_str(Q)
        A = format_str(A)
        # 只要有一个为空，就把对话去掉
        if not Q.strip() or not A.strip():
            continue
        q_list.append(Q)
        a_list.append(A)

    assert len(q_list) == len(a_list)

    new_qlist = []
    new_alist = []
    for q, a in tqdm(zip(q_list, a_list)):
        q = jieba.cut(q)
        a = jieba.cut(a)
        new_qlist.append(q)
        new_alist.append(a)
    writefile(new_qlist, target_fileQ)
    writefile(new_alist, target_fileA)
    print("generate test file completed!")
    f.close()