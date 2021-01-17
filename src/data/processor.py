# -*- coding: utf-8 -*-

from pathlib import Path
import pickle
import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

class Processor:
    """ Common base for handling data """
    def __init__(self, data):
        self.data = data
        self.tokenizer = Tokenizer(filters='', lower=True)
    
    def create_inputs(self):
        self.tokenizer.fit_on_texts(self.data)
        total_words = len(self.tokenizer.word_index) + 1
        # Tokenize corpus and encode to IDs
        tok_corpus = self._inputs_to_ids()

        max_len = max([len(x) for x in tok_corpus])
        padded_corpus = np.array(pad_sequences(tok_corpus, maxlen=max_len, padding='pre'))
        
        X, y = padded_corpus[:,:-1], padded_corpus[:,-1]
        y = to_categorical(y, num_classes=total_words)
        return X, y, max_len, total_words
    
    def _inputs_to_ids(self):
        corpus_as_ids = []
        for line in self.data:
            tokens = self.tokenizer.texts_to_sequences([line])[0] # creates a nested list
            for i in range(1, len(tokens)):
                n_gram_sequence = tokens[:i+1]
                corpus_as_ids.append(n_gram_sequence)
        return corpus_as_ids

    def save_tokenizer(self, path: Path): # should this be static?
        """
        Save Tokenizer fit on training data
        """
        assert self.is_fit(), "The Tokenizer object is not fit on texts"
        pickle.dump(self.tokenizer, path)

    def is_fit(self) -> bool: # to modify
        """  """        
        if len(self.tokenizer.word_index) > 1:
            return True
        return False