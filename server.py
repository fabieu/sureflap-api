from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from ressources import config, devices, households, timeline, dashboard, pets, users
import cherrypy

### Flask Configuration ###
app = Flask(__name__, template_folder='templates')
#app.config["DEBUG"] = True
CORS(app)


### Routes ###
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
    if config.init_config():
        # Mount the application
        cherrypy.tree.graft(app, "/")

        # Unsubscribe the default server
        cherrypy.server.unsubscribe()

        # Instantiate a new server object
        server = cherrypy._cpserver.Server()

        # Configure the server object
        server.socket_host = "0.0.0.0"
        server.socket_port = int(config.PORT)
        server.thread_pool = 30

        cherrypy.config.update({'log.screen': False,
                                'log.access_file': '',
                                'log.error_file': ''})

        # For SSL Support
        # server.ssl_module            = 'pyopenssl'
        # server.ssl_certificate       = 'ssl/certificate.crt'
        # server.ssl_private_key       = 'ssl/private.key'
        # server.ssl_certificate_chain = 'ssl/bundle.crt'

        # Subscribe this server
        server.subscribe()

        # Start the server engine (Option 1 *and* 2)
        cherrypy.engine.start()
        cherrypy.engine.block()
