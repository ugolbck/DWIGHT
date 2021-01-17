# -*- coding: utf-8 -*-
""" Inference API """

from modeling import predict, load_tools
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hello world"

@app.get("/predict/")
async def predict_sent(seed_text: str, len_resp: int):
    model, max_len, tokenizer = load_tools(
                                "/Users/ugo/Documents/Projects/project-dwight/DWIGHT/models/", 
                                "/Users/ugo/Documents/Projects/project-dwight/DWIGHT/models/tok.pickle"
                                )
    return predict(seed_text, len_resp, model, max_len, tokenizer)