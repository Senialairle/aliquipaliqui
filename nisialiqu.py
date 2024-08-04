from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open("template.html").read())

@app.route('/submit', methods=['POST'])
def submit():
    checkbox_value = 'checked' if request.form.get('myCheckbox') else 'not checked'
    return f'Checkbox was {checkbox_value}'

if __name__ == '__main__':
    app.run(debug=True)
