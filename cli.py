# cli.py

"""
Command-line interface for the financial chatbot.
Allows interacting with the chatbot via the terminal.
"""

from chatbot import financial_chatbot

def main():
    """
    Main function for the CLI application.
    """
    print("Welcome to the Financial Chatbot!")
    print("I can provide insights about Microsoft, Tesla, and Apple's financial data from 2022-2024.")
    print("Type 'exit' or 'quit' to end the conversation.")
    print()
    print("I can answer questions like:")
    print("1. What is the total revenue for Microsoft in 2024?")
    print("2. How has Tesla's net income changed over the last year?")
    print("3. Which company had the highest revenue growth in the most recent year?")
    print("4. What is the financial health of Apple?")
    print("5. Compare the cash flow performance of all companies")
    print()
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            print("Thank you for using the Financial Chatbot. Goodbye!")
            break
        
        response = financial_chatbot(user_input)
        print(f"Bot: {response}")
        print()

if __name__ == "__main__":
    main()
