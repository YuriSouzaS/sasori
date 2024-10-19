from flask import Flask, render_template, url_for, request, redirect
from api import getAllProduto, save, getProduto

app = Flask(__name__)

@app.route('/')
def index():
    parts = getAllProduto()
    return render_template('index.html', date=parts[0])

@app.route('/next')
def next():
    parts = getAllProduto()
    return render_template('index.html', date=parts[1])

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name: str = request.form['nameProduto']
        desc: str = request.form['desc']
        image: str = request.form['image']
        amount: int = request.form['quantidade']
        price: float = request.form['price']
        category: str = request.form['categoria']
                
        save(name, amount, desc,image, price, category)
        return redirect(url_for('index'))
         
    return render_template('form.html')


@app.route('/produto/<string:name>')
def produtoCard(name):
    date = getProduto(name)
    return render_template('produto.html', content=date)



if __name__ == "__main__":
    app.run()