# Chain-of-Thought Loan EMI Explanation Assistant

## Overview

This project demonstrates **Chain-of-Thought (CoT) Prompt Engineering** using a locally running Llama model through Ollama.

The application calculates the Equated Monthly Installment (EMI) for a loan and explains the calculation through a structured, step-by-step reasoning process.

Instead of directly providing the EMI amount, the AI performs intermediate calculations and explains how the final value is obtained.

---

# Prompt Engineering Technique

## Chain-of-Thought Prompting

Chain-of-Thought Prompting encourages the language model to solve a problem by reasoning through multiple intermediate steps before arriving at the final answer.

Instead of generating only the final output, the model:

- Understands the problem
- Identifies required values
- Performs intermediate calculations
- Applies the EMI formula
- Computes the total payment
- Computes the total interest
- Explains the result in simple language

This improves transparency and makes complex calculations easier to understand.

---

# Application

The application accepts basic loan information such as:

- Loan Amount
- Annual Interest Rate
- Loan Tenure

The AI then calculates:

- Monthly EMI
- Total Payment
- Total Interest

along with a detailed explanation of each calculation step.

---

# Technologies Used

- Python
- Ollama
- Llama 3.2
- python-dotenv

---

# Installation

## Install Ollama

Download Ollama:

https://ollama.com/download

Pull the required model:

```bash
ollama pull llama3.2
```

---

## Install Dependencies

```bash
pip install ollama python-dotenv
```

---

# Run

```bash
python main.py
```

---

# Sample Input

```
Loan Amount: ₹500000

Interest Rate: 8.5%

Loan Tenure: 5 years
```

---

# Sample Output

```
Thought

The loan amount, annual interest rate, and tenure are available.

Step 1

Principal = ₹500000

Annual Interest Rate = 8.5%

Loan Tenure = 5 Years

Step 2

Monthly Interest Rate = 8.5 ÷ (12 × 100)

Loan Tenure = 60 Months

Step 3

Apply EMI Formula

EMI = ₹10,258.64

Step 4

Total Payment = ₹615,518.40

Step 5

Total Interest = ₹115,518.40

Final Answer

Loan Summary

Loan Amount:
₹500000

Interest Rate:
8.5%

Loan Tenure:
5 Years

Monthly EMI:
₹10,258.64

Total Payment:
₹615,518.40

Total Interest:
₹115,518.40

Explanation:
The EMI is calculated using the standard EMI formula based on the principal amount, monthly interest rate, and repayment duration.

Disclaimer:
This EMI is only an estimate.
```

---

# Folder Structure

```
ChainOfThought_Loan_EMI_Assistant
│
├── main.py
├── .env
└── README.md
```

---

# Why Chain-of-Thought?

EMI calculation involves multiple mathematical steps.

Instead of directly producing the answer, Chain-of-Thought Prompting encourages the AI to:

- Understand the loan details
- Convert values where necessary
- Apply the EMI formula
- Calculate the monthly installment
- Compute the total payment
- Compute the total interest
- Explain every step before presenting the final result

This makes the solution easier to understand and verify.

---

# Features

- Calculates Monthly EMI
- Calculates Total Payment
- Calculates Total Interest
- Explains each calculation step
- Uses the standard EMI formula
- Accepts flexible loan details
- Runs completely offline using Ollama

---

# Learning Outcomes

This project demonstrates:

- Chain-of-Thought Prompt Engineering
- Mathematical reasoning using LLMs
- Step-by-step problem solving
- Local LLM integration using Ollama
- Python integration with Generative AI

---

# Author

Prompt Engineering Assignment

Chain-of-Thought Loan EMI Explanation Assistant









Loan Amount: ₹10,00,000
Annual Interest Rate: 8.5%
Loan Tenure: 20 years




Loan Amount: ₹5,00,000
Annual Interest Rate: 12%
Loan Tenure: 36 months




Loan Amount: ₹1,50,000
Annual Interest Rate: 18%
Loan Tenure: 1 year





Loan Amount: ₹2,00,000
Annual Interest Rate: 0%
Loan Tenure: 5 years






Loan Amount: ₹75,00,000
Annual Interest Rate: 7.2%
Loan Tenure: 30 years