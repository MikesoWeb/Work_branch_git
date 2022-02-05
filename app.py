from flask import Flask, Markup

app = Flask('app')


def index():
    name_branch = 'Main'
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


app.add_url_rule('/', view_func=index)

if __name__ == '__main__':
    app.run(debug=True)
