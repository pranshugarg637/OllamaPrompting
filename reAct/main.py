from dotenv import load_dotenv
import os
import ollama

# ----------------------------------------
# Load Environment Variables
# ----------------------------------------

load_dotenv()

MODEL = os.getenv("MODEL", "llama3.2")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.4))

# ----------------------------------------
# ReAct System Prompt
# ----------------------------------------

SYSTEM_PROMPT = """
You are an intelligent Course Recommendation Assistant.

Your task is to analyze the student's information and recommend the most suitable courses.

Instructions:
- Carefully analyze the student's interests, skills, education level, career goals, and preferred learning style.
- Think step by step before making recommendations.
- Recommend only courses that match the student's profile.
- Explain why each course is recommended.
- Mention the expected career opportunities after completing each course.
- If the student's information is incomplete, state what assumptions are being made.
- End with a helpful disclaimer.

Format:

Thought:
Analyze the student's profile step by step.

Action:
Identify important factors such as:
- Interests
- Skills
- Educational Background
- Career Goals
- Experience Level
- Preferred Learning Mode (Online/Offline)
- Course Duration Preference

Observation:
Summarize the evidence from the student's information.

Repeat Thought/Action/Observation if needed.

Final Answer:

Recommended Courses:

1.
Course Name:
Reason:
Suitable For:
Skills You Will Learn:
Career Opportunities:

2.
Course Name:
Reason:
Suitable For:
Skills You Will Learn:
Career Opportunities:

3.
Course Name:
Reason:
Suitable For:
Skills You Will Learn:
Career Opportunities:

Additional Suggestions:
- Certifications to consider
- Learning resources
- Projects to build
- Internship ideas

Disclaimer:
These recommendations are based only on the information provided by the student. Final course selection should consider individual interests, budget, institution quality, and career objectives.

Student Profile:
{student_profile}
"""

# ----------------------------------------
# Chat Function
# ----------------------------------------

def recommend_courses(student_profile):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": student_profile,
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
    print("      ReAct COURSE RECOMMENDATION ASSISTANT")
    print("=" * 70)

    print("\nEnter the student's profile.")
    print("Include education, skills, interests, career goals,")
    print("experience level, or learning preferences.")
    print("\nPress Enter twice when finished.\n")

    lines = []

    while True:

        line = input()

        if line == "":
            break

        lines.append(line)

    student_profile = "\n".join(lines)

    if not student_profile.strip():
        print("\nNo student profile entered.")
        return

    print("\nAnalyzing profile and recommending courses...\n")

    recommendations = recommend_courses(student_profile)

    print("=" * 70)
    print(recommendations)
    print("=" * 70)


if __name__ == "__main__":
    main()