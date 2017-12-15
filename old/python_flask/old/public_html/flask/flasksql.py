from Flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'mint'
app.config['MYSQL_DATABASE_PASSWORD'] = 'salasana'
app.config['MYSQL_DATABASE_DB'] = 'testdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


mysql.init_app(app)


@app.route('/')

def get():
        cur = mysql.connect().cursr()
        cur.execute('''select * from testdb.test_table''')
        r = [dict((cur.description[i][0]
