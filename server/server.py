from flask import Flask, render_template
import os

# Create a Flask web application
print(__file__)
static_dir = str(os.path.abspath(os.path.join(__file__ , "..", "../docs")))
app = Flask(__name__, static_url_path="", static_folder=static_dir)
app.template_folder = '../scripts/html'

# Define a route and the corresponding function
@app.route('/')
def index():
    return render_template('index.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)