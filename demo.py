import MySQLdb as mysql
from flask import Flask,request,render_template
app = Flask(__name__)
con = mysql.connect(user='root',\
					passwd='',\
					db='winiu4',\
					host='localhost')
con.autocommit(True)
cur = con.cursor()

@app.route('/list')
def list():
	init_str = ''
	sql = 'select * from cmdb'
	cur.execute(sql)
	for c in cur.fetchall():

		init_str = init_str + '''<tr><td>%s</td><td>%s</td><td>
								<button data-id="%s" class="btn btn-warning delete">
								delete</button></td></tr>''' % (c[1],c[2],c[0])
	print init_str
	return init_str

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/delete')
def delete():
	delete_id = request.args.get('id')
	sql = 'delete from cmdb where id = %s' % (delete_id)
	cur.execute(sql)
	return 'ok'

@app.route('/add')
def add():
	name = request.args.get('name')
	age = request.args.get('age')
	sql = 'insert into cmdb values ("%s",%s)' % (name,age)
	cur.execute(sql)
	return 'ok'




if __name__ == '__main__':
	app.run(debug=True)







