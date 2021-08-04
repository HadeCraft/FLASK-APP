from flask import Flask , jsonify , request
app = Flask(__name__)

contacts = [100,200,300,400,500,600]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "statue":"error",
            "message":"Please provide the data!!"
        },400)

contact =  {
    'id': tasks[-1]['id'] + 1,
    'Name': request.json['Name'],
    'Contact':request.json.get('Contact', ""),
    'done' : False
    }


