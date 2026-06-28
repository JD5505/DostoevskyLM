import streamlit as st
import requests

API_URL = "https://p01--dostoevskylm--vgrjx29d46vq.code.run/predict"

st.set_page_config(
    page_title="Dostoevsky Language Model",
    page_icon="📚",
    layout="wide"
)

st.title("Dostoevsky Language Model")
st.markdown("""# 📖 Dostoevsky GRU

*A GRU-based language model trained on the works of Fyodor Dostoevsky.*

Enter a starting phrase below, and the model will predict the next words to generate text in a style inspired by Dostoevsky's novels.

### Features
- 🧠 GRU Recurrent Neural Network
- 📚 Trained on Dostoevsky's literary works
- 🌡️ Adjustable temperature for creativity
- ⚡ Powered by a FastAPI backend

---

### How to Use
1. Enter a prompt (e.g., **"The old man looked"**).
2. Choose a temperature value.
3. Select the number of words to generate.
4. Click **Generate**.
5. Read the generated continuation.

---

> **Note:** This model is trained to imitate writing style, not historical facts. Generated text may contain grammatical inconsistencies or fictional content.
            
---            
                        """)

sentence = st.text_area("Enter any Half-Sentence:")
max_words = st.number_input("Enter Maximum number of Words:", min_value=5, max_value=100)

st.markdown("""
### 🌡️ Temperature

The **temperature** controls how creative or predictable the generated text is.

- **0%** → Extremely deterministic. The model almost always picks the most likely next word, resulting in repetitive but coherent text.
- **100%** → Default behavior. A balanced mix of coherence and creativity.
- **200%** → Maximum randomness. The output becomes highly creative but may lose grammatical structure and coherence.

> **Tip:** For the best balance between readability and creativity, try values between **70%** and **130%**.
""")

temperature = temperature = st.slider(
                                        "🌡️ Temperature (%)",
                                        min_value=0,
                                        max_value=200,
                                        value=100,
                                        step=5,
                                        help="100% is the default. Lower values produce more predictable text, while higher values increase creativity."
                                    )

if st.button("Enter"):
    input_dict = {
        "sentence": sentence, 
        "total_words": max_words,
        "temp":temperature
    }

    try:
        response = requests.post(API_URL, json=input_dict)
        if response.status_code == 200:
            result = response.json()
            st.success(result['Prediction'])        
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI Server")




