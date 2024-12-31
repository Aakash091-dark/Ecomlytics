from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to display data
@app.route('/data')
def data():
    df = pd.read_csv('./data/Cleaned_Ecommerce_Customers.csv')
    data_html = df.head().to_html()  # Convert data to HTML table
    return f"<h1>Dataset Overview</h1>{data_html}"

# Route for summary statistics
@app.route('/summary')
def summary():
    df = pd.read_csv('./data/Cleaned_Ecommerce_Customers.csv')
    summary_html = df.describe().to_html()
    return f"<h1>Summary Statistics</h1>{summary_html}"

@app.route('/visualizations')
def visualizations():
    return '''
        <h1>Visualizations</h1>
        <img src="/static/images/correlation_heatmap.png" alt="Correlation Heatmap">
    '''


if __name__ == '__main__':
    app.run(debug=True)
