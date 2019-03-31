# -*- coding: utf-8 -*-
class Params:
	'''
	Parameters of our model
	'''
	src_train = "data/combine/cutQ.txt"
	tgt_train = "data/combine/cutA.txt"
	src_test = "data/combine/cutQ_valid.txt"
	tgt_test = "data/combine/cutA_valid.txt"
	enc_vocab = 'combine_en.vocab.tsv'
	dec_vocab = 'combinede.vocab.tsv'

	maxlen = 15
	batch_size = 64
	hidden_units = 512
	logdir = 'logdir'
	num_epochs = 5
	num_identical = 6
	num_heads = 8
	dropout = 0.1
	learning_rate = 0.0001
	word_limit_size = 20
	word_limit_lower = 3
	checkpoint = 'checkpoint'
