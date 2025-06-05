from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_info():
    user_info = {
        'name': 'Ngô Lê Anh Tú',
        'age': 21,
        'email': 'anhtu23042004@gmail.com'
    }
    return render_template('index.html', user=user_info)

if __name__ == '__main__':
    app.run(debug=True)
