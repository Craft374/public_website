from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head>
                <meta charset="utf-8">
                <title>My Website</title>
            </head>
            <body>
                <h1>Welcome to My Website</h1>
                <form method="post" action="/submit">
                    <label for="message">Type your message:</label><br>
                    <textarea id="message" name="message" rows="8" cols="80"></textarea><br>
                    <button type="submit">Submit</button>
                </form>
            </body>
        </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    message = request.form['message']
    with open('message.txt', 'w') as f:
        f.write(message)
    return 'Message saved successfully!'

if __name__ == '__main__':
    app.run()
