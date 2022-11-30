from flask import Flask, render_template
import pandas

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/search/<int:user_year>')
def get_matches_by_year(user_year):
    df_fifa = pandas.read_csv('fifa_matches.csv')
    dic_fifa = df_fifa.to_dict()

    home = dic_fifa['home']
    away = dic_fifa['away']
    score = dic_fifa['score']
    year = dic_fifa['year']

    return render_template('search.html',
                           home=home,
                           away=away,
                           score=score,
                           year=year,
                           range=range,
                           len=len,
                           user_year=user_year
                           )
