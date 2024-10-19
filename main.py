from flask import Flask,render_template,request,redirect
import requests

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    weather=None
    news=None
    quote=None
    if request.method == 'POST':
        city = request.form.get('city')
        weather = get_weather(city)
        news=get_news()
        quote=get_quote()

    return render_template('index.html',weather=weather,news=news,quote=quote)
def get_weather(city):
        api_key = '83ae226b645257424cfc78b3aa9e1aed'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        return response.json()


def get_news():
    api_key = '166ca3af12784888bf57ecad3551ac34'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    return response.json().get('articles',[])

def get_quote():
    # url = f'https://api.quotable.io/random'
    url=f'https://quoteapi.pythonanywhere.com/random'
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)