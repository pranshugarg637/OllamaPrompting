from dotenv import load_dotenv #dotenv helps to store important and sensitive documents in a seperate file called .env file 
import os #used to read content from the .env file
import ollama 

# ----------------------------------------
# Load Environment Variables
# ----------------------------------------

load_dotenv() #checks if there is any .env file and then loads its key value pairs into the python virtual environment
MODEL = os.getenv("MODEL", "llama3.2") #look for model and if not found then by default add llama3.2
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.3))

# ----------------------------------------
# Zero-Shot System Prompt
# ----------------------------------------

SYSTEM_PROMPT = """You are a Meeting Notes Summarizer. Your only job is to convert raw, unstructured meeting notes into a clean, structured summary.

RULES (follow strictly):
1. Use ONLY information present in the notes. Never invent, assume, or add anything not explicitly stated.
2. If a section has no relevant information, write "None mentioned" under it. Do not skip or omit sections.
3. Do not repeat the same point in multiple sections.
4. Keep language concise and professional. No opinions, no commentary, no extra explanation outside the format.
5. If speaker names are given, attribute decisions and action items to them. If no name is given for an action item, write "Unassigned".
6. Preserve all deadlines, dates, and numbers exactly as written in the notes. Do not reformat or guess dates.
7. If the notes are messy, informal, or use shorthand, still extract the meaning accurately without changing the facts.
8. Output ONLY the summary in the exact format below. Do not add greetings, explanations, or notes about your process.

OUTPUT FORMAT (use exactly this structure, including headers and dashes):

Meeting Summary
---------------
Topic:
<one-line topic of the meeting>

Key Discussion Points:
- <point 1>
- <point 2>

Decisions Made:
- <decision 1>
- <decision 2>

Action Items:
- <Person> → <Task> (Deadline: <date or "None">)

Timeline / Deadlines:
- <deadline or milestone>

Additional Notes:
- <anything important that doesn't fit above, e.g. risks, concerns, unresolved issues>

If a category has nothing relevant, write "None mentioned" instead of leaving it blank or omitting it."""

# ----------------------------------------
# Chat Function
# ----------------------------------------

def summarize_notes(notes):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": notes,
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

    print("=" * 65)
    print("      ZERO-SHOT MEETING NOTES SUMMARIZER")
    print("=" * 65)

    print("\nPaste your meeting notes below.")
    print("When finished, press Enter twice.\n")

    lines = []

    while True:

        line = input()

        if line == "":
            break

        lines.append(line)

    meeting_notes = "\n".join(lines) #list ke har ek element ko join with next line between 2

    if not meeting_notes.strip():
        print("\nNo meeting notes were entered.")
        return

    print("\nGenerating professional summary...\n")

    summary = summarize_notes(meeting_notes)

    print("=" * 65)
    print(summary)
    print("=" * 65)


if __name__ == "__main__":
    main()     
#Every Python file, when it runs, automatically gets a built-in variable called __name__. Python sets its value depending on how the file is being used:
#If you run the file directly (e.g., python main.py in your terminal), Python sets __name__ = "__main__".

