# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:12:23 2019

@author: Henry
"""
#importing a language package in order to tokenize the words
import nltk

#Defining the main and letting it be able to be called and must go through this every time
def main():
    # downloads data, reads the data and places this sentence into a variable, then placing it into the tokenizer
    data = load_data()
    data = data.read()
    tokens = tokenize(data)

#opens the file and downloads the file
def load_data():
    return open("test.txt","r")

#tokenizes the sentece with word tokenizer and returns these individual tokens in an array.
def tokenize(data):
    tokens = nltk.word_tokenize(data)
    return tokens

main()