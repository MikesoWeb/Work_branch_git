from flask import Flask, Markup

app = Flask('app')


@app.get('/')
def index():
    name_branch = 'Develop'
    return Markup(f"""
    <h1 style="
        display: flex;
        justify-content: center;
        margin-top: 40px;
        font-size: 80px;
        color: teal;
        font-family: monospace;">
        {name_branch} branch
    </h1>
    """)


if __name__ == '__main__':
    app.run(debug=True)
