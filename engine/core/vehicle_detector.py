import os


class VehicleDetector:

    def __init__(self):

        self.reset()

    # ============================================
    # Reset
    # ============================================

    def reset(self):

        self.body = None

        self.wheels = []

        self.parts = []

        self.other = []

    # ============================================
    # Detect Vehicle
    # ============================================

    def detect(self, models):

        self.reset()

        for model in models:

            self.classify(model)

        return {

            "body": self.body,

            "wheels": self.assign_wheels(),

            "parts": self.parts,

            "other": self.other

        }

    # ============================================
    # Classify Model
    # ============================================

    def classify(self, model):

        name = os.path.basename(
            model
        ).lower()

        # ------------------------
        # Body Detection
        # ------------------------

        body_words = [

            "chassis",
            "body",
            "vehicle",
            "car",
            "truck",
            "sedan",
            "van",
            "suv",
            "police",
            "charger",
            "mustang",
            "camaro"

        ]

        if any(word in name for word in body_words):

            if self.body is None:

                self.body = model

                return

        # ------------------------
        # Wheel Detection
        # ------------------------

        wheel_words = [

            "wheel",
            "tire",
            "tyre",
            "rim"

        ]

        if any(word in name for word in wheel_words):

            self.wheels.append(
                model
            )

            return

        # ------------------------
        # Vehicle Parts
        # ------------------------

        part_words = [

            "door",
            "hood",
            "bonnet",
            "trunk",
            "boot",
            "spoiler",
            "bumper",
            "mirror",
            "engine",
            "grille",
            "light"

        ]

        if any(word in name for word in part_words):

            self.parts.append(
                model
            )

            return

        # ------------------------
        # Unknown
        # ------------------------

        self.other.append(
            model
        )

    # ============================================
    # Assign Wheels
    # ============================================

    def assign_wheels(self):

        wheel_data = {

            "front_left": "",
            "front_right": "",
            "rear_left": "",
            "rear_right": ""

        }

        if len(self.wheels) == 1:

            wheel = self.wheels[0]

            wheel_data["front_left"] = wheel
            wheel_data["front_right"] = wheel
            wheel_data["rear_left"] = wheel
            wheel_data["rear_right"] = wheel

        elif len(self.wheels) >= 2:

            front = self.wheels[0]
            rear = self.wheels[1]

            wheel_data["front_left"] = front
            wheel_data["front_right"] = front
            wheel_data["rear_left"] = rear
            wheel_data["rear_right"] = rear

        elif len(self.wheels) >= 4:

            wheel_data["front_left"] = self.wheels[0]
            wheel_data["front_right"] = self.wheels[1]
            wheel_data["rear_left"] = self.wheels[2]
            wheel_data["rear_right"] = self.wheels[3]

        return wheel_data