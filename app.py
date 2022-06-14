from flask import Flask, jsonify, request
from resources import user

#from dotenv import load_dotenv
#from sqlalchemy.orm import joinedload

api=Flask(__name__)



@api.route('/')
def dummy_api():
    return "Welcome To Flask-SqlAlchemy"

@api.route('/insert', methods=['GET'])
#class insert:
def insert():
    return user.insert()
#    return jsonify("...inserted successfully...")

if __name__== "__main__":
    api.run(debug=True, host="0.0.0.0", port="5001")
