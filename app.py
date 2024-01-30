from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_country_info', methods=['POST'])
def get_country_info():
    if request.method == 'POST':
        country_name = request.form['country_name']
        country_info = fetch_country_info(country_name)
        return render_template('index.html', country_info=country_info)

def fetch_country_info(country_name):
    base_url = 'https://restcountries.com/v2/name/'
    url = f'{base_url}{country_name}'
    response = requests.get(url)
    
    if response.status_code == 200:
        country_info = response.json()
        return country_info
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
