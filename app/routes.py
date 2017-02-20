import time
import sqlite3
from app import app
from flask import request

@app.route('/', methods=['GET'])
@app.route('/api/v1/signup', methods=['GET'])
def index():
    # get information from request
    ip = request.environ['REMOTE_ADDR']

    #NOTE: only for debugging in docker
    print(request.args)
    mail = request.args.get('mail')
    if mail:
        # open database
        db = sqlite3.Connection('./db/user.db')
        
        # get database cursor
        cursor = db.cursor()

        # create table running on a new database
        cursor.execute('CREATE TABLE IF NOT EXISTS mail (id INTEGER PRIMARY KEY AUTOINCREMENT, address TEXT, ip TEXT, time INT)')
        
        # check if mail exists in database
        cursor.execute('SELECT * FROM mail')
        rows = cursor.fetchall()
        contains_mail = False
        for row in rows:
            if row[1] == mail:
                contains_mail = True
                break

        # else, add it to the database
        if not contains_mail:
            cursor.execute(
                    'INSERT INTO mail(address, ip, time) VALUES (?,?,?)',
                    (mail, ip, int(time.time()))
                    )
        cursor.execute('SELECT * FROM mail')
        print(cursor.fetchall())

        # close database connection after committing the changes
        cursor.close()
        db.commit()
        db.close()
        return "1"
    return "0"
