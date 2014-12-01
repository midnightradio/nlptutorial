#!/usr/bin/env python
# coding=utf-8

from __future__ import unicode_literals, print_function, division
from collections import Counter
from itertools import chain
from math import log
import sys,io,os

__test_input      = "../../../test/01-test-input.txt"
__test_data_file  = "../../../data/wiki-en-test.word"
__model_file      = "./model_file"


def test_print(filename, prob_dict):
  ur"""
  >>> prob_dict = load_model()
  >>> test_print(__test_input, prob_dict)
  entropy = 2.45681342082
  coverage = 0.8
  """
  lambda_one  = .95
  lambda_unk  = 1-lambda_one
  V, W, H, unk = 10**6, .0, .0, 0
  word_generator = (word for line in io.open(filename) for word in chain(line.split(), ["</s>"])) 
  for word in word_generator:
    W += 1
    P = lambda_unk / V
    if word in prob_dict:
      P += lambda_one * prob_dict[word]
    else:
      unk += 1
    
    H -= log(P, 2)
  print("entropy = {}".format(H/W))
  print("coverage = {}".format((W-unk)/W))
  

def load_model():
  ur"""
  >>> prob_dict = load_model()
  >>> print(sorted(prob_dict.iteritems()))
  [(u'</s>', 0.25), (u'a', 0.25), (u'b', 0.25), (u'c', 0.125), (u'd', 0.125)]
  """
  return dict((w, float(p)) for (w, p) in (line.split() for line in io.open(__model_file)))
  
if __name__ == '__main__':
  prob_dict = load_model()
  filename = sys.argv[1] if len(sys.argv) >= 2 and os.path.isfile(sys.argv[1]) else __test_data_file
  print(filename)
  test_print(filename, prob_dict)