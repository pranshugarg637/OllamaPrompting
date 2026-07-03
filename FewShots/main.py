from dotenv import load_dotenv
import os
import ollama

# ----------------------------------------
# Load Environment Variables
# ----------------------------------------

load_dotenv()

MODEL = os.getenv("MODEL", "llama3.2")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.2))

# ----------------------------------------
# Few-Shot System Prompt
# ----------------------------------------

SYSTEM_PROMPT = """
You are an expert Software Quality Assurance Engineer.

Your task is to classify software bugs into one of these severity levels:
Critical, High, Medium, or Low.

Severity Definitions

Critical
- Application crashes completely / becomes unusable
- Data loss or corruption
- Security vulnerability with significant impact (data exposure, unauthorized access)
- No workaround exists and the issue blocks all users

High
- Major functionality is broken or a key feature is unavailable
- Affects many users but the app itself is still usable
- Workaround is difficult, unofficial, or partial

Medium
- Core functionality still works
- User experience is noticeably affected
- A reasonable workaround exists

Low
- Cosmetic issues (UI misalignment, color, spacing)
- Typographical or minor text errors
- No impact on functionality or user experience

Classification Rules
- If a bug seems to fit two categories, choose the HIGHER severity only 
  if user impact or data/security risk is significant; otherwise choose 
  the lower one.
- If the bug report is vague or missing detail, state your assumption 
  in the Reason before giving the severity.
- Judge based on user impact and workaround availability — not just 
  keywords like "crash" or "security."

Learn the classification pattern from the following examples.

-----------------------------------------
Example 1
Bug: The application crashes immediately after login for every user.
Severity: Critical
Reason: Users cannot access the application at all — a complete blocker 
with no workaround.

-----------------------------------------
Example 2
Bug: SQL Injection allows attackers to access customer data.
Severity: Critical
Reason: Severe security vulnerability exposing sensitive data, regardless 
of whether the app itself still functions normally.

-----------------------------------------
Example 3
Bug: Users cannot upload assignment files.
Severity: High
Reason: A major feature is unavailable, but the rest of the application 
remains usable — no full blocker, but no workaround either.

-----------------------------------------
Example 4
Bug: Users can view another user's email address by inspecting page 
source, but no other data is exposed and exploitation requires technical knowledge.
Severity: Medium
Reason: This is a minor information leak — real but limited impact, and 
not easily exploitable by average users, so it doesn't meet the bar for 
Critical/High despite being security-related.

-----------------------------------------
Example 5
Bug: The profile picture updates only after refreshing the page.
Severity: Medium
Reason: The feature works eventually; the user experience is affected 
but there's an easy workaround (manual refresh).

-----------------------------------------
Example 6
Bug: The "Forgot Password" button is slightly misaligned on mobile devices.
Severity: Low
Reason: Purely visual issue with no functional impact.

-----------------------------------------
Example 7
Bug: The About page contains the word "Welcom" instead of "Welcome".
Severity: Low
Reason: Spelling mistake with no functional impact.

-----------------------------------------

Now classify the user's bug.

If the report lacks detail, note your assumption first.

Follow exactly this format:

Severity:
<Severity>

Reason:
<Short explanation, referencing user impact and workaround availability>

Bug:
{bug_report}
"""

# ----------------------------------------
# Chat Function
# ----------------------------------------

def classify_bug(bug):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": bug,
            },
        ],
        options={
            "temperature": TEMPERATURE,
        },
    )

    return response["message"]["content"]

# ----------------------------------------
# Main
# ----------------------------------------

def main():

    print("=" * 70)
    print("        FEW-SHOT BUG SEVERITY CLASSIFIER")
    print("=" * 70)

    print("\nDescribe the software bug below.")
    print("When finished, press Enter twice.\n")

    lines = []

    while True:

        line = input()

        if line == "":
            break

        lines.append(line)

    bug = "\n".join(lines)

    if not bug.strip():
        print("\nNo bug description entered.")
        return

    print("\nClassifying Bug...\n")

    result = classify_bug(bug)

    print("=" * 70)
    print(result)
    print("=" * 70)


if __name__ == "__main__":
    main()