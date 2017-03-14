#!/usr/bin/python
#tweet
#Student: Changle Xu, Yuan Gao, Bei Xia

import cPickle as pickle
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import sys

sys.stderr.write("Started mapper.\n");

def word_feats(words):
    # Turn a string into a list of feature words
    return dict([(word, True) for word in words])

def main(argv):
    # Classifier trained with example from:
    # http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/
    classifier = pickle.load(open("movclass.p", "r"))
    for line in sys.stdin:
        #Lower every letter for the purpose of decreasing the difficulty
        line = line.lower()
        # split line into words and test with classifier
        tolk_posset = word_tokenize(line.rstrip())
        d = word_feats(tolk_posset)
        
        #for each president, the first and second means the president's name in the file; the third is used as key
        president = [("ben","carson","Carson"),("hillary","clinton","Clinton"),("bernie","sanders","Sanders"),("donald","trump","Trump")]
        name = ""
        num = 0
        for word in president:
                if word[0] in line or word[1] in line:
                        num += 1
                        #If a tweet contains more than one candidate's name we ignore it
                        if num ==1:
                                name = word[2]
                        break
        #the key of output is name-pos or name-neg; the value of output is the amounts
        if name.strip():
                print "LongValueSum: %s" % name +"-" +classifier.classify(d) + "\t" + "1"

if __name__ == "__main__":
    main(sys.argv)

