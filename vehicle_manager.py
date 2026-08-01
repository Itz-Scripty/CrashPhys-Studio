import os
import json


class VehicleManager:

    def __init__(self, profile_folder="profiles"):

        self.profile_folder = profile_folder
        self.vehicles = []


    def scan_profiles(self):

        self.vehicles.clear()

        if not os.path.exists(self.profile_folder):
            os.makedirs(self.profile_folder)

        for file in os.listdir(self.profile_folder):

            if file.endswith(".json"):

                path = os.path.join(
                    self.profile_folder,
                    file
                )

                try:

                    with open(path, "r") as data:

                        vehicle = json.load(data)

                        self.vehicles.append({
                            "name": vehicle.get("name", "Unknown Vehicle"),
                            "path": path
                        })

                except Exception:

                    pass


    def get_vehicle_names(self):

        return [
            vehicle["name"]
            for vehicle in self.vehicles
        ]


    def get_vehicle_path(self, index):

        if index < 0 or index >= len(self.vehicles):
            return None

        return self.vehicles[index]["path"]