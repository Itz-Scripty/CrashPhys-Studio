import json
import os



class VehicleBuilder:


    def __init__(self):

        self.vehicle = {

    "name": "",

    "type": "single",

    "body": {

        "model": ""

    },

            "wheels": {

                "front_left": "",

                "front_right": "",

                "rear_left": "",

                "rear_right": ""

            },

            "parts": [],

            "engine_health": 100

        }

    def set_vehicle_type(self, vehicle_type):

        self.vehicle["type"] = vehicle_type


    # ============================================
    # Set Vehicle Name
    # ============================================

    def set_name(self, name):

        self.vehicle["name"] = name



    # ============================================
    # Set Chassis
    # ============================================

    def set_body(self, model):

        self.vehicle["body"]["model"] = model



    # ============================================
    # Add Wheel
    # ============================================

    def set_wheel(self, position, model):

        if position in self.vehicle["wheels"]:

            self.vehicle["wheels"][position] = model



    # ============================================
    # Add Extra Part
    # ============================================

    def add_part(self, model):

        self.vehicle["parts"].append(
            model
        )



    # ============================================
    # Engine
    # ============================================

    def set_engine_health(self, health):

        self.vehicle["engine_health"] = health



    # ============================================
    # Validate
    # ============================================

    def validate(self):

        if not self.vehicle["name"]:

            return False, "Vehicle needs a name."


        if not self.vehicle["body"]["model"]:

            return False, "Vehicle needs a chassis."


        return True, "Vehicle ready."



    # ============================================
    # Export JSON
    # ============================================

    def save(self, path):

        valid, message = self.validate()


        if not valid:

            raise Exception(message)



        with open(
            path,
            "w"
        ) as file:

            json.dump(
                self.vehicle,
                file,
                indent=4
            )



        return True