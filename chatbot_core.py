
import random

def init_session(session_state):
    if "history" not in session_state:
        session_state.history = []
    if "level" not in session_state:
        session_state.level = "beginner"

def handle_query(query, session_state):
    term = query.strip().lower()

    if "explain" in term or "what is" in term:
        return explain_ratio(term, session_state.level)
    elif "calculate" in term:
        return calculate_ratio(term)
    elif "quiz" in term or "test" in term:
        return quiz_user(term)
    elif "which ratio" in term or "recommend" in term:
        return case_advisor(term)
    elif "translate" in term:
        return translate(term)
    elif "summary" in term:
        return show_summary(session_state)
    elif "i’m new" in term or "beginner" in term:
        session_state.level = "beginner"
        return "Switched to beginner mode."
    elif "advanced" in term:
        session_state.level = "advanced"
        return "Switched to advanced mode."
    else:
        return "Sorry, I didn't understand that. Try asking me about a specific ratio or say 'explain' or 'quiz me'."

def explain_ratio(term, level):
    explanation = f"""📘 **{term.upper()}**

This is a placeholder explanation for the ratio **{term}**.

- **Formula**: (Example) Net Income / Shareholder's Equity
- **Meaning**: Measures return on equity invested by shareholders.
- **Malay Term**: Pulangan atas Ekuiti

Want a calculation example or a quiz on this? Just ask!
"""
    return explanation

def calculate_ratio(term):
    return "🧮 Please enter the relevant values to calculate the ratio. (e.g., Net Income = 1000, Equity = 5000)"

def quiz_user(term):
    return "📊 Here's a quiz question: What does the ROE ratio measure? (A) Liquidity (B) Profitability (C) Leverage"

def case_advisor(term):
    return "📂 Based on your case, use Profitability Ratios like ROE or Net Profit Margin."

def translate(term):
    return "🈺 Translation: 'Return on Equity' = 'Pulangan atas Ekuiti'"

def show_summary(session_state):
    return "📁 You’ve reviewed 3 ratios: ROE, Current Ratio, and Debt-to-Equity."
