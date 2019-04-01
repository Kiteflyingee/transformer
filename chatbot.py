# -*- coding: utf-8 -*-
from __future__ import print_function
import codecs
import os
from train import Graph
from params import Params as pm
from data_loader import load_data, load_vocab, getword_idx, generate_dataset
import tensorflow as tf
import numpy as np
import jieba

def chatbot():
	en2idx, idx2en, de2idx, idx2de = getword_idx()
	g = Graph(en2idx, de2idx, is_training = False)
	print("MSG : Graph loaded!")
	with g.graph.as_default():
		sv = tf.train.Supervisor()
		with sv.managed_session(config = tf.ConfigProto(allow_soft_placement = True)) as sess:
			# load pre-train model
			sv.saver.restore(sess, tf.train.latest_checkpoint(pm.checkpoint))
			print("MSG : Restore Model!")
			while True:
				# X = input("请输入:")
				X = "你好啊"
				X = list(jieba.cut(X))
				X.append(u'<EOS>')
				inpt = [en2idx.get(word, 1) for word in X]
				X=np.zeros((1, pm.maxlen), np.int32)
				for i in range(pm.maxlen):
					if i < len(inpt):
						X[0,i] = inpt[i]
				# Autoregressive inference
				preds = []
				nppreds = np.zeros((1, pm.maxlen), dtype = np.int32)
				for j in range(pm.maxlen):
					_preds = sess.run(g.preds, feed_dict = {g.inpt: X, g.outpt: nppreds})
					preds.append(_preds[0,j])
				got = " ".join(idx2de[idx] for idx in preds).split("<EOS>")[0].strip()
				print(got)

if __name__ == "__main__":
    chatbot()