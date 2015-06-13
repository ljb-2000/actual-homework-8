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
	o = {"status":1}
	name = request.args.get('name')
	age = request.args.get('age')
	sql = 'insert into user values ("%s",%d)' % (name,int(age))
	print sql
	try:
		cur.execute(sql)
		o.status = 0
	return json.dumps(o)
if __name__ == '__main__':
	app.run(debug=True)
