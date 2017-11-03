from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "LetsC0unt"

@app.route("/")

def index():
    #check if 'count' key is in session obj, if it is, add to session count.
    # if not, session doesn't exist so must initialize a session.
    if 'count' in session:
        session['count'] += 1
        
    else:
        session['count'] = 1
        
    return render_template('counter.html', curr_count=session['count'])

@app.route('/add2', methods=["POST"])

def add_two():
    session['count'] += 1

    return redirect('/')


@app.route('/reset', methods=["POST"])
def reset():
    session['count'] = 0

    return redirect('/')

app.run(debug=True)
