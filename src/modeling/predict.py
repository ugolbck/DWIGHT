# -*- coding: utf-8 -*-
""" Prediction side """

import pickle
from tensorflow.keras import Model

def load_model():
    pass

def load_tokenizer():
    pass

def generate_text(seed_text, next_words, model, max_sequence_len, tokenizer):
    response = seed_text
    for _ in range(next_words):
        tokens = tokenizer.texts_to_sequences([response])
        tokens = pad_sequences(tokens, maxlen=max_sequence_len-1, padding='pre')
        
        predicted = model.predict(tokens, verbose=0)
        predicted = np.argmax(predicted)
        try:
            new_word = tokenizer.index_word[predicted]
        except:
            raise
        # for word, index in tokenizer.word_index.items():
        #     if index == predicted:
        #         output_word = word
        #         break
        response += new_word + " "
    return response