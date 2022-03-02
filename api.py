from flask import Flask, request, jsonify, abort
import uuid

app = Flask(__name__)

# create unique id for lists, users, entries
user_id_bob = str(uuid.uuid4())
user_id_alice = str(uuid.uuid4())
user_id_eve = str(uuid.uuid4())
todo_list_1_id = '1318d3d1-d979-47e1-a225-dab1751dbe75'
todo_list_2_id = '3062dc25-6b80-4315-bb1d-a7c86b014c65'
todo_list_3_id = '44b02e00-03bc-451d-8d01-0c67ea866fee'
todo_1_id = str(uuid.uuid4())
todo_2_id = str(uuid.uuid4())
todo_3_id = str(uuid.uuid4())
todo_4_id = str(uuid.uuid4())

# define internal data structures with example data
user_list = [
    {'id': user_id_bob, 'name': 'Bob'},
    {'id': user_id_alice, 'name': 'Alice'},
    {'id': user_id_eve, 'name': 'Eve'},
]
todo_lists = [
    {'id': todo_list_1_id, 'name': 'Einkaufsliste'},
    {'id': todo_list_2_id, 'name': 'Arbeit'},
    {'id': todo_list_3_id, 'name': 'Privat'},
]
todos = [
    {'id': todo_1_id, 'name': 'Milch', 'description': '', 'list': todo_list_1_id, 'user': user_id_bob},
    {'id': todo_2_id, 'name': 'Arbeitsblätter ausdrucken', 'description': '', 'list': todo_list_2_id, 'user': user_id_alice},
    {'id': todo_3_id, 'name': 'Kinokarten kaufen', 'description': '', 'list': todo_list_3_id, 'user': user_id_eve},
    {'id': todo_3_id, 'name': 'Eier', 'description': '', 'list': todo_list_1_id, 'user': user_id_eve},
]

# add some headers to allow cross origin access to the API on this server, necessary for using preview in Swagger Editor!
@app.after_request
def apply_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# define endpoint for getting and deleting existing todo lists
@app.route('/todo-list/<list_id>', methods=['GET', 'DELETE'])
def handle_list(list_id):
    # find todo list depending on given list id
    list_item = None
    for l in todo_lists:
        if l['id'] == list_id:
            list_item = l
            break
    # if the given list id is invalid, return status code 404
    if not list_item:
        return 200
    if request.method == 'GET':
        # find all todo entries for the todo list with the given id
        print('Returning todo list...')
        #return '', 200 
        return jsonify([i for i in todos if i['list'] == list_id])
    elif request.method == 'DELETE':
        # delete list with given id
        print('Deleting todo list...')
        todo_lists.remove(list_item)
        return '', 200

 
#schows all Todo-Lists
@app.route("/todo-list", methods=['GET'])
def getlist():
    return jsonify(todo_lists)


"""
#fügt neue Todo-Liste hinzu
@app.route("/todo-list", methods=['POST'])
def postlist():
    return "POSTLIST"
 """

"""
#fügt einer Liste einen neuen Eintrag hinzu
@app.route("/todo-list/<list_id>/entry", methods=['POST'])
def postentry():
    return "POSTENTRY"

#aktualisiert einen Eintrag
@app.route("/todo-list/<list_id>/entry/<entry_id>", methods=['PUT'])
def putentryid():
    return "PUTENTRYID"

"""

#löscht einen Eintrag
@app.route("/todo-list/<list_id>/entry/<entry_id>", methods=['DELETE'])
def deleteentryid(entry_id):
    for e in user_list:
        if e["id"] == entry_id:
            user_list.remove(e)
            return '', 200
    
    return 404


#shows all user
@app.route("/user", methods=['GET'])
def getuser():
    return jsonify(user_list)


"""
#fügt einen neuen User hinzu
@app.route("/user", methods=['POST'])
def postuser():
    return "POSTUSER"

"""

#löscht einen User
@app.route("/user/<user_id>", methods=['DELETE'])
def deleteuser(user_id):
    for u in user_list:
        if u["id"] == user_id:
            user_list.remove(u)
            return '', 200
    
    return 404
    


#Server starten
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
