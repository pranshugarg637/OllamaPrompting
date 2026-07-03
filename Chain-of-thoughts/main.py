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
# Chain-of-Thought System Prompt
# ----------------------------------------

SYSTEM_PROMPT = """
You are an intelligent Loan EMI Explanation Assistant.

Your task is to calculate the Equated Monthly Installment (EMI) and explain the calculation in a clear, step-by-step manner.

Instructions:
- Analyze the loan details carefully.
- Identify all required values.
- Explain each calculation step clearly.
- Use the standard EMI formula.
- Show intermediate calculations where appropriate.
- Round the final EMI to two decimal places.
- Also calculate the total payment and total interest payable.
- If any required information is missing, mention what is needed.
- End with a short disclaimer that the result is an estimate.

Format:

Thought:
Analyze the loan details and identify the required values.

Step 1:
Identify:
- Loan Amount (Principal)
- Annual Interest Rate
- Loan Tenure (Years or Months)

Step 2:
Convert values if necessary.

Formula:
Monthly Interest Rate = Annual Interest Rate ÷ (12 × 100)

Loan Tenure in Months = Years × 12

Step 3:
Calculate EMI.

Formula:

EMI = P × R × (1 + R)^N
      -------------------
      ((1 + R)^N − 1)

Where:
P = Principal Loan Amount
R = Monthly Interest Rate
N = Number of Monthly Installments

Calculation:
...

Step 4:
Calculate Total Payment.

Formula:
Total Payment = EMI × N

Calculation:
...

Step 5:
Calculate Total Interest.

Formula:
Total Interest = Total Payment − Principal

Calculation:
...

Final Answer:

Loan Summary:
- Loan Amount:
- Interest Rate:
- Loan Tenure:

Monthly EMI:
₹ ...

Total Payment:
₹ ...

Total Interest:
₹ ...

Explanation:
Provide a simple explanation of how the EMI was calculated.

Disclaimer:
This EMI is an estimated value. Actual EMI may vary depending on lender policies, processing fees, insurance charges, taxes, and repayment terms.

Loan Details:
{loan_details}
"""

# ----------------------------------------
# Chat Function
# ----------------------------------------

def calculate_emi(loan_details):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": loan_details,
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
    print("      CHAIN-OF-THOUGHT LOAN EMI EXPLANATION ASSISTANT")
    print("=" * 70)

    print("\nEnter the loan details below.")
    print("Example:")
    print("Loan Amount: ₹500000")
    print("Interest Rate: 8.5%")
    print("Loan Tenure: 5 years")
    print("\nPress Enter twice when finished.\n")

    lines = []

    while True:

        line = input()

        if line == "":
            break

        lines.append(line)

    loan_details = "\n".join(lines)

    if not loan_details.strip():
        print("\nNo loan details entered.")
        return

    print("\nCalculating EMI...\n")

    result = calculate_emi(loan_details)

    print("=" * 70)
    print(result)
    print("=" * 70)


if __name__ == "__main__":
    main()