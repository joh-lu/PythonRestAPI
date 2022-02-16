from flask import Flask, request
import uuid

app = Flask(__name__)


class List:
    def __init__(self, id, name, todos):
        self.id = id
        self.name = name
        self.todos = todos


class ToDo:
    def __init__(self, id, name, description, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.user_id = user_id


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


#zeigt alle Todo-Listen
@app.route("/todo-list", methods=['GET'])
def getlist():
    return "GETLIST"

#fügt neue Todo-Liste hinzu
@app.route("/todo-list", methods=['POST'])
def postlist():
    return "POSTLIST"

#zeigt alle Einträge einer Todo-Liste
@app.route("/todo-list/<string:list_id>", methods=['GET'])
def getlistid():
    return "GETLISTID"

#löscht eine Todo-Liste
@app.route("/todo-list/<string:list_id>", methods=['DELETE'])
def deletelistid():
    return "DELETELISTID"

#fügt einer Liste einen neuen Eintrag hinzu
@app.route("/todo-list/<string:list_id>/entry", methods=['POST'])
def postentry():
    return "POSTENTRY"

#aktualisiert einen Eintrag
@app.route("/todo-list/<string:list_id>/entry/<string:entry_id>", methods=['PUT'])
def putentryid():
    return "PUTENTRYID"

#löscht einen Eintrag
@app.route("/todo-list/<string:list_id>/entry/<string:entry_id>", methods=['DELETE'])
def deleteentryid():
    return "DELETEENTRYID"


#zeigt alle User
@app.route("/user", methods=['GET'])
def getuser():
    return "GETUSER"

#fügt einen neuen User hinzu
@app.route("/user", methods=['POST'])
def postuser():
    return "POSTUSER"

#löscht einen User
@app.route("/user/<string:user_id>", methods=['DELETE'])
def deleteuser():
    return "DELETEUSER"


#Server starten
if __name__ == '__main__':
    app.run(host='')