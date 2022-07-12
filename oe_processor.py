#oe_modules takes standard settings from the OE model and loads them into the nlp object

#import stanza
import oe_modules
from oe_modules import nlp
import sys

#Takes a sentence to be tokenized and lemmatized. It will eventually read from a file.

doc = nlp('eala þu cleric wuna þu lareow gelæred þæt an.')

#Processes the text into tokens and lemmas

def oe_processor():
    #Creates and opens a file in writing mode, to take the output of the function.
    sys.stdout = open('oe_test.csv', 'w')
    for i, sentence in enumerate(doc.sentences):
        tokens = ([f'id: {token.id}\ttext: {token.text}\t' for token in sentence.tokens])
        lemmas = ([f'lemma: {word.lemma}' for sent in doc.sentences for word in sent.words])
        #Prints the output of tokens and lemmas in column format. Should be extendable to pos tagger and depparser
        for t, l in zip(tokens, lemmas):
            print(t, l)

oe_processor()