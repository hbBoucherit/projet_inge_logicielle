from typing import Optional
from fastapi import FastAPI
from collections import defaultdict

import numpy as np
import sklearn
import joblib


labels = ['find-around-me','find-flight','find-hotel', 'find-restaurant', 'find-train',  'irrelevant', 'provide-showtimes', 'purchase']
model = joblib.load("nlp_model_log.pkl")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sentence/{sentence}")
def read_item(sentence: str):
    json = defaultdict(str)

    pred = model.predict([str(sentence)])[0] #label
    pred_proba = model.predict_proba([str(sentence)])[0] #tableau de probas

    for i in range(len(labels)):
        json[labels[i]]=np.round(pred_proba[i],2)
    return {"sentence": str(sentence), "pred":pred, "pred_proba":json}