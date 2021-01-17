# -*- coding: utf-8 -*-
""" Prediction side """

import pickle, os
from pathlib import Path

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

def load_tools(path_model: Path, path_tok: Path):
    model = load_model(path_model)
    max_len = model.get_config()["layers"][0]["config"]["batch_input_shape"][1] + 1
    if os.path.getsize(path_tok) > 0:    
        with open(path_tok, "rb") as f:
            tokenizer = pickle.load(f)
    else:
        print("Empty tokenizer file")
    print(model.summary(), "\n", max_len, tokenizer)
    return model, max_len, tokenizer


def predict(seed_text, next_words, model, max_sequence_len, tokenizer):
    response = seed_text
    for _ in range(next_words):
        tokens = tokenizer.texts_to_sequences([response])
        tokens = pad_sequences(tokens, maxlen=max_sequence_len-1, padding='pre')
        
        predicted = model.predict(tokens, verbose=0)
        predicted = np.argmax(predicted)
        
        new_word = tokenizer.index_word[predicted]
        response += new_word + " "
    return response[len(seed_text):]
