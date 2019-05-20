from vsearch import searchforletters
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def hello():
    return 'Hello from Flask!!'

@app.route('/search4', methods=['POST'])
def do_search():
    phrase=request.form['phrase']
    letters=request.form['letters']
    title='Here are your results: '
    results=str(searchforletters(phrase,letters))
    return render_template('results.html',the_phrase=phrase,the_letters=letters,the_title=title,the_results=results)

@app.route('/entry')
def entry_page():
    return render_template('entry.html',the_title='Welceome to searchforletters on the web!')

app.debug = True 
app.run()
