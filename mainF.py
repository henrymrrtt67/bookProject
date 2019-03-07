# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:12:23 2019

@author: Henry
"""
import nltk
nltk.download('punkt')

main()
def main():
    data = load_data()
    print("okay here")
    data.read()
    print(data)
    tokens = tokenize(data)

def load_data():
    return open("test.txt","r")

def tokenize(data):
    tokens = nltk.tokenizer.word_tokenize(data)
    return tokens