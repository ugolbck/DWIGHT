# -*- coding: utf-8 -*-

from data import Dataset
from modeling import Processor

from typing import Optional
from pathlib import Path

from tensorflow.keras import Model
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping
import tensorflow.keras.utils as ku

def load_data(path_to_data: Optional[Path] = None):
    """ Load Dataset instance """
    if path_to_data:
        return Dataset(path=path_to_data)
    return Dataset()

def prepare_data(dataset):
    processor = Processor()

def create_model():
    pass

def fit_model(model):
    pass

def main():
    data = load_data()
    X, y, max_len, 


if __name__ == "__main__":
    maint()