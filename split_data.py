#coding=utf-8

from random import randint

VAL_NUM = 200
SRC_FILE = r"./data/weibo/stc_weibo_train_post"
TAG_FILE = r"./data/weibo/stc_weibo_train_response"
VAL_SRC_FILE = r"./data/weibo/cutQ_valid.txt"
VAL_TAG_FILE = r"./data/weibo/cutA_valid.txt"

def read():
    
    with open(SRC_FILE, 'r', encoding="utf-8") as sf, \
            open(TAG_FILE, 'r', encoding='utf-8') as tf:
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
                src_val_set.append(src_lines[randidx])
                tag_val_set.append(tag_lines[randidx])
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