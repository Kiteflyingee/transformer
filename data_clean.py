#coding=utf-8
from tqdm import tqdm
import jieba
import pickle

def clean(cut_words):
    '''
    '''
    stopwords = [' ', '\n',',' ,'@', '#','，', '。','！','‘', '’', "“","”",'《','》','?',"？",'.','︶︿︶']
    line_clean = []
    for word in cut_words:
        if word in stopwords:
            continue
        line_clean.append(word)
    if len(line_clean) == 0:
        line_clean = ['不会']
    return line_clean


def readfile(filepath):
    '''
    读取文件,清理文本，分词。
    :return a list: 每个元素为一个句子的分词list
    '''
    doc = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            words = jieba.cut(line)
            words = clean(words)
            doc.append(words)
    print("read finished!")
    return doc

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

def cleanQA():
    '''
    清理原始语料库，分词写入到文件中
    '''
    question_file = r"./data/combine/combineQ.txt"
    answer_file = r"./data/combine/combineA.txt"
    target_fileQ = r"./data/combine/cutQ.txt"
    target_fileA = r"./data/combine/cutA.txt"

    docQ = readfile(question_file)
    writefile(docQ, target_fileQ)
    docA = readfile(answer_file)
    writefile(docA, target_fileA)

def clean_testfile(filepath, target_fileQ, target_fileA):
    '''
    生成一个测试语料库
    '''
    questions, answers = pickle.load(open(filepath, 'rb'))
    q_list = []
    a_list = []
    for q, a in tqdm(zip(questions, answers)):
        q = jieba.cut(q)
        a = jieba.cut(a)
        q = clean(q)
        a = clean(a)
        q_list.append(q)
        a_list.append(a)

    writefile(q_list, target_fileQ)
    writefile(a_list, target_fileA)
    print("generate test file completed!")

if __name__ == "__main__":
    
    # cleanQA()
    filepath = r"data/qingyun.pkl"
    target_fileQ = r"./data/test/cutQ.txt"
    target_fileA = r"./data/test/cutA.txt"
    clean_testfile(filepath, target_fileQ, target_fileA)
