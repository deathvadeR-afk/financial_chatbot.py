# test_chatbot.py

"""
Test script for the financial chatbot.
Tests the chatbot's responses to various queries.
"""

from chatbot import financial_chatbot

def test_chatbot():
    """
    Test the chatbot with a set of predefined queries.
    """
    test_queries = [
        "What is the total revenue for Microsoft in 2024?",
        "How has Tesla's net income changed over the last year?",
        "Which company had the highest revenue growth in the most recent year?",
        "What is the financial health of Apple?",
        "Compare the cash flow performance of all companies",
        "Tell me about Microsoft's profit margin"  # Unrecognized query
    ]

    print("=== Financial Chatbot Test ===\n")
    
    for i, query in enumerate(test_queries, 1):
        print(f"Test {i}: {query}")
        print(f"Response: {financial_chatbot(query)}")
        print("-" * 80)
        print()

if __name__ == "__main__":
    test_chatbot()
