# -*- coding: utf-8 -*-
""" Inference API """

from modeling import predict, load_model, load_tokenizer
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hello world"

@app.post("/predict/")
async def predict_sent(seed_text: str, resp_length: int):
    tok = load_tokenizer()
    model = load_model()
    max_len = None # find way to get max_len from model object
    return predict(seed_text, resp_length, model, max_len, tok)