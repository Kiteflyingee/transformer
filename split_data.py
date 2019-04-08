#coding=utf-8

from random import randint

'''
切分训练集和测试集
'''

VAL_NUM = 1000
SRC_FILE = r"./data/test/cutQ.txt"
TAG_FILE = r"./data/test/cutA.txt"
TRA_SRC_FILE = r"./data/test/cutQ_train.txt"
TRA_TAG_FILE = r"./data/test/cutA_train.txt"
VAL_SRC_FILE = r"./data/test/cutQ_valid.txt"
VAL_TAG_FILE = r"./data/test/cutA_valid.txt"

def read():
    
    with open(SRC_FILE, 'r', encoding="utf-8") as sf,  \
            open(TAG_FILE, 'r', encoding='utf-8') as tf, \
            open(TRA_SRC_FILE, 'w', encoding='utf-8') as ts, \
            open(TRA_TAG_FILE, 'w', encoding='utf-8') as tt:
        src_lines = sf.readlines()
        tag_lines = tf.readlines()
        assert len(src_lines) == len(tag_lines)
        totalnum = len(src_lines)
        src_val_set = []
        tag_val_set = []
        count = 0
        while count < VAL_NUM:
            randidx =  randint(1, totalnum) 
            if randidx < VAL_NUM:
                count += 1
                src_val_set.append(src_lines.pop(randidx))
                tag_val_set.append(tag_lines.pop(randidx))
        ts.writelines(src_lines)
        tt.writelines(tag_lines)
    return src_val_set, tag_val_set

def write(src_val_set, tag_val_set):
    
    with open(VAL_SRC_FILE, 'w', encoding='utf-8') as sf,\
            open(VAL_TAG_FILE, 'w', encoding='utf-8') as tf:
        
        for val in src_val_set:
            val = val.strip()
            sf.write(val + '\n')
        
        for val in tag_val_set:
            val = val.strip()
            tf.write(val + '\n')


if __name__ == "__main__":

    src_val_set, tag_val_set = read()    
    write(src_val_set, tag_val_set)