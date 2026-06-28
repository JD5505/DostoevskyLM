# 📖 DostoGRU

A **GRU-based neural language model** trained on the literary works of **Fyodor Dostoevsky**. Given an input prompt, the model predicts subsequent words to generate text inspired by Dostoevsky's writing style.

The project consists of:

* **TensorFlow/Keras** language model
* **FastAPI** backend for inference
* **Streamlit** frontend for an interactive interface

---

## Features

* 🧠 Word-level language modeling using GRU
* 📚 Trained on Dostoevsky's novels
* 🌡️ Adjustable temperature sampling (0% - 200%)
* ⚡ FastAPI REST API
* 🎨 Interactive Streamlit frontend

---

## Project Structure

```text
DostoevskyLM/
│
├── backend/
│   ├── app.py
│   ├── Model/
│   │   ├── model.keras
│   │   ├── predict.py
│   │   ├── temperature.py
│   │   ├── fyodor.txt
│   │   └── model_training.ipynb
│   │
│   ├── Schema/
│   │   └── user_input.py
│   │
│   └── Tokenizer/
│
├── frontend/
│   └── index.py
│
├── requirements.txt
└── README.md
```

---

## Model Architecture

| Layer           | Output Shape        |
| --------------- | ------------------- |
| Embedding       | (99, 100)           |
| GRU (256 units) | (99, 256)           |
| GRU (256 units) | (256)               |
| Dropout         | (256)               |
| Dense           | (10,000 vocabulary) |

### Statistics

* Vocabulary Size: **10,000**
* Embedding Dimension: **100**
* Sequence Length: **99**
* GRU Units: **256 × 2**
* Total Parameters: **12.7 Million**
* Trainable Parameters: **4.24 Million**

---

## Temperature Sampling

The model supports temperature values from **0% to 200%**.

| Temperature | Behavior                                    |
| ----------- | ------------------------------------------- |
| **0%**      | Deterministic and repetitive                |
| **50%**     | Conservative predictions                    |
| **100%**    | Default balance of coherence and creativity |
| **150%**    | More creative with occasional mistakes      |
| **200%**    | Highly random and experimental              |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/JD5505/DostoevskyLM.git
cd DostoevskyLM
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Backend

Navigate to the backend folder:

```bash
cd backend
```

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

Open another terminal:

```bash
cd frontend
streamlit run index.py
```

---

## Example

**Prompt**

```
After thinking for several minutes,
```

**Generated Output**

```
After thinking for several minutes, he finally decided that he could not understand what had happened and quietly walked away.
```

---

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* FastAPI
* Streamlit
* Pydantic

---

## Future Improvements

* Beam Search decoding
* Top-k sampling
* Top-p (Nucleus) sampling
* Transformer-based language model
* Docker deployment
* Hugging Face deployment
* Better text preprocessing
* Larger training corpus

---

## Disclaimer

This project is intended for educational purposes. The generated text imitates the statistical writing style learned from the training corpus and does not reproduce the reasoning, opinions, or intent of Fyodor Dostoevsky.
