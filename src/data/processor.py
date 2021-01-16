# -*- coding: utf-8 -*-

import pickle
import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class Processor:
    """ Common base for handling data """
    def __init__(self, data):
        self.data = data
        self.tokenizer = Tokenizer(filters='', lower=True)
    
    def create_inputs(self):
        self.tokenizer.fit_on_texts(corpus)
        total_words = len(tokenizer.word_index) + 1
        
        corpus_as_ids = []
        for line in corpus:
            tokens = tokenizer.texts_to_sequences([line])[0] # creates a nested list
            for i in range(1, len(tokens)):
                n_gram_sequence = tokens[:i+1]
                corpus_as_ids.append(n_gram_sequence)
        return corpus_as_ids, total_words
    
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