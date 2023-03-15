# Import flask and flask-restful
from flask import Flask, request
from flask_restful import Resource, Api

# Create an instance of flask app and api
app = Flask(__name__)
api = Api(app)

# Define a class for each endpoint resource
class Temperature(Resource):
    # Define the get method to return the current body temperature
    def get(self):
        # Get the optional query parameter for unit (default is Celsius)
        unit = request.args.get("unit", "Celsius")
        # Get the current body temperature from some data source (e.g., database, sensor, etc.)
        # For simplicity, assume it is 37 degrees Celsius
        temp = 37
        # Convert the temperature to the requested unit if necessary
        if unit == "Fahrenheit":
            temp = temp * 9/5 + 32
        elif unit == "Kelvin":
            temp = temp + 273.15
        # Return the temperature as a JSON object with status code 200 (OK)
        return {"temperature": temp, "unit": unit}, 200

    # Define the post method to set the desired body temperature
    def post(self):
        # Get the required JSON data from the request body (e.g., {"temperature": 38, "unit": "Celsius"})
        data = request.get_json()
        # Validate the data (e.g., check if temperature and unit are valid values)
        # For simplicity, assume they are valid
        # Set the desired body temperature using some logic or function (e.g., adjust thermostat, medication, etc.)
        # For simplicity, assume it is successful
        # Return a success message as a JSON object with status code 201 (Created)
        return {"message": f"Desired body temperature set to {data['temperature']} {data['unit']}"}

class Sleep(Resource):
    # Define similar methods for sleep endpoint as above
    pass

class Allergy(Resource):
    # Define similar methods for allergy endpoint as above
    pass

# Add each resource class to the api with their corresponding URL path 
api.add_resource(Temperature, "/v1/body/temperature")
api.add_resource(Sleep, "/v1/body/sleep")
api.add_resource(Allergy, "/v1/body/allergy", "/v1/body/allergy/<string:allergen>")

# Run the app on port 5000 in debug mode 
if __name__ == "__main__":
    app.run(debug=True,port=5000)