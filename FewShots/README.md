# Few-Shot Bug Severity Classifier

## Overview

This project demonstrates **Few-Shot Prompt Engineering** using a locally running Llama model through Ollama.

The application classifies software bugs into severity levels by learning from multiple examples included in the prompt.

Unlike Zero-Shot or One-Shot Prompting, the AI receives several example bug reports along with their correct classifications before classifying the user's bug.

---

## Prompt Engineering Technique

### Few-Shot Prompting

Few-Shot Prompting provides the model with multiple examples before presenting the actual task.

The examples teach the AI:

- Severity categories
- Decision-making pattern
- Output format
- Reasoning style

The AI generalizes this pattern to classify new software bugs accurately.

---

## Severity Levels

- Critical
- High
- Medium
- Low

---

## Technologies Used

- Python
- Ollama
- Llama 3.2
- python-dotenv

---

## Installation

Install Ollama

```bash
ollama pull llama3.2
```

Install dependencies

```bash
pip install ollama python-dotenv
```

Run

```bash
python main.py
```

---

## Sample Input

The application freezes whenever a user tries to generate a PDF report.

---

## Sample Output

Severity:
High

Reason:
Generating reports is an important feature. Although the application does not completely crash, users cannot complete a major task.

---

## Folder Structure

```
FewShot_Bug_Severity_Classifier
│
├── main.py
├── .env
└── README.md
```

---

## Why Few-Shot?

This application is an ideal use case for Few-Shot Prompting because bug severity classification depends on understanding patterns rather than simple instructions.

By observing multiple correctly classified examples, the model learns how to distinguish between Critical, High, Medium, and Low severity issues and applies the same reasoning to unseen bug reports.

---

## Author

Prompt Engineering Assignment

Few-Shot Bug Severity Classifier









1. The mobile app freezes and must be force-closed whenever a user 
   tries to attach a photo to a message.

2. Clicking "Export Report" does nothing — no error, no download, 
   no response at all.

3. The dashboard chart colors don't match the company's brand guide 
   (using red instead of orange for warnings).

4. The word "recieve" is misspelled in the confirmation email template.
5. A user discovered that changing the "id" parameter in the URL lets 
   them view other users' order history, but it requires manually 
   editing the browser address bar.

6. Push notifications are delayed by 10-15 minutes during peak hours, 
   but eventually arrive correctly.

7. The checkout page works fine on Chrome and Firefox, but the "Place 
   Order" button doesn't respond on Safari — about 12% of users are on Safari.

8. After the recent update, deleted files reappear in the recycle bin 
   after 24 hours even though the user permanently deleted them.

9. The app doesn't crash, but repeatedly logs users out every 5 minutes, 
   forcing them to re-enter credentials constantly.

10. Admins can technically demote another admin to a regular user without 
    any confirmation prompt, and there's no audit log of who did it.
    11. The app is slow sometimes.

12. Something broke in the reports section after the last deploy.

13. Users are complaining about the search feature.
14. A rarely-used admin-only debug panel throws a full stack trace 
    error visible to the user, but it's only accessible internally 
    and not linked anywhere in the UI.

15. The payment succeeds and the order is placed correctly, but the 
    confirmation page shows the wrong order total (display only — 
    backend charge is correct).