#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function, unicode_literals, division
import sys, os, io
from collections import Counter
from itertools import imap
from pprint import pprint

__test_input  = "../../../test/00-input.txt"
__test_answer = "../../../test/00-answer.txt"
__data_file   = "../../../data/wiki-en-train.word"

def report(counter):
  ur"""
  >>> report(wordcount(__test_input)) # doctest: +NORMALIZE_WHITESPACE
  a   1
  c   2
  b   2
  d   1
  2
  0 0 0 0 0 1 
  """
  for w, c in counter.iteritems():
    print("%s\t%d"%(w,c))

  print(sum((1 for c in counter.itervalues() if c == 1)))
  print(counter['in'], counter['on'], counter['with'], counter['to'], counter['the'], counter['a'])

def wordcount(filepath):
  counter = Counter()
  for words in (line.split() for line in io.open(filepath)):
    counter.update(words)

  return counter
  

if __name__ == '__main__':
  datafile = sys.argv[1] if len(sys.argv) >= 2 and os.path.isfile(sys.argv[1]) else __data_file

  counter = wordcount(datafile)
  report(counter)
