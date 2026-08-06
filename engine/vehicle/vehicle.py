# ============================================================
# CrashPhys Studio
# File: engine/vehicle/vehicle.py
# Version: 0.3.0
#
# Vehicle Core
#
# Handles:
# - Vehicle identity
# - Engine
# - Body
# - Wheels
# - Suspension
# - Transform
#
# ============================================================


from engine.vehicle.components.engine import Engine
from engine.vehicle.components.body import Body
from engine.core.transform import Transform





class Vehicle:



    next_id = 1





    def __init__(
        self,
        name="Vehicle"
    ):


        self.name = name


        self.id = Vehicle.next_id

        Vehicle.next_id += 1



        #
        # Components
        #

        self.engine = Engine()


        self.body = Body()



        self.transform = Transform()



        #
        # Wheels
        #

        self.wheels = []


        self.suspension = []



        #
        # State
        #

        self.enabled = True

        self.destroyed = False



        print(
            "[Vehicle] Created:",
            self.name,
            "ID:",
            self.id
        )





    # ========================================================
    # Wheels
    # ========================================================


    def add_wheel(
        self,
        wheel
    ):


        self.wheels.append(
            wheel
        )


        print(
            "[Vehicle] Wheel Added:",
            wheel.name
        )





    # ========================================================
    # Suspension
    # ========================================================


    def add_suspension(
        self,
        suspension
    ):


        self.suspension.append(
            suspension
        )


        suspension.wheel.attach_suspension(
            suspension
        )


        print(
            "[Vehicle] Suspension Added:",
            suspension.name
        )





    # ========================================================
    # Update
    # ========================================================


    def update(
        self,
        delta_time
    ):


        for wheel in self.wheels:

            wheel.update(
                delta_time
            )





    # ========================================================
    # Debug
    # ========================================================


    def info(
        self
    ):


        return {


            "Name": self.name,

            "ID": self.id,

            "Engine": self.engine,

            "Body": self.body,

            "Wheels": len(self.wheels),

            "Destroyed": self.destroyed


        }