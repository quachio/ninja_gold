from flask import Flask, redirect, render_template, session, request, Markup
from datetime import datetime

import random

app = Flask(__name__)
app.secret_key = 'ZKdRFjd6WpFCD+9NGETh4'


@app.route('/')
def index():
    if 'total' not in session:
        session['total'] = 0
        session['message'] = Markup('')
        
    return render_template('index.html', message=session['message'])

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    if building == 'farm':
        session['gold'] = random.randint(10, 20)
        session['total'] += session['gold']
        session['message'] += Markup( f'<p style="color: green"> Earned ' + str(session['gold']) + ' golds from the farm ' + dt_string + '</p>')
    elif building == 'cave':
        session['gold'] = random.randint(5, 10)
        session['total'] += session['gold']
        session['message'] += Markup( f'<p style="color: green"> Earned ' + str(session['gold']) + ' golds from the cave ' + dt_string + '</p>')
    elif building == 'house':
        session['gold'] = random.randint(2, 5)
        session['total'] += session['gold']
        session['message'] += Markup( f'<p style="color: green"> Earned ' + str(session['gold']) + ' golds from the house' + dt_string + '</p>')
    elif building == 'casino':
        session['gold'] = random.randint(0, 50)
        if random.randint(0, 1) == 0:
            session['total'] += session['gold']
            session['message'] += Markup( f'<p style="color: green"> Earned ' + str(session['gold']) + ' golds from the casino' + dt_string + '</p>')
        else:
            session['total'] -= session['gold']
            if session['total'] < 0:
                session['total'] = 0
            session['message'] += Markup( f'<p style="color: red"> Earned ' + str(session['gold']) + ' golds from the casino' + dt_string + '</p>')
    else:
        return redirect('/')

    print('Got post data', request.form, session['gold'])
    return redirect('/')

@app.route('/reset')
def reset_session():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)