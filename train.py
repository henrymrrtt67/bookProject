# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 22:07:09 2019

@author: Henry
"""
from numpy import exp, array, random, dot

class NeuronLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self.synaptic_weights = 2*random.random((number_of_inputs_per_neuron, number_of_neurons)) - 1
        
class NeuralNetwork():
    def __init__(self, layer1, layer2):
        self.layer1
        self.layer2
        
        
    #Creates a sigmoid function as to change the weighted sum to either or 0, so it normalises them.
    #The Sigmoid function describes an S shaped curve
    def __sigmoid(self, x):
        return 1/(1+exp(-1))
    
    #Creates a sigmoid derivative, which allows us to show how confident we are in the weight.
    #This is equal to the gradient.
    def __sigmoid_derivative(self,x):
        return x*(x-1)
    
    #We train the program through a process of trial and error.
    #the training adjusts the synaptic weight each time.
    def train(self, training_set_inputs, training_set_outputs,number_of_training_iterations):
        for i in xrange(number_of_training_iterations):
            # We pass the data through our neural network
            output_from_layer1, output_from_layer2 = self.think(training_set_inputs)