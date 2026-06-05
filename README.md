# 🧠 Transcript Validation System

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)

---

## 📌 Overview

The **Transcript Validation System** is a preprocessing module designed to ensure that input transcripts are **clean, meaningful, and usable** before being passed to AI or evaluation systems.

It acts as a **quality control layer**, preventing invalid or noisy data from affecting downstream processes.

---

## 🎯 Key Features

* ✅ Detects **empty transcripts**
* 🔊 Identifies **noise-only inputs**
* ⚠️ Detects **malformed or corrupted text**
* 🌍 Handles **multilingual artifacts**
* ⚡ Fast and lightweight validation

---

##  System Architecture

```
Input Transcript
       ↓
Preprocessing Layer
       ↓
Validation Engine
       ↓
Decision Module
       ↓
Valid / Invalid Output
```

---

##  Validation Rules

| Type         | Description                | Example            |
| ------------ | -------------------------- | ------------------ |
| Empty        | No content                 | ""                 |
| Noise        | Repeated/random characters | "aaaaaa", "@@@###" |
| Malformed    | Broken encoding            | "���"              |
| Multilingual | Mixed languages            | "Hello नमस्ते"     |

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/transcript-validator.git
cd transcript-validator
pip install -r requirements.txt
```

---

##  Usage

```python
from src.validator import validate_transcript

result = validate_transcript("Hello world")
print(result)
```

---

## 📊 Example Output

```json
{
  "status": "Valid",
  "reason": "Clean Transcript"
}
```

---

🌐 API Usage 
from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, title="Transcript Validator API", version="1.0")

ns = api.namespace("validate", description="Validation operations")

input_model = api.model("Input", {
    "transcript": fields.String(required=True, description="Input text")
})

@ns.route("/")
class Validate(Resource):
    @ns.expect(input_model)
    def post(self):
        data = api.payload
        text = data.get("transcript", "")

        if text.strip() == "":
            result = {"status": "Invalid", "reason": "Empty transcript"}
        elif len(set(text)) == 1:
            result = {"status": "Invalid", "reason": "Noise-only text"}
        else:
            result = {"status": "Valid", "reason": "Looks good"}

        return result

if __name__ == "__main__":
    app.run(debug=True)
## 📁 Project Structure

```
transcript-validator/
│
├── src/
│   ├── validator.py
│   ├── checks.py
│
├── tests/
├── docs/
├── requirements.txt
├── README.md
└── app.py
```

---
 Test Cases

| Input         | Output    |
| ------------- | --------- |
| ""            | Invalid   |
| "aaaaaa"      | Noise     |
| "Hello world" | Valid     |
| "���"         | Malformed |

---

##  Future Improvements

* 🔹 ML-based noise detection
* 🔹 Confidence scoring
* 🔹 Real-time API deployment
* 🔹 Integration with AI pipelines

---

##  Author

**Mohit Raj**

---

## ⭐ Contribute

Contributions are welcome!
Feel free to fork, improve, and submit a pull request.

---

 License

This project is licensed under the MIT License.

