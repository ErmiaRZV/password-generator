# 🔐 Password Generator (Python + Streamlit)

### 🔗 **Live Demo:**  
👉 https://password-generator-ghypz6onxezr5n5cur8wmu.streamlit.app/

An interactive **Password Generator** built with **Python OOP** and **Streamlit**.  
Generate secure PINs, random passwords, or memorable passwords using dictionary words.  

---

## 🚀 Features

- Object-oriented Python design  
- Generate **numeric PINs**, **random passwords**, or **memorable passwords**  
- Customizable options: digits, symbols, capitals, separators  
- Streamlit UI for interactive web experience  
- Real-time password generation  

---

## 📂 Project Structure

```
PasswordGenerator/
│
├── src/
│ ├── init.py # Marks src as a Python package
│ ├── main.py # Core password generator logic
│ └── run.py # Streamlit interactive UI
│
├── requirements.txt # Dependencies (Streamlit, nltk)
└── README.md # Project documentation
```

### Explanation of Files

- **src/** : Contains all Python source code  
- **main.py** : Password generator classes (PIN, Random, Memorable)  
- **run.py** : Streamlit interface for web app  
- **requirements.txt** : Python dependencies  
- **README.md** : Project documentation  

---

## 🖥️ Running the Streamlit App

### 1️⃣ Install dependencies
Make sure you have Python installed, then run:

```bash
pip install -r requirements.txt
⚠️ For Memorable Passwords, you also need NLTK words corpus:
import nltk
nltk.download('words')
```
## 2️⃣ Run the app
```
streamlit run src/run.py
```
## 📘 Documentation

### Classes (`main.py`)

#### `PasswordGenerator` (Abstract Base Class)
- `generate_password()` : abstract method to generate password

#### `pinGenerator`
- Generates numeric PIN  
- **Attribute:** `length` (default 4)  
- **Method:** `generate_password()` returns numeric PIN

#### `randomPasswordGenerator`
- Generates random password  
- **Options:** digits, symbols, capital letters  
- **Attributes:** `length`, `include_digits`, `include_symbols`, `include_capitals`  
- **Method:** `generate_password()` returns password string

#### `memorablePasswordGenerator`
- Generates password by joining dictionary words  
- **Options:** number of words, separator, include_upper  
- **Attributes:** `length`, `include_upper`, `separator`, `character` (list of words)  
- **Method:** `generate_password()` returns password string

### Streamlit (`run.py`)
- `st.radio` to select password type  
- `st.number_input` to select length / number of words  
- `st.checkbox` for options (digits, symbols, uppercase)  
- `st.text_input` for separator  
- `st.button` to generate password  
- `st.success` displays generated password

---

## 🛠 Future Improvements
- Add **password strength meter**  
- Add **history of generated passwords**  
- Add **copy to clipboard button**  
- Improve **UI styling** with Streamlit components  
- Add **unit tests** for generators  
- Deploy publicly on **Streamlit Cloud**

---

## 👤 Author
**Ermia Razavi**  

⭐ Star this project on GitHub and share your results!
