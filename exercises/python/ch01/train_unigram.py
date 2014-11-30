#!/usr/bin/env python
# coding=utf-8

from __future__ import unicode_literals, print_function, division
from itertools import chain
from collections import Counter
import sys, io, os

__train_input     = "../../../test/01-train-input.txt"
__train_data_file = "../../../data/wiki-en-train.word"
__model_file      = "./model_file"

def report(counter):
  ur"""
  >>> counter = train_unigram(__train_input)
  >>> report(counter)
  >>> print(io.open(__model_file).read()) # doctest: +NORMALIZE_WHITESPACE
  </s> 0.25
  a 0.25
  b 0.25
  c 0.125
  d 0.125
  """
  total_count = sum(count for (word, count) in counter.iteritems())

  with io.open(__model_file, mode="w", encoding='utf8') as f:
    for (word, prob) in sorted((word, count / total_count) for (word, count) in counter.iteritems()):
      print("{0}\t{1}".format(word, prob), file=f)
      
def train_unigram(filename):
  counter = Counter()
  counter.update(word for line in io.open(filename) for word in chain(line.split(), ["</s>"])) 
  return counter
  
if __name__ == '__main__':
  filename = sys.argv[1] if len(sys.argv) >= 2 and os.path.isfile(sys.argv[1]) else __train_data_file
  print(filename)
  counter = train_unigram(filename)
  report(counter)
  