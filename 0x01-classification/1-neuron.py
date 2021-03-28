#!/usr/bin/env python3

import numpy as np


class Neuron: 
    
  def __init__(self,nx):
    
    if nx<1 : 
      raise ValueError("nx must be a positive integer")
    
    #Attributes
    self.W = np.random.randn(nx)
    self.b = 0
    self.A = 0

@property
def W(self):
    return self.__W

@property
def b(self):
    return self.__b

@property
def A(self):
    return self.__A
