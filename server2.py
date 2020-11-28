from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
import os

db_connect = create_engine('sqlite:///data3.db')
app = Flask(__name__)
api = Api(app)


def test(a):
    string = str(a)
    return string


class Apps(Resource):
    def get(self):
        connect = db_connect.connect()  # connect to database
        query = connect.execute("select * from TodaysApps")  # This line performs query and returns json result
        row = query.cursor.fetchall()
        for i in range(len(row)):
            return row[i]  # Fetches first row that is Employee ID


# class Tracks(Resource):
#     def get(self):
#         connect = db_connect.connect()
#         query = connect.execute("select trackid, name, composer, unitprice from tracks;")
#         result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
#         return jsonify(result)
#
#
# class Employees_Name(Resource):
#     def get(self, employee_id):
#         connect = db_connect.connect()
#         query = connect.execute("select * from employees where EmployeeId =%d " % int(employee_id))
#         result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
#         return jsonify(result)


api.add_resource(Apps, '/apps')  # Route_1
# api.add_resource(Tracks, '/tracks')  # Route_2
# api.add_resource(Employees_Name, '/employees/<employee_id>')  # Route_3

if __name__ == '__main__':
    # connect = db_connect.connect()
    # connect.execute("UPDATE employees SET FirstName = 'bob' where EmployeeId = 3;")
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5002)))

#  http://localhost:5002/employees
