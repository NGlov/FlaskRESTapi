from flask import Flask, jsonify, request
app = Flask(__name__)
arrOfAnimals = [{'id': 1, 'animal': 'lion' }, {'id': 2, 'animal': 'fox'}, {'id': 3, 'animal': 'whale'}, {'id': 4, 'animal': 'sheep'}, {'id': 5, 'animal': 'deer'}]
@app.route("/get_animals", methods=['GET'])
def getReq():
        return jsonify(arrOfAnimals), 200 #convert to json and return http 200 success code "http://127.0.0.1:5000/get_animals"
@app.route("/del_animals", methods=['DELETE'])
def delReq():
    index = request.args.get('index', type=int)
    if index is None:
        return jsonify({"error": "Index parameter is missing"}), 400
    if 0 <= index < len(arrOfAnimals):
        removed_animal = arrOfAnimals.pop(index)
        return jsonify(removed_animal), 200
    else:
        return jsonify({"error": "This animal does not exist within the list!"}), 4
@app.route("/add_animals", methods=['POST'])
def postReq():
    if request.method == "POST":
        data = request.get_json()

        return jsonify(data), 201
    else:
        return jsonify("Animal already is in list!")
    
if __name__ == "__main__":
    app.run(debug=True)