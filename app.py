from flask import Flask, render_template, url_for, request, redirect
from api import getAllProduto, save

app = Flask(__name__)

@app.route('/')
def index():
    date = getAllProduto()
    return render_template('index.html', date=date)

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


@app.route('/produto/')
def produtoCard():
    return render_template('produto.html')



if __name__ == "__main__":
    app.run()