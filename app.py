from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    quote = ""
    error_message = ""
    if request.method == 'POST':
        if request.form['submit_button'] == 'Generate':
            response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
            if response.status_code == 200:
                data = response.json()
                quote = data['title'] if data else ""
            else:
                error_message = "Error getting quote"
    return render_template('index.html', quote=quote, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
