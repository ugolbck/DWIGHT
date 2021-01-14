# -*- coding: utf-8 -*-

from src.data import Dataset
from src.modeling import Processor

from typing import Optional
from pathlib import Path

def load_data(path_to_data: Optional[Path] = None):
    """ Load Dataset instance """
    if path_to_data:
        return Dataset(path=path_to_data)
    return Dataset()

def prepare_data(dataset, processor):
    pass

def create_model():
    pass

def fit_model(model):
    pass