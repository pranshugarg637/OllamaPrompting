# One-Shot LinkedIn Post Formatter

## Overview

This project demonstrates **One-Shot Prompt Engineering** using a locally running Llama model through Ollama.

The application converts a simple project description into a professional LinkedIn post.

Unlike Zero-Shot Prompting, this application provides **one example** to teach the AI the desired writing style before asking it to generate the actual post.

---

## Prompt Engineering Technique

### One-Shot Prompting

One-Shot Prompting provides the AI with a single example of the desired input and output.

The example teaches the model:

- Writing style
- Tone
- Formatting
- Structure

The AI then follows the same pattern for a completely different project.

---

## Technologies Used

- Python
- Ollama
- Llama 3.2
- python-dotenv

---

## Installation

### Install Ollama

Download Ollama:

https://ollama.com/download

Pull the model:

```bash
ollama pull llama3.2
```

---

### Install Dependencies

```bash
pip install ollama python-dotenv
```

---

## Run

```bash
python main.py
```

---

## Sample Input

Built a local AI chatbot using Python and Ollama.

The chatbot demonstrates six Prompt Engineering techniques including Zero-Shot, One-Shot, Few-Shot, ReAct, Chain-of-Thought and AI Skills.

It allows users to select a prompting method and ask questions using the Llama 3.2 model running locally.

---

## Sample Output

🚀 Excited to share one of my recent AI projects!

I built a Local AI Chatbot using Python and Ollama that demonstrates multiple Prompt Engineering techniques while running completely offline.

✨ Key Highlights:

• Integrated Ollama with Python
• Implemented six Prompt Engineering methods
• Used Llama 3.2 locally
• Created an interactive terminal chatbot

This project strengthened my understanding of Prompt Engineering and local Large Language Models.

Looking forward to exploring more AI applications!

#Python #AI #Ollama #LLM #PromptEngineering #MachineLearning

---

## Folder Structure

```
OneShot_LinkedIn_Post_Formatter
│
├── main.py
├── .env
└── README.md
```

---

## Author

Prompt Engineering Assignment

One-Shot LinkedIn Post Formatter











Built a Zero-Shot Meeting Notes Summarizer using Python and Ollama that runs entirely on a local LLM (Llama 3.2) without any external API calls or internet dependency. The tool takes raw, unstructured meeting notes as input through the terminal and uses a carefully engineered zero-shot system prompt to convert them into a clean, structured summary. The output includes sections for key discussion points, decisions made, action items with assigned owners, deadlines, and additional notes. I used python-dotenv to manage configuration like model selection and temperature settings, keeping the code environment-agnostic and easy to reconfigure. One of the biggest challenges was designing a system prompt that could reliably handle messy, informal notes without hallucinating information that wasn't actually said in the meeting. I iterated on the prompt several times, adding explicit fallback rules for missing sections and unassigned action items, which significantly improved consistency across different types of meeting notes. This project deepened my understanding of prompt engineering, local LLM deployment, and how much output quality depends on how clearly instructions are structured rather than just the model itself.





Made a to-do list app with React.


Built a full-stack expense tracker using React, Node.js, Express, and 
MongoDB. Users can add transactions, categorize them, and view monthly 
spending trends on a chart built with Chart.js. Implemented JWT-based 
authentication and reduced average page load time by 40% by lazy-loading 
components. Deployed on Render with CI/CD via GitHub Actions. Took about 
3 weeks, mostly solo, with one friend helping on the UI.




Built a machine learning model in Python using scikit-learn to predict 
house prices based on a Kaggle dataset. Used feature engineering and 
cross-validation, and got the model to 89% accuracy (R² score).



My team of 3 built a hackathon project — a Chrome extension that 
summarizes long articles using the OpenAI API. We won 2nd place out 
of 40 teams. Built with vanilla JS and the Chrome Extensions API.