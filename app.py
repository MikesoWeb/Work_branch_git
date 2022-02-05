from flask import Flask, render_template

app = Flask('app')


@app.get('/')
def index():
    name_branch = 'feature-style'
    return render_template('index.html', name_branch=name_branch)


if __name__ == '__main__':
    app.run(debug=True, port=5555)
