import json


class ProfileIO:


    @staticmethod
    def save(vehicle, filename):

        data = {

            "name": vehicle.name,

            "model": vehicle.model,

            "engine_health": vehicle.engine_health,

            "front_left_tire": vehicle.front_left_tire,

            "front_right_tire": vehicle.front_right_tire,

            "rear_left_tire": vehicle.rear_left_tire,

            "rear_right_tire": vehicle.rear_right_tire
        }


        with open(filename, "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )


    @staticmethod
    def load(vehicle, filename):

        with open(filename, "r") as file:

            data = json.load(file)


        vehicle.name = data.get(
            "name",
            "New Vehicle"
        )


        vehicle.model = data.get(
            "model",
            ""
        )


        vehicle.engine_health = data.get(
            "engine_health",
            100
        )


        vehicle.front_left_tire = data.get(
            "front_left_tire",
            "Healthy"
        )


        vehicle.front_right_tire = data.get(
            "front_right_tire",
            "Healthy"
        )


        vehicle.rear_left_tire = data.get(
            "rear_left_tire",
            "Healthy"
        )


        vehicle.rear_right_tire = data.get(
            "rear_right_tire",
            "Healthy"
        )