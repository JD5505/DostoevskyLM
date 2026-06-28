import numpy as np
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from Model.temperature import sample_with_temperature

MAX_INPUT_LEN = 99

model = load_model("Model/model.keras")
tokenizer = joblib.load("Tokenizer/tokenizer.pkl")


index_to_word = {idx: word for word, idx in tokenizer.word_index.items()}


def generate_text(seed_text, next_words=50, temperature=0.8, stop_on_endseq=True):
    seed_text = seed_text.lower()

    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=MAX_INPUT_LEN, padding="pre")

        preds = model.predict(token_list, verbose=0)[0]
        predicted_id = sample_with_temperature(preds, temperature)

        output_word = index_to_word.get(predicted_id, "")

        if output_word == "" :
            break
        if stop_on_endseq and output_word == "endseq":
            break

        seed_text += " " + output_word

    return seed_text


if __name__ == "__main__":
    seed = "after thinking for several minutes, he finally decided that"

    for temp in [0.3, 0.7, 1.0, 1.3, 1.7, 2.0]:
        print(f"\n--- temperature={temp} ---")
        print(generate_text(seed, next_words=40, temperature=temp))