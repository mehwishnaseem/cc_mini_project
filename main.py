from flask import Flask, jsonify, request
from fetch_uv_data import fetch_uv_data, retrieve_data
from dbase import select_data, insert_data, delete_record, modify_record

app = Flask(__name__)

# GET
@app.route("/location/<city>/", methods=['GET'])
def get_data(city):
    try:
        lat, lng = select_data(city)
        ext_api_data = retrieve_data(lat, lng)
        return jsonify(ext_api_data), 200
    except:
        return jsonify({'error':'city not found'}), 404


# POST
@app.route('/add', methods=['POST'])
def create_a_record():
    if not request.json or not all(k in request.json for k in ['city', 'lat', 'lng']):
        return jsonify({'error':'the city record needs to have a city, lat & long'}), 400
    new_record = {
        'city': request.json['city'],
        'lat' : request.json.get('lat', ''),
        'lng' : request.json.get('lng', ''),
    }
    insert_data(new_record['city'], new_record['lat'], new_record['lng'])
    return jsonify({'message':'new city created: /add/{} and lat:{}, lng:{}'.format(new_record['city'], new_record['lat'], new_record['lng'])}), 201


# PUT
@app.route('/edit', methods=['PUT']) 
def edit_record():
    print(request.json)
    if not request.json or not all(k in request.json for k in ['city', 'lat', 'lng']):
        return jsonify({'error':'the city record needs to have a city, lat & long'}), 400
    new_record = {
        'city': request.json['city'],
        'lat' : request.json.get('lat', ''),
        'lng' : request.json.get('lng', ''),
    }
    
    status = modify_record(new_record['city'], new_record['lat'], new_record['lng'])
    if status:
        return jsonify({'success': f'Modified {new_record["city"]}'}), 201
    else:    
        return jsonify({'error':'city name not found!'}), 404 


# DELETE
@app.route('/delete/<city>', methods=['DELETE']) 
def delete_a_record(city): 
    
    status = delete_record(city)
    if status:
        return jsonify({'success': f'Deleted {city}'}), 200
    else:    
        return jsonify({'error': 'Record not found'}), 404     
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
