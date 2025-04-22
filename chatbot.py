# chatbot.py

"""
Core module for the financial chatbot.
Contains the main logic for processing user queries.
"""

from financial_data import FINANCIAL_DATA, GROWTH_METRICS, FINANCIAL_HEALTH, CASH_FLOW_COMPARISON

def get_total_revenue(company, year):
    """
    Get the total revenue for a specific company in a specific year.
    
    Args:
        company (str): The company name (Microsoft, Tesla, or Apple)
        year (str): The year (2022, 2023, or 2024)
        
    Returns:
        str: A response containing the total revenue information
    """
    if company in FINANCIAL_DATA and year in FINANCIAL_DATA[company]:
        revenue = FINANCIAL_DATA[company][year]["Total Revenue"]
        return f"The total revenue for {company} in {year} was ${revenue:,} million."
    else:
        return f"Sorry, I don't have revenue data for {company} in {year}."

def get_net_income_change(company):
    """
    Get the net income change for a specific company between 2023 and 2024.
    
    Args:
        company (str): The company name (Microsoft, Tesla, or Apple)
        
    Returns:
        str: A response containing the net income change information
    """
    if company in FINANCIAL_DATA:
        income_2023 = FINANCIAL_DATA[company]["2023"]["Net Income"]
        income_2024 = FINANCIAL_DATA[company]["2024"]["Net Income"]
        change = ((income_2024 - income_2023) / income_2023) * 100
        
        if change > 0:
            return f"{company}'s net income increased by {change:.2f}% from 2023 to 2024, rising from ${income_2023:,} million to ${income_2024:,} million."
        else:
            return f"{company}'s net income decreased by {abs(change):.2f}% from 2023 to 2024, falling from ${income_2023:,} million to ${income_2024:,} million."
    else:
        return f"Sorry, I don't have net income change data for {company}."

def get_highest_revenue_growth():
    """
    Get the company with the highest revenue growth in 2024.
    
    Returns:
        str: A response containing the highest revenue growth information
    """
    growth_2024 = {
        company: GROWTH_METRICS[company]["2024"]["Revenue Growth"] 
        for company in GROWTH_METRICS
    }
    
    highest_company = max(growth_2024, key=growth_2024.get)
    
    response = f"Among Microsoft, Tesla, and Apple, {highest_company} had the highest revenue growth in 2024 at {growth_2024[highest_company]:.2f}%.\n\n"
    response += "Revenue growth rates for 2024:\n"
    
    for company, growth in growth_2024.items():
        response += f"- {company}: {growth:.2f}%\n"
    
    return response

def get_financial_health(company):
    """
    Get the financial health assessment for a specific company.
    
    Args:
        company (str): The company name (Microsoft, Tesla, or Apple)
        
    Returns:
        str: A response containing the financial health information
    """
    if company in FINANCIAL_HEALTH:
        return FINANCIAL_HEALTH[company]
    else:
        return f"Sorry, I don't have financial health data for {company}."

def compare_cash_flow():
    """
    Compare the cash flow performance of all companies.
    
    Returns:
        str: A response containing the cash flow comparison
    """
    return CASH_FLOW_COMPARISON

def financial_chatbot(user_query):
    """
    Process a user query and return an appropriate response.
    
    Args:
        user_query (str): The user's query
        
    Returns:
        str: The chatbot's response
    """
    # Normalize the query by converting to lowercase
    query = user_query.lower().strip()
    
    # Check for revenue query pattern
    if "total revenue" in query or "revenue for" in query:
        for company in ["microsoft", "tesla", "apple"]:
            if company in query:
                for year in ["2022", "2023", "2024"]:
                    if year in query:
                        return get_total_revenue(company.capitalize(), year)
                return "Please specify which year (2022, 2023, or 2024) you're interested in."
        return "Please specify which company (Microsoft, Tesla, or Apple) you're interested in."
    
    # Check for net income change query
    elif "net income" in query and ("change" in query or "changed" in query):
        for company in ["microsoft", "tesla", "apple"]:
            if company in query:
                return get_net_income_change(company.capitalize())
        return "Please specify which company (Microsoft, Tesla, or Apple) you're interested in."
    
    # Check for highest revenue growth query
    elif "highest revenue growth" in query or ("highest" in query and "growth" in query):
        return get_highest_revenue_growth()
    
    # Check for financial health query
    elif "financial health" in query:
        for company in ["microsoft", "tesla", "apple"]:
            if company in query:
                return get_financial_health(company.capitalize())
        return "Please specify which company (Microsoft, Tesla, or Apple) you're interested in."
    
    # Check for cash flow comparison query
    elif "cash flow" in query and ("compar" in query or "all companies" in query):
        return compare_cash_flow()
    
    # Default response for unrecognized queries
    else:
        return """I can answer the following financial queries:
1. What is the total revenue for [company] in [year]?
2. How has [company]'s net income changed over the last year?
3. Which company had the highest revenue growth in the most recent year?
4. What is the financial health of [company]?
5. Compare the cash flow performance of all companies

Please try phrasing your question using one of these formats."""
