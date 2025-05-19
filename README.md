# 🌐 Lingua Franca

**Lingua Franca** is a simple and elegant web-based translation tool built with **Flask** and powered by the **Google Translate API**.  
It allows users to translate text between multiple languages, automatically detect the source language, and enjoy a visually engaging interface inspired by the aesthetics of *The Matrix*.

---

## 🧠 Project Context

This project was developed as part of a programming course at [La Plateforme_], with the objective of learning how to:
- Interact with external APIs in Python
- Build a web application using Flask
- Create a functional and user-friendly interface

---

## ✨ Features

- 📝 Text translation from a source to a target language
- 🌍 Automatic language detection (if the source language is unknown)
- 🎨 Dark theme with Matrix-style design and animated background
- ⌨️ "Live typing" animation for translated text
- ✅ Simple, responsive, and intuitive layout

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, googletrans (unofficial Google Translate API)
- **Frontend**: HTML, CSS, JavaScript
- **Templating**: Jinja2
- **Versioning**: Git & GitHub

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/lingua-franca.git
cd lingua-franca

## Virtual Environnement

python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

## Install Dependancies

pip install -r requirements.txt
Make sure to use googletrans==4.0.0-rc1 for compatibility.

## Run the App
python app.py
Then open your browser at http://127.0.0.1:5000.

## Improvements & Future Ideas
Add light/dark mode toggle

Enable real-time translation (AJAX)

Save translation history

Integrate official Google Cloud Translate API

Add voice input or text-to-speech
