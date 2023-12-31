from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample shopping list items (replace this with a database)
shopping_list = []

@app.route('/')
def index():
    return render_template('index.html', shopping_list=shopping_list)

@app.route('/add_item', methods=['POST'])
def add_item():
    item = request.form['item']
    if item:
        shopping_list.append(item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
