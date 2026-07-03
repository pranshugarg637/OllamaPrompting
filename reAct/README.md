# ReAct Course Recommendation Assistant

## Overview

This project demonstrates the use of **ReAct (Reasoning + Acting) Prompt Engineering** using a locally running Llama model through Ollama.

The application acts as an intelligent **Course Recommendation Assistant**. Instead of recommending courses immediately, it follows the ReAct prompting pattern by reasoning about the student's profile, evaluating multiple candidate courses one by one, rejecting weaker options, and finally recommending the most suitable courses.

The goal is to simulate a thoughtful decision-making process similar to how a career counselor would recommend courses.

---

# Prompt Engineering Technique

## ReAct (Reasoning + Acting)

ReAct combines **Reasoning** and **Acting**.

Instead of producing an answer immediately, the AI repeatedly:

- Thinks about the problem
- Takes an action
- Observes the result
- Refines its reasoning

This cycle continues until the AI has enough information to confidently produce the final answer.

The workflow follows this pattern:

```
Thought
↓

Action

↓

Observation

↓

Thought

↓

Action

↓

Observation

↓

Final Answer
```

Unlike Zero-Shot or Few-Shot prompting, ReAct encourages the model to evaluate multiple possibilities before making a recommendation.

---

# Application

The application recommends the most suitable courses based on a student's profile.

The student may provide information such as:

- Current education
- Skills
- Interests
- Career goals
- Experience level
- Preferred learning style

The AI then:

- Analyzes the student's profile
- Considers multiple candidate courses
- Evaluates each candidate
- Rejects weaker options
- Selects the best three recommendations

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

# Run the Application

```bash
python main.py
```

---

# Sample Input

```
I am a second-year Computer Science student.

I know Python and basic C++.

I enjoy solving programming problems and building web applications.

My career goal is to become an AI Engineer.

I prefer project-based learning.

I have completed basic Machine Learning and want to learn more advanced AI topics.
```

---

# Sample Output

```
Thought 1:
The student has a Computer Science background with basic programming knowledge and an interest in Artificial Intelligence.

Action 1:
Propose candidate course:
Machine Learning Specialization

Observation 1:
Strong fit because it builds directly on the student's existing knowledge.

...

Final Answer

Recommended Courses

1. Machine Learning Specialization

Reason:
Builds a strong AI foundation.

Suitable For:
Intermediate learners interested in AI.

Skills You Will Learn:
• Supervised Learning
• Model Evaluation
• Regression
• Classification

Career Opportunities:
• Machine Learning Engineer
• AI Engineer

...

Courses Considered but Not Recommended

• Frontend Web Development
Reason:
Does not closely align with the student's AI career goal.
```

---

# Folder Structure

```
ReAct_Course_Recommendation_Assistant
│
├── main.py
├── .env
└── README.md
```

---

# Why ReAct Prompting?

Course recommendation is a decision-making problem rather than a simple question-answer task.

A good recommendation requires evaluating several possible courses before selecting the most suitable ones.

ReAct Prompting makes this process transparent by allowing the model to:

- Analyze the student's profile
- Consider multiple candidate courses
- Evaluate each option
- Reject unsuitable courses
- Justify the final recommendations

This produces recommendations that are more structured, explainable, and easier to understand than directly listing courses.

---

# Features

- Accepts a student's profile as input
- Evaluates multiple candidate courses
- Uses Thought → Action → Observation cycles
- Provides the top three course recommendations
- Explains why each course was selected
- Rejects less suitable options with reasons
- Suggests certifications, projects, and internship ideas
- Runs completely offline using Ollama and Llama 3.2

---

# Learning Outcomes

This project demonstrates:

- ReAct Prompt Engineering
- Structured AI reasoning
- Decision-making with Large Language Models
- Local LLM integration using Ollama
- Python integration with Generative AI

---

# Author

Prompt Engineering Assignment

ReAct Course Recommendation Assistant




Age: 22
Education: B.Tech in Computer Science
Interests: Solving logical problems, building things end-to-end
Skills: Strong in Python, data structures, some ML exposure
Personality: Enjoys independent deep-focus work, dislikes large meetings
Work-style: Prefers small teams, remote-friendly




Age: 24
Education: B.Com graduate
Interests: Passionate about becoming a Data Scientist, watches ML videos for fun
Skills: No programming background, strong in Excel and basic statistics only
Personality: Patient, detail-oriented, doesn't mind slow, methodical work
Work-style: Comfortable with long-term self-study





Age: 26
Education: MBA, Finance specialization
Skills: Excellent at financial modeling and valuation (top of class, 2 
years experience as a financial analyst)
Interests: Says finance work "pays well but feels boring," genuinely 
excited about teaching and mentoring others
Personality: Outgoing, enjoys explaining concepts, patient with beginners
Work-style: Prefers people-facing roles over solo analytical work






Age: 21
Education: 3rd year Marketing student
Interests: Loves brand strategy and advertising, follows major ad 
campaigns closely
Skills: Good at writing, creative thinking
Personality: Severe discomfort with public speaking and client-facing 
presentations, prefers working behind the scenes
Work-style: Wants to avoid pitching or client meetings entirely







Age: 25
Education: Engineering graduate
Interests: Enjoys both deep technical problem-solving AND leading/
motivating a team
Skills: Strong technical skills (backend development), some experience 
leading a small project team
Personality: Introverted in large groups but comfortable and confident 
leading a small, familiar team
Work-style: Wants growth but doesn't want to fully leave hands-on 
technical work