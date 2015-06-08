import MySQLdb as mysql
from flask import Flask,request,render_template
app = Flask(__name__)
con = mysql.connect(user='root',\
					passwd='',\
					db='winiu4',\
					host='localhost')
con.autocommit(True)
cur = con.cursor()

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/add')
def add():
	name = request.args.get('name')
	age = request.args.get('age')
	sql = 'insert into user values ("%s",%d)' % (name,int(age))
	print sql
	cur.execute(sql)
	return 'ok'
if __name__ == '__main__':
	app.run(debug=True)
