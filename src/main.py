# -*- coding: utf-8 -*-
""" Inference API """

import os
from modeling import predict, load_tools
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hello world"

@app.get("/predict/")
async def predict_sent(seed_text: str, len_resp: int):
    # Get models path for Unix systems
    abs_path = "/".join(os.path.abspath(".").split("/")[:-1])
    model_abs_path = os.path.join(abs_path, "models")
    model, max_len, tokenizer = load_tools(
                                model_abs_path, 
                                os.path.join(model_abs_path, "tok.pickle")
                                )
    return predict(seed_text, len_resp, model, max_len, tokenizer)