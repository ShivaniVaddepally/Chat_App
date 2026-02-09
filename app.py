from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

messages = []  # temporary message storage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    username = request.form['username']
    return render_template('chat.html', username=username, messages=messages)

@app.route('/send', methods=['POST'])
def send():
    username = request.form['username']
    message = request.form['message']
    messages.append(f"{username}: {message}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
