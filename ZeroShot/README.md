# Zero-Shot Meeting Notes Summarizer

## Overview

This project demonstrates the use of **Zero-Shot Prompt Engineering** using a locally running Llama model through Ollama.

The application converts raw meeting notes into a structured and professional meeting summary without providing the AI with any examples.

Instead, the model receives only clear instructions through a carefully designed system prompt.

---

## Prompt Engineering Technique

### Zero-Shot Prompting

Zero-shot prompting means the model is given only instructions.

No examples are provided.

The model relies entirely on its pre-trained knowledge and the developer's prompt to complete the task.

This application uses zero-shot prompting because meeting summarization is a common task that can be performed accurately using only well-written instructions.

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

### Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
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

Today's meeting focused on launching the college website.

Rahul will complete the frontend.

Sneha will deploy the backend.

Testing begins Friday.

Final deadline is Monday.

Client requested dark mode.

---

## Sample Output

Meeting Summary

Topic:
College Website Launch

Key Discussion Points

- Launch preparation reviewed
- Frontend and backend responsibilities assigned

Decisions Made

- Testing starts Friday
- Dark mode will be included

Action Items

- Rahul → Complete frontend
- Sneha → Deploy backend

Timeline / Deadlines

- Testing: Friday
- Deadline: Monday

Additional Notes

- Client requested dark mode

---

## Folder Structure

```
ZeroShot_Meeting_Notes_Summarizer
│
├── main.py
├── .env
└── README.md
```

---

## Author

Prompt Engineering Assignment

Zero-Shot Meeting Notes Summarizer



Quarterly Product Roadmap Review
Date: June 29, 2026
Attendees: Karan (Head of Product), Neha (Engineering Lead), Vikram (Design Lead), Alisha (Customer Success), Farhan (Data Analytics), Ritu (Marketing)
Karan opened the meeting by summarizing the current state of the product. He mentioned that user growth has been steady at around 8 percent month over month, but churn has ticked up slightly in the last two months, from 4.1 percent to 5.3 percent. He said this needs to be a top priority for the next quarter.
Neha gave an engineering update. The new API gateway migration is 90 percent complete, with full rollout expected by July 15th. She flagged that two legacy services still depend on the old authentication system and migrating them will take an additional two weeks. She requested that QA be looped in earlier this time to avoid the regression issues seen during the last migration in March.
Vikram presented the redesigned onboarding flow. Early usability testing with 12 users showed a 40 percent improvement in time to first value, meaning users reach their first meaningful action much faster than before. However, three of the twelve testers got confused by the new permissions screen, so Vikram proposed simplifying it further before the wider rollout. He asked for one more week to iterate before handing it off to engineering.
Alisha shared feedback directly from customer support tickets. The most common complaint over the last month was around slow load times on the dashboard page, mentioned in approximately 34 support tickets. She also noted that several enterprise customers have asked about SSO support, which is currently not available on the platform. She suggested this could be a blocker for closing at least two deals currently in the pipeline.
Farhan presented data on the churn increase Karan mentioned earlier. His analysis showed that churn is concentrated almost entirely among users who signed up through the free trial and did not complete onboarding within the first three days. Users who completed onboarding within three days had a churn rate of only 2.1 percent, compared to 11.8 percent for those who did not. This strongly suggests the onboarding flow Vikram is working on could directly address the churn problem, not just improve activation metrics.
Ritu gave a marketing update. The current quarter campaign generated 1200 new trial signups, exceeding the target of 900. However, she noted that the cost per acquisition has increased by 18 percent compared to last quarter, mainly due to rising ad costs on paid social channels. She proposed testing a referral program as a lower cost acquisition channel for next quarter and asked for engineering support to build a basic referral tracking feature.
Karan then opened the floor for prioritization discussion. There was some disagreement between Neha and Vikram about sequencing. Neha argued the legacy authentication migration should be completed first since it is a technical risk that grows the longer it is delayed. Vikram argued the onboarding redesign should be prioritized first given the direct link Farhan found between onboarding completion and churn. After some discussion, the group agreed that both could proceed in parallel since they do not share engineering resources, but agreed the onboarding project would get priority if any resource conflicts arise.
The SSO feature request from Alisha was discussed next. Neha estimated it would take approximately six weeks of engineering time to build a basic SSO integration supporting common providers like Okta and Azure AD. Karan asked Alisha to get more specific details from the two enterprise prospects about which SSO provider they specifically require before committing engineering time, since building for the wrong provider first could waste effort.
Ritu's referral program proposal was tabled for now due to limited engineering bandwidth this quarter, but Karan asked her to prepare a detailed proposal including estimated cost savings so it can be considered as a priority for next quarter's planning.
Toward the end of the meeting, Karan raised a concern about the upcoming board meeting on July 20th, where he will need to present updated growth and retention numbers. He asked Farhan to prepare a dashboard with the latest churn and activation metrics by July 10th so there is time to review before the board presentation.
Action items were then summarized. Neha will complete the API gateway migration by July 15th and provide a revised timeline for the legacy authentication migration by next Monday. Vikram will finalize the simplified permissions screen within one week and then hand off the onboarding flow to engineering. Alisha will follow up with the two enterprise prospects to gather specific SSO provider requirements by July 8th. Farhan will prepare the churn and activation dashboard for the board meeting by July 10th. Ritu will prepare a detailed referral program proposal for consideration in next quarter's planning, no fixed deadline given.
Karan closed the meeting by reiterating that reducing churn is the top priority for the quarter and that the onboarding redesign and authentication migration should both be treated as high priority workstreams. He scheduled a follow up check-in for July 8th to review progress on the SSO requirements gathering and permissions screen simplification.