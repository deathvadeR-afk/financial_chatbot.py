# app.py

"""
Flask web application for the financial chatbot.
Provides a web interface for interacting with the chatbot.
"""

from flask import Flask, render_template, request, jsonify
from chatbot import financial_chatbot

app = Flask(__name__)

@app.route('/')
def index():
    """
    Route for the home page.
    """
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    """
    API endpoint for getting chatbot responses.
    """
    user_query = request.form['user_query']
    response = financial_chatbot(user_query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
