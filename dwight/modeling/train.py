# -*- coding: utf-8 -*-
""" Training side """
from dwight.data import Dataset, Processor

from typing import Optional
from pathlib import Path
import pickle

from tensorflow.keras import Model
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping


def load_data(path_to_data: Optional[Path] = None) -> Dataset:
    """ Load Dataset instance """
    if path_to_data:
        return Dataset(path=path_to_data)
    return Dataset()


def load_processor(dataset: Dataset):
    return Processor(dataset.get_line_pairs_as_list("Dwight"))


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


def fit_model(model: Model, X, y, epochs: int, batch_size: int, val_size: float):
    # TODO: early stopping
    history = model.fit(X, y, epochs=epochs, validation_split=val_size, batch_size=batch_size, verbose=1)
    return history


def evaluate(hist):
    pass


def save_tools(model, tokenizer, path: Path):
    # TODO: create new directory with date and hyperparam config + callbacks
    model.save(path)
    pickle.dump(tokenizer, path)


def main():
    data = load_data()
    processor = load_processor(data)
    X, y, max_len, n_words = processor.create_inputs()
    print(len(X), len(y), max_len, n_words)
