# 🌸 HerHealth AI

> An AI-powered women's health companion built with Python, Google Gemini API, and Gradio.

## 🚀 Live Demo

👉 https://herhealth-ai.onrender.com

## 📌 About the Project

HerHealth AI is an educational women's health companion designed to provide simple, accessible information and basic wellness tools through an interactive web interface.

The project combines Generative AI with traditional Python programming to create multiple useful features in one application.

## ✨ Features

### 🤖 AI Health Assistant

Users can ask general women's health questions and receive easy-to-understand educational responses powered by Google Gemini.

### 📅 Period Tracker

A Python-based period tracking feature that calculates an estimated next period based on:

- Last period date
- Menstrual cycle length

This feature demonstrates date handling and calculations using Python.

### 🥗 Lifestyle Planner

Users can enter:

- Age
- Height
- Weight

The application generates a general lifestyle plan to encourage healthy habits.

## 🛠️ Technologies Used

- Python
- Google Gemini API
- Gradio
- Pandas
- Python Datetime
- HTML/CSS through Gradio
- Render
- GitHub

## 🧠 AI Integration

The AI Health Assistant uses the Google Gemini API to generate educational responses.

The application is designed to provide general information and does not replace professional medical advice.

## 📂 Project Structure

```text
HerHealth-AI/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```




## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/bhawna4424-sudo/HerHealth-AI.git
cd HerHealth-AI
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your Gemini API Key

Set your Gemini API key as an environment variable.

**Windows Command Prompt:**

```cmd
set GEMINI_API_KEY=your_api_key_here
```

**Windows PowerShell:**

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

**Linux / macOS:**

```bash
export GEMINI_API_KEY="your_api_key_here"
```

⚠️ **Never upload your actual Gemini API key to GitHub.**

### 4. Run the Application

```bash
python app.py
```

The Gradio application will start and provide a local web interface.
