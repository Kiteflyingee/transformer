# -*- coding: utf-8 -*-
class Params:
	'''
	Parameters of our model
	'''
	src_train = "data/test/cutQ_train.txt"
	tgt_train = "data/test/cutA_train.txt"
	src_test = "data/test/cutQ_valid.txt"
	tgt_test = "data/test/cutA_valid.txt"
	enc_vocab = 'test_en.vocab.tsv'
	dec_vocab = 'test_de.vocab.tsv'

	maxlen = 10
	batch_size = 256
	hidden_units = 512
	logdir = 'logdir'
	num_epochs = 50
	num_identical = 6
	num_heads = 8
	dropout = 0.1
	learning_rate = 0.0001
	word_limit_size = 20
	word_limit_lower = 3
	checkpoint = 'checkpoint'
