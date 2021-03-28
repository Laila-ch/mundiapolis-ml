#0-neuron.py


class Neuron : 
    
  def __init__(self,nx) :
    if type(nx)!="int" : 
      raise Exception("nx must be an integer")
    if nx<1 : 
      raise Exception("nx must be a positive integer")
      self.b = 0
      self.A = 0

