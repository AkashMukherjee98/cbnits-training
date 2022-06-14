from flask import jsonify, request,make_response
#from flask_sqlalchemy import SQLAlchemy
#from dotenv import load_dotenv
from models import db_user
import traceback

#@app.route('/')
#def dummy_api():
#    return "Welcome To User"

# @app.route('/create', methods=['GET'])
# def insert():
#     return "ok.."


#@app.route('/input', methods=['GET'])
def insert():
    #return "ok.."
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.get_json()
            # response_users = db_user.User.query.all()
            # for resp in response_users:
            #     print(resp)
            user=db_user.User(username=data['username'], email=data['email'])
            print(user)
            db_user.db.session.add(user)
            db_user.db.session.commit()         
        return "inserted data"
    except Exception as e:
        print(traceback.print_exc)
        print("error",e)
        return make_response(e)


#@app.route('/fetch', methods=['GET'])
# def fetch():
#     #return "hi"
#     val=[]
#     #value={}
#     users=u.User.query.all()
#     for user in users:
#         dic={}
#         id=user.id
#         name=user.username
#         mail=user.email
#         #print(id," ",name," ",mail)
#         dic=id,name,mail
#         #print("ss",dic)
#         val.append(dic)
#     print("\n")
#         #print(val)
#     return jsonify(val)
#     #for i in val:        
#     #return "ok  "

#@app.route('/update', methods=['PUT'])
# def update():
#     content_type = request.headers.get('Content-Type')
#     if(content_type == 'application/json'):
#         data = request.get_json()
#         u_id=data['id']
#         u_name=data['username']
#         u_mail=data['email']
#         print(u_id)
#         user = u.User.query.get(u_id)
#         user.username = u_name
#         user.email= u_mail
#         u.db.session.commit() 
#         return "update Sucessful"

#@app.route('/delt', methods=['DELETE'])
# def delt():
#     content_type = request.headers.get('Content-Type')
#     if(content_type == 'application/json'):
#         data = request.get_json()
#         u_id=data['id']
#         print(u_id)
#         user=u.User.query.get(u_id)
#         u.db.session.delete(user)
#         u.db.session.commit()
#         return "delete successful"


#if __name__== "__main__":
#    app.run(debug=True, host="0.0.0.0", port="5001")