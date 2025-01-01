from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# Load the dataset
DATA_PATH = "data\Cleaned_Ecommerce_Customers.csv"  # Ensure the path matches your file structure
df = pd.read_csv(DATA_PATH)

# Ensure the static folder is present for storing images
os.makedirs("static/images", exist_ok=True)

@app.route("/")
def home():
    """
    Homepage with a brief overview of the project.
    """
    return """
    <h1>Welcome to Ecomlytics</h1>
    <p>Analyze e-commerce customer data and gain valuable insights.</p>
    <ul>
        <li><a href="/statistics">View Data Statistics</a></li>
        <li><a href="/visualizations">View Visualizations</a></li>
        <li><a href="/customer-count">Customer Count</a></li>
        <li><a href="/search-customer/1">Search for a Customer (Example ID: 1)</a></li>
    </ul>
    """

@app.route("/statistics")
def statistics():
    """
    Display basic statistics about the dataset.
    """
    stats = df.describe().to_html()
    return f"""
    <h1>Data Statistics</h1>
    {stats}
    <a href="/">Back to Home</a>
    """

@app.route("/customer-count")
def customer_count():
    """
    Display the total number of customers.
    """
    count = len(df)
    return f"""
    <h1>Total Customers: {count}</h1>
    <a href="/">Back to Home</a>
    """

@app.route("/visualizations")
def visualizations():
    """
    Display visualizations saved in the static/images folder.
    """
    visualizations_html = """
    <h1>Visualizations</h1>
    <ul>
        <li><img src="/static/images/yearly_amount_distribution.png" alt="Yearly Amount Distribution"></li>
        <li><img src="/static/images/time_on_platforms.png" alt="Time on Platforms"></li>
        <li><img src="/static/images/membership_vs_spending.png" alt="Membership vs Spending"></li>
        <li><img src="/static/images/time_on_app_vs_spending.png" alt="Time on App vs Spending"></li>
        <li><img src="/static/images/time_on_website_vs_spending.png" alt="Time on Website vs Spending"></li>
        <li><img src="/static/images/spending_vs_time.png" alt="Spending vs Time on App and Website"></li>
    </ul>
    <a href="/">Back to Home</a>
    """
    return visualizations_html

@app.route("/search-customer/<int:id>")
def search_customer(id):
    """
    Search for a specific customer by ID.
    """
    customer = df[df.index == id]  # Assuming the index represents the customer ID
    if not customer.empty:
        return f"""
        <h1>Customer Details</h1>
        {customer.to_html()}
        <p><a href="/">Back to Home</a></p>
        """
    else:
        return f"""
        <h1>Customer Not Found</h1>
        <p>No customer with ID {id} found.</p>
        <p><a href="/">Back to Home</a></p>
        """

if __name__ == "__main__":
    app.run(debug=True)
