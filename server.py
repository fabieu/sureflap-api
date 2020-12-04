from flask import Flask, render_template, request, jsonify
from ressources import config, devices, households, timeline, dashboard, pets, users
import os

###### Flask Configuration ######
app = Flask(__name__, template_folder='templates')
#app.config["DEBUG"] = True
os.environ['WERKZEUG_RUN_MAIN'] = 'true'

##### Routes ######
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

# Dashboard
@app.route('/dashboard', methods=['GET'])
def route_getDashboard():
    return jsonify(dashboard.getDashboard())

# Devices
@app.route('/devices', methods=['GET'])
def route_devices():
    return jsonify(devices.getDevices())

@app.route('/devices/<id>', methods=['GET'])
def route_device_ID(id):
    return jsonify(devices.getDeviceByID(id))


# Households
@app.route('/households', methods=['GET'])
def route_getHouseholds():
    return jsonify(households.getHouseholds())

@app.route('/households/<householdID>', methods=['GET'])
def route_getHouseholdByID(householdID):
    return jsonify(households.getHouseholdByID(householdID))


# Pets
@app.route('/households/<householdID>/pets', methods=['GET'])
def route_getPetsFromHousehold(householdID):
    return jsonify(pets.getPetsFromHousehold(householdID))

@app.route('/households/<householdID>/pets/<petID>', methods=['GET'])
def route_getPet(householdID, petID):
    return jsonify(pets.getPet(householdID, petID))

@app.route('/households/<householdID>/pets/<petID>/location', methods=['GET'])
def route_getPetLocation(householdID, petID):
    return jsonify(pets.getPetLocation(petID))

@app.route('/households/<householdID>/pets/<petID>/location', methods=['POST'])
def route_setPetLocation(householdID, petID):
    return jsonify(pets.setPetLocation(petID, request.form))

@app.route('/households/<householdID>/pets/location', methods=['GET'])
def route_getPetsLocations(householdID):
    return jsonify(pets.getPetsLocations(householdID))


# Users
@app.route('/households/<householdID>/users', methods=['GET'])
def route_getUsersFromHousehold(householdID):
    return jsonify(users.getUsersFromHousehold(householdID))

@app.route('/households/<householdID>/users/<userID>', methods=['GET'])
def route_getUser(householdID, userID):
    return jsonify(users.getUser(userID))

@app.route('/households/<householdID>/users/<userID>/photo', methods=['GET'])
def route_getUserPhoto(householdID, userID):
    return jsonify(users.getUserPhoto(userID))


# Timeline
@app.route('/households/<householdID>/timeline', methods=['GET'])
def route_getTimeline(householdID):
    return jsonify(timeline.getTimeline(householdID))


###### main ######
if __name__ == '__main__':
    if config.validate():
        app.run(host='0.0.0.0', port=3001)