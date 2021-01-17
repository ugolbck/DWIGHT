# -*- coding: utf-8 -*-
""" Prediction side """

import pickle
from pathlib import Path
from tensorflow.keras.models import load_model

def load_tools(path_model: Path, path_tok: Path):
    model = load_model(path_model)
    max_len = model.get_config()["layers"][0]["config"]["batch_input_shape"][1] + 1
    tokenizer = pickle.load(path_tok)
    return model, max_len, tokenizer


def generate_text(seed_text, next_words, model, max_sequence_len, tokenizer):
    response = seed_text
    for _ in range(next_words):
        tokens = tokenizer.texts_to_sequences([response])
        tokens = pad_sequences(tokens, maxlen=max_sequence_len-1, padding='pre')
        
        predicted = model.predict(tokens, verbose=0)
        predicted = np.argmax(predicted)
        
        new_word = tokenizer.index_word[predicted]
        response += new_word + " "
    return response

def predict(s, l):
    return "Boobs"