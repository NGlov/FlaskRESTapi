from flask import Flask, jsonify, request
app = Flask(__name__)
arrOfAnimals = [{'id': 1, 'animal': 'lion' }, {'id': 2, 'animal': 'fox'}, {'id': 3, 'animal': 'whale'}, {'id': 4, 'animal': 'sheep'}, {'id': 5, 'animal': 'deer'}]
@app.route("/get_animals", methods=['GET'])
def getReq():
        return jsonify(arrOfAnimals), 200 #convert to json and return http 200 success code "http://127.0.0.1:5000/get_animals"
@app.route("/del_animals", methods=['DELETE'])
def delReq():
    animal_id = request.args.get('id', type=int)
    if animal_id is None:
        return jsonify({"error": "Index out of bounds!"}), 400
    for animal in arrOfAnimals:
            if animal['id'] == animal_id:
                arrOfAnimals.remove(animal)
                return jsonify(animal)
    else:
        return jsonify({"error": "This animal does not exist within the list!"}), 404
@app.route("/add_animals", methods=['POST'])
def postReq():
    if request.method == "POST":
        data = request.get_json()

        return jsonify(data), 201
    else:
        return jsonify("Animal already is in list!")
    
if __name__ == "__main__":
    app.run(debug=True)
