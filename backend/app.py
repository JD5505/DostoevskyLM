from fastapi import FastAPI
from Schema.user_input import UserInput
from Model.predict import generate_text
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/')
def home():
    return {'Message': "Hello, Welcome to Dostoevsky GRU RNN Model API"}

@app.post("/predict")
def user_input(data:UserInput):
    sentence = data.sentence
    temp = data.Temp
    total_words = data.total_words
    prediction = generate_text(sentence, total_words, temp)
    prediction = prediction.replace("\n", " ")
    
    return JSONResponse(status_code=200, content={'Prediction': prediction})
