from flask import Flask, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conectando com banco MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSAWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
mysql = MySQL()
mysql.init_app(app)
# Cursor do MySQL
cursor = mysql.get_db().cursor()


@app.route('/')
def rota1():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM computer")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', computers=data)


if __name__ == "__main__":
    app.run(debug=True)