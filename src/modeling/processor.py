# -*- coding: utf-8 -*-

# import Tokenizer
# import padding
import pickle
import numpy as np

class Processor:
    """ Common base for handling data """
    def __init__(self, data):
        self.data = data
        self.tokenizer = Tokenizer() # remove filters
    
    def create_inputs(self):
        # base: ([q1, q2, q3, q4], [a1, a2])
        # flatten it:
        # input 1 : [q1, q2, q2, q4] | output 1: a1
        # input 2 = [q1, q2, q2, q4, a1] | output 2: a2
        pass
    
    def _inputs_to_ids(self):
        pass

    def save_tokenizer(self): # should this be static?
        """
        Save Processor with Tokenizer fit on training data
        """
        pass

    def is_fit(self) -> bool: # to modify
        """  """        
        if len(self.tokenizer.word_index) > 1:
            return True
        return False