from __future__ import division
import math
import sklearn
import os
import sys
import re
import pandas
import numpy as np
import scipy
import unicodedata
import nltk
nltk.download()
from collections import Counter
from nltk.corpus import wordnet as wn
from nltk import word_tokenize,sent_tokenize
from nltk.corpus import PlaintextCorpusReader
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
import StringIO
from os import path
import cPickle as pickle
import sklearn.preprocessing as pp
import string
from decimal import Decimal
from collections import Counter
from decimal import Decimal
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

def sci_str(dec):
    return ('{:.' + str(len(dec.normalize().as_tuple().digits) - 1) + 'E}').format(dec)

def definition():
	global R   #Here you give a value to bilbodog (even None)
	R={}




class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)


def isNotBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return True
    #myString is None OR myString is empty or blank
    else:
         return False

def definition():
	global S   #Here you give a value to bilbodog (even None)
	S={}
	


WORD = re.compile(r'\w+')

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

path = "/Python27/training/C01"
def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
count = 0
totalTxt=""
full_file_paths = get_filepaths("/Python27/training/C01")

for file in full_file_paths:
    #f = os.path.basename(file)
    note = open(file, "r")
    txt=note.read()
    totalTxt+=txt
    count+=1
    note.close() 
for c in string.punctuation:
     totalTxt= totalTxt.replace(c,"")   
totalTxt=re.sub(r'\s+',' ',totalTxt)
totalTxt='\''+totalTxt+'.\''
holdLemmas=totalTxt
k=len(holdLemmas)
if (len(holdLemmas)!=3):
	print holdLemmas
vector1 = text_to_vector(holdLemmas)
j=vector1
    #vector2 = text_to_vector(holdLemmas)
    #print vector1
P={}
f = open("/Perl/cosineTriples")
tripleWords = []
lines = f.readlines()
for line in lines:
    line2=line.split("|")
    line2Length=len(line2)
    for  i, a in enumerate(line2):
        if (isNotBlank(a)):
            #print a, i, j[a]
            if (j[a]==0):
                j[a]=0.5
        if (i==1):
            curStr=a
            curValue=float(j[a])/k
            if curStr.strip():           # line contains eol character(s)
                  curS = curStr
        elif(i==2):
            curStr=curStr+' '+a
            prevValue=curValue
            curValue=float(j[a])/k
            if curStr.strip():           # line contains eol character(s)
                curS = curStr
            curValue*=prevValue
        elif(i==3):
            curStr=curS+' '+a
            curValue=float(j[a])/k
            curValue*=prevValue
            if curStr.strip():           # line contains eol character(s)
                 curS = curStr
            #print curS, curValue
            P[curS]=curValue








path = "/Python27/training/C02"
AAAA="AAAA"

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   

totalTxt1=""
full_file_paths = get_filepaths("/Python27/training/C02")

Q={}


for file in full_file_paths:
#f = os.path.basename(file)
    note = open(file, "r")
    txt=note.read()
    totalTxt1+=txt
    count+=1
    note.close() 
for c in string.punctuation:
     totalTxt1= totalTxt1.replace(c,"")   
totalTxt1=re.sub(r'\s+',' ',totalTxt1)
totalTxt1=totalTxt1+'.\''
totalTxt1='\''+totalTxt1
holdLemmas=totalTxt1
k=len(holdLemmas)
if (len(holdLemmas)!=3):
	print holdLemmas
vector1 = text_to_vector(holdLemmas)
j=vector1
    #vector2 = text_to_vector(holdLemmas)
    #print vector1
f = open("/Perl/cosineTriples")
tripleWords = []
lines = f.readlines()
for line in lines:
    line2=line.split("|")
    line2Length=len(line2)
    for  i, a in enumerate(line2):
        if (isNotBlank(a)):
            #print a, i, j[a]
            if (j[a]==0):
                j[a]=0.5
        if (i==1):
            curStr=a
            curValue=float(j[a])/k
            if curStr.strip():           # line contains eol character(s)
                  curS = curStr
        elif(i==2):
            curStr=curStr+' '+a
            prevValue=curValue
            curValue=float(j[a])/k
            if curStr.strip():           # line contains eol character(s)
                curS = curStr
            curValue*=prevValue
        elif(i==3):
            curStr=curS+' '+a
            curValue=float(j[a])/k
            curValue*=prevValue
            if curStr.strip():           # line contains eol character(s)
                 curS = curStr
            #print curS, curValue
            Q[curS]=curValue


#for k, v in Q.iteritems():
	    #print(k,v)


path = "/Python27/test/C01"
			

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
count = 0

full_file_paths = get_filepaths("/Python27/test/C01")

correctlyClassified=0
incorrectlyClassified=0

fileList=[]

curStr=""
curValue=0.0
textLemmas=""
lemma=""
line=""
BBBB="BBBB"
count=0
R={}
HIV={}
TUBERCULOSIS={}
Tuberc=0
Hiv=0
end_result = 0


for file in full_file_paths:
    f = os.path.basename(file)
    note = open(file, "r")
    text=note.read()
    #print f
    H=HashTable()
    H[count]=text
    #print count
    #print H[count]
    count+=1
    if count < 400:
        for c in string.punctuation:
           text= text.replace(c,"")
        tokens = word_tokenize(text)
        tagged_tokens = pos_tag(tokens)
        for tagged_token in tagged_tokens:
            word = tagged_token[0]
            for c in string.punctuation:
                word= word.replace(c,"") 
            word_pos = tagged_token[1]
            if ((word_pos=="JJ") or (word_pos=="NN") or (word_pos=="VB")
                or (word_pos=="VBD") 
                or (word_pos=="NNS") or  (word_pos=="VBG") or(word_pos=="VBN")
                or  (word_pos=="VBP") 
                or (word_pos=="JJR") or (word_pos=="JJS") or (word_pos=="VBZ")):
                lemma = wordnet_lemmatizer.lemmatize(word)
                #print lemma
                textLemmas=textLemmas+' '+lemma
        textLemmas='\''+textLemmas+' .\'\n'
        textLemmas=re.sub(r'\'\s+','\'',textLemmas)
        holdLemmas=textLemmas
        k=len(holdLemmas)
        if (len(textLemmas)!=3):
            print textLemmas
        vector2 = text_to_vector(textLemmas)
        textLemmas=""
        holdLemmas=""
        l=vector2
        #vector2 = text_to_vector(holdLemmas)
        #print vector1
        f = open("/Perl/cosineTriples")
        belongsToP=0
        belongsToQ=0
        tripleWords = []
        lines = f.readlines()
        for line in lines:
            line2=line.split("|")
            line2Length=len(line2)
            for  i, a in enumerate(line2):
                if (isNotBlank(a)):
        #print a, i, j[a]
                  if (l[a]==0):
                      l[a]=0.5
                  if (i==1):
                     curStr=a
                     curValue=float(l[a])/k
                     if curStr.strip():           # line contains eol character(s)
                        curS = curStr
                  elif(i==2):
                     curStr=curStr+' '+a
                     prevValue=curValue
                     curValue=float(l[a])/k
                     if curStr.strip():           # line contains eol character(s)
                        curS = curStr
                     curValue*=prevValue
                  elif(i==3):
                     curStr=curS+' '+a
                     curValue=float(l[a])/k
                     curValue*=prevValue
                     if curStr.strip():           # line contains eol character(s)
                        curS = curStr
                     #print curS, curValue
                     R[curS]=curValue    
      
        for k, v in R.iteritems():
            #(k,v) 
            for m, n in P.iteritems():
                 #print(k,v
                 #print(l,w)                                 
                if (k==m):
                    #print(k, v, n)
                    p_one=n*math.log(n)/math.log(v)
                    p_one+=p_one
                    TUBERCULOSIS[count]=p_one
        for k, v in R.iteritems():
            for l, o in Q.iteritems():
                if (k==l):
                   #print(k, v, o)
                   p_two=o*math.log(o)/math.log(v)
                   p_two+=p_two
                   HIV[count]=p_two

    
for i, p_one in TUBERCULOSIS.iteritems():
    for j, p_two in HIV.iteritems():
        if (j==i):
            print(j)
            if (p_one>p_two):
                Tuberc+=1
            elif(p_two>p_one):
                Hiv+=1

print "assigned to TUBERCULOSIS:", Tuberc


testfilesPOSTuberculosis=open('/Python27/testfPosTub', 'w')
for item in fileList:
    testfilesPOSTuberculosis.write("%s\n" % item)

