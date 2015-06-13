import MySQLdb as mysql
from flask import Flask,request,render_template
app = Flask(__name__)
con = mysql.connect(user='root',\
                    passwd='',\
                    db='winiu4',\
                    host='localhost')
import json
con.autocommit(True)
cur = con.cursor()

@app.route('/list')
def list():
    page = int(request.args.get('page',1))
    count = request.args.get('count',5)

    o = {
        'status':1,
        'table_str':'',
        'total_page':'',
        'pagation_str':''

    }   

    init_str = ''
    count_sql = 'select count(*) from cmdb'
    cur.execute(count_sql)
    total = cur.fetchall()[0][0]
    o['total_page'] = total/count+1
    sql = 'select * from cmdb limit %s,%s' % ((page-1)*count,count)
    cur.execute(sql)
    for c in cur.fetchall():

        init_str = init_str + '''<tr><td>%s</td><td>%s</td><td>%s</td><td>
                                <button data-id="%s" class="btn btn-warning delete">
                                delete</button>
                                <button data-id="%s" class="btn btn-info update">
                                update</button>
                                </td></tr>''' % (c[0],c[1],c[2],c[0],c[0])
    o['table_str'] = init_str

    page_str = ''
    i = 1
    while i<=o['total_page']:
        if i==page:     
            page_str = page_str+'''
                                <li class="active page-reboot" data-page="%s">
                                    <a href="#">%s</a></li> 
                        '''%(i,i)
        else:
            page_str = page_str+'''
                                <li data-page="%s" class="page-reboot">
                                    <a href="#">%s</a></li> 
                        '''%(i,i)

        i = i+1
    o['pagation_str'] = page_str
    return json.dumps(o)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete')
def delete():
    delete_id = request.args.get('id')
    sql = 'delete from cmdb where id = %s' % (delete_id)
    cur.execute(sql)
    return 'ok'
@app.route('/search')
def search():
    id = request.args.get('id')
    sql = 'select memory from cmdb where id = %s' % (id)
    cur.execute(sql)

    return str(cur.fetchall()[0][0])
@app.route('/update')
def update():
    id = request.args.get('id')
    memory = request.args.get('memory')
    sql = 'update cmdb set memory=%s where id = %s' % (memory,id)
    cur.execute(sql)
    return 'ok'

@app.route('/add')
def add():
    o = {}
    o['status'] = 1
    server = request.args.get('server')
    memory = request.args.get('memory')
    sql = 'insert into cmdb (server ,memory) values ("%s",%s)' % (server,memory)
    try:
        cur.execute(sql)
        o['status'] = 0
    except:
        pass
    return json.dumps(o)




if __name__ == '__main__':
    app.run(debug=True,port=9092,host='0.0.0.0')







