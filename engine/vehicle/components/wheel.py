# ============================================================
# CrashPhys Studio
# File: engine/vehicle/components/wheel.py
# Version: 0.3.0
#
# Wheel Component
#
# Handles:
# - Wheel identity
# - Wheel transform
# - Wheel dimensions
# - Wheel health
# - Damage foundation
# - Suspension connection
#
# ============================================================


class Wheel:


    FRONT_LEFT = "FrontLeft"
    FRONT_RIGHT = "FrontRight"
    REAR_LEFT = "RearLeft"
    REAR_RIGHT = "RearRight"




    def __init__(
        self,
        name
    ):


        self.name = name



        #
        # Transform
        #

        self.position = [

            0.0,

            0.0,

            0.0

        ]


        self.rotation = [

            0.0,

            0.0,

            0.0

        ]



        self.scale = [

            1.0,

            1.0,

            1.0

        ]



        #
        # Wheel specs
        #

        self.radius = 0.5

        self.width = 0.35



        #
        # Physics
        #

        self.health = 100.0


        self.destroyed = False



        self.suspension = None



        print(

            "[Wheel] Created:",

            self.name

        )





    # ========================================================
    # Transform
    # ========================================================


    def set_position(
        self,
        x,
        y,
        z
    ):


        self.position[0] = x
        self.position[1] = y
        self.position[2] = z





    def set_rotation(
        self,
        x,
        y,
        z
    ):


        self.rotation[0] = x
        self.rotation[1] = y
        self.rotation[2] = z





    # ========================================================
    # Suspension
    # ========================================================


    def attach_suspension(
        self,
        suspension
    ):


        self.suspension = suspension



        print(

            "[Wheel] Suspension Attached:",

            self.name

        )





    # ========================================================
    # Damage
    # ========================================================


    def damage(
        self,
        amount
    ):


        if self.destroyed:

            return



        self.health -= amount



        if self.health <= 0:


            self.health = 0


            self.destroyed = True



            print(

                "[Wheel] Destroyed:",

                self.name

            )





    # ========================================================
    # Update
    # ========================================================


    def update(
        self,
        delta_time
    ):


        if self.suspension:


            self.suspension.update(

                delta_time

            )





    # ========================================================
    # Info
    # ========================================================


    def get_data(
        self
    ):


        return {


            "name":

                self.name,


            "position":

                self.position,


            "rotation":

                self.rotation,


            "radius":

                self.radius,


            "width":

                self.width,


            "health":

                self.health,


            "destroyed":

                self.destroyed

        }