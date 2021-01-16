# -*- coding: utf-8 -*-
""" Training side """
from data import Dataset, Processor

from typing import Optional
from pathlib import Path

from tensorflow.keras import Model
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping

def load_data(path_to_data: Optional[Path] = None) -> Dataset:
    """ Load Dataset instance """
    if path_to_data:
        return Dataset(path=path_to_data)
    return Dataset()

def prepare_data(dataset: Dataset):
    processor = Processor(dataset.get_line_pairs_as_list("Dwight"))
    return processor.create_inputs()

def create_model(
    max_sequence_len: int,
    total_words: int,
    units: int,
    embed_size: int,
) -> Model:
    input_len = max_sequence_len - 1
    input = Input(shape=(input_len))
    x = Embedding(total_words, embed_size, mask_zero=True)(input)
    x = LSTM(units, activation="relu", recurrent_regularizer="l2", dropout=0.2)(x)
    output = Dense(total_words, activation='softmax')(x)
    model = Model(input, output)
    model.compile(loss='categorical_crossentropy', optimizer='Adam')
    return model

def fit_model(model: Model, X, y, epochs: int, batch_size: int, val_size: int):
    # TODO: early stopping
    history = model.fit(X_train, y, epochs=epochs, verbose=1)
    return history

def evaluate(hist):
    pass

def main():
    data = load_data()
    X, y, max_len, n_words = prepare_data(data)
    print(len(X), len(y), max_len, n_words)
