# financial_data.py

"""
Financial data module for the chatbot.
Contains the financial data and functions to access it.
"""

# Financial data for Microsoft, Tesla, and Apple (2022-2024)
FINANCIAL_DATA = {
    "Microsoft": {
        "2022": {"Total Revenue": 198270, "Net Income": 72738, "Total Assets": 364840, "Total Liabilities": 198298, "CFFOA": 89035},
        "2023": {"Total Revenue": 211915, "Net Income": 72361, "Total Assets": 411976, "Total Liabilities": 205723, "CFFOA": 87582},
        "2024": {"Total Revenue": 245122, "Net Income": 88136, "Total Assets": 512163, "Total Liabilities": 243686, "CFFOA": 118548}
    },
    "Tesla": {
        "2022": {"Total Revenue": 81462, "Net Income": 12587, "Total Assets": 82338, "Total Liabilities": 36440, "CFFOA": 14724},
        "2023": {"Total Revenue": 96773, "Net Income": 14974, "Total Assets": 106618, "Total Liabilities": 43009, "CFFOA": 13256},
        "2024": {"Total Revenue": 97690, "Net Income": 7153, "Total Assets": 122070, "Total Liabilities": 48390, "CFFOA": 14923}
    },
    "Apple": {
        "2022": {"Total Revenue": 394328, "Net Income": 99803, "Total Assets": 352755, "Total Liabilities": 302083, "CFFOA": 122151},
        "2023": {"Total Revenue": 383285, "Net Income": 96995, "Total Assets": 352583, "Total Liabilities": 290437, "CFFOA": 110543},
        "2024": {"Total Revenue": 391035, "Net Income": 9736, "Total Assets": 364980, "Total Liabilities": 308030, "CFFOA": 118254}
    }
}

# Pre-calculated financial metrics
GROWTH_METRICS = {
    "Microsoft": {
        "2023": {"Revenue Growth": 6.88, "Net Income Growth": -0.52, "Assets Growth": 12.92, "Liabilities Growth": 3.74, "CFFOA Growth": -1.63},
        "2024": {"Revenue Growth": 15.67, "Net Income Growth": 21.80, "Assets Growth": 24.32, "Liabilities Growth": 18.45, "CFFOA Growth": 35.36}
    },
    "Tesla": {
        "2023": {"Revenue Growth": 18.80, "Net Income Growth": 18.96, "Assets Growth": 29.49, "Liabilities Growth": 18.03, "CFFOA Growth": -9.97},
        "2024": {"Revenue Growth": 0.95, "Net Income Growth": -52.23, "Assets Growth": 14.49, "Liabilities Growth": 12.51, "CFFOA Growth": 12.58}
    },
    "Apple": {
        "2023": {"Revenue Growth": -2.80, "Net Income Growth": -2.81, "Assets Growth": -0.05, "Liabilities Growth": -3.85, "CFFOA Growth": -9.50},
        "2024": {"Revenue Growth": 2.02, "Net Income Growth": -89.96, "Assets Growth": 3.52, "Liabilities Growth": 6.06, "CFFOA Growth": 6.98}
    }
}

# Financial health insights
FINANCIAL_HEALTH = {
    "Microsoft": "Microsoft demonstrates excellent financial health with consistent revenue growth (15.67% in 2024), strong net income growth (21.80% in 2024), and solid cash flow from operations. The company maintains a balanced growth across all financial metrics, suggesting sustainable business operations and successful expansion strategies.",
    "Tesla": "Tesla shows mixed financial health indicators. While revenue growth has slowed (0.95% in 2024), net income declined significantly (-52.23% in 2024). Their cash flow from operations improved compared to 2023, but Tesla's relatively lower CFFOA compared to net income might indicate potential concerns with cash conversion efficiency.",
    "Apple": "Apple maintains strong overall financial health despite fluctuations. Their revenue showed modest growth (2.02% in 2024), but net income experienced a significant decline (-89.96% in 2024). However, Apple maintains the strongest cash generation capability among the three companies, suggesting superior business fundamentals despite short-term profit challenges."
}

# Cash flow comparison
CASH_FLOW_COMPARISON = """Cash Flow Performance Comparison (2022-2024):

Microsoft: Shows the most consistent year-over-year improvement in Cash Flow from Operating Activities (CFFOA), growing to $118,548 million in 2024, a 35.36% increase from 2023.

Apple: Maintains the strongest overall cash generation capability with CFFOA at $118,254 million in 2024, showing recovery from the previous year's decline.

Tesla: Has the lowest absolute CFFOA at $14,923 million in 2024, but showed improvement over 2023, increasing by approximately 12.58%.

The CFFOA-to-revenue ratio is most favorable for Apple, suggesting superior cash conversion efficiency. All companies maintained positive CFFOA throughout the period, indicating healthy core operations."""
