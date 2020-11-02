from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastroLivros.sqlite3'
db = SQLAlchemy(app)


class BancoLivro(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    livro = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    lido = db.Column(db.String(3), nullable=False)

    def __init__(self, id, livro, autor, lido):
        self.id = id
        self.livro = livro
        self.autor = autor
        self.lido = lido


@app.route('/')
def index():
    livros = BancoLivro.query.all()
    return render_template('index.html', livros=livros)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        adic_livro = BancoLivro(request.form['id'], request.form['livro'],
                           request.form['autor'], request.form['lido'])
        db.session.add(adic_livro)
        #aqui salvamos no banco
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    editalivrobanco = BancoLivro.query.get(id)
    if request.method == 'POST':
        editalivrobanco.id = request.form['id']
        editalivrobanco.livro = request.form['livro']
        editalivrobanco.autor = request.form['autor']
        editalivrobanco.lido = request.form['lido']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', editalivrobanco=editalivrobanco)


@app.route('/delete/<int:id>')
def delete(id):
    deleta_livro_banco = BancoLivro.query.get(id)
    db.session.delete(deleta_livro_banco)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)