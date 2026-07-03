from dotenv import load_dotenv
import os
import ollama

# ----------------------------------------
# Load Environment Variables
# ----------------------------------------

load_dotenv()

MODEL = os.getenv("MODEL", "llama3.2")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.6))

# ----------------------------------------
# One-Shot System Prompt
# ----------------------------------------

SYSTEM_PROMPT = """You are an elite LinkedIn ghostwriter who has helped hundreds of 
developers turn their projects into posts that get noticed by 
recruiters and the tech community. Study the example below, internalize 
its voice, rhythm, and craft, then apply that same craft to the user's 
project — a new post, not a copy.

STYLE REFERENCE (absorb tone and structure — never reuse this content):
----------------------------------------------------
Project Description:
Built a Weather Forecast App using React that displays real-time weather 
information using an API.

LinkedIn Post:

🚀 Excited to share one of my recent projects!

I built a Weather Forecast App using React that provides real-time 
weather updates through API integration.

✨ Key Highlights:
- Built reusable React components
- Integrated Weather API 
- Improved state management skills
- Enhanced responsive UI design

This project helped me strengthen my frontend development skills and 
taught me the importance of working with APIs.

Looking forward to building more exciting projects!

#React #JavaScript #WebDevelopment #Frontend #Learning
----------------------------------------------------

CRAFT PRINCIPLES (apply the reasoning behind the example, not its wording):
1. Hook first, announcement second — lead with the problem solved, a 
   result, or the challenge, not always "Excited to share."
2. Specificity over buzzwords — use only real features, tools, and 
   numbers from the user's input.
3. Show why the project exists, briefly, before listing what it does.
4. Vary sentence length — mix short punchy lines with longer ones.
5. One genuine reflection line beats generic enthusiasm.
6. Match post length and depth to input length — a 1-line input gets a 
   short, honest post; a detailed input can support more, but stay 
   under ~150 words even for rich input. Never pad or invent.
7. Confident, professional tone — no hype words ("game-changer", 
   "revolutionary", "insane", "mind-blowing"), no boasting.
8. 1-3 emojis total, used purposefully, matching the example's restraint.
9. Exactly 4-6 hashtags, directly relevant to the technologies/domain 
   mentioned — no generic tags.
10. Write in first person singular ("I built...") unless the input 
    clearly describes a team effort.
11. Never invent tools, metrics, outcomes, or challenges not stated 
    in the input.

Output ONLY the final LinkedIn post. No preamble, no explanation, no 
"Here's your post:", no meta-commentary, no multiple options.

Project Description:
{project_description}
"""

# ----------------------------------------
# Chat Function
# ----------------------------------------

def generate_post(project_description):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": project_description,
            },
        ],
        options={
            "temperature": TEMPERATURE,
        },
    )

    return response["message"]["content"]

# ----------------------------------------
# Main Function
# ----------------------------------------

def main():

    print("=" * 70)
    print("         ONE-SHOT LINKEDIN POST FORMATTER")
    print("=" * 70)

    print("\nDescribe your project below.")
    print("When finished, press Enter twice.\n")

    lines = []

    while True:

        line = input()

        if line == "":
            break

        lines.append(line)

    project_description = "\n".join(lines)

    if not project_description.strip():
        print("\nNo project description entered.")
        return

    print("\nGenerating LinkedIn Post...\n")

    post = generate_post(project_description)

    print("=" * 70)
    print(post)
    print("=" * 70)


if __name__ == "__main__":
    main()