# ============================================================
# CrashPhys Studio
# File: engine/vehicle/components/suspension.py
# Version: 0.4.0
#
# Suspension Component
#
# Handles:
# - Wheel connection
# - Spring travel
# - Compression
# - Ride height
# - Suspension physics foundation
# - Wheel position updates
#
# ============================================================



class Suspension:



    def __init__(
        self,
        name,
        wheel=None
    ):


        self.name = name


        #
        # Connected wheel
        #

        self.wheel = wheel



        #
        # Suspension settings
        #

        self.max_travel = 0.35

        self.rest_height = -0.45


        #
        # State
        #

        self.compression = 0.0

        self.travel = 0.0



        #
        # Physics values
        #

        self.spring_rate = 2500.0

        self.damping = 150.0

        self.force = 0.0



        #
        # Enabled
        #

        self.enabled = True



        #
        # Store original wheel position
        #

        self.base_position = None



        if wheel:


            self.base_position = [

                wheel.position[0],

                wheel.position[1],

                wheel.position[2]

            ]



            wheel.attach_suspension(

                self

            )



        print(

            "[Suspension] Created:",

            self.name

        )







    # ========================================================
    # Compression
    # ========================================================


    def set_compression(
        self,
        amount
    ):


        self.compression = max(

            0.0,

            min(

                amount,

                1.0

            )

        )



        self.travel = (

            self.compression *

            self.max_travel

        )







    # ========================================================
    # Spring Force
    # ========================================================


    def calculate_force(
        self
    ):


        self.force = (

            self.spring_rate *

            self.travel

        )


        return self.force







    # ========================================================
    # Update
    # ========================================================


    def update(
        self,
        delta_time
    ):


        if not self.enabled:

            return



        self.calculate_force()



        if self.wheel is None:

            return



        if self.base_position is None:

            return






        #
        # Move wheel vertically
        #
        # More compression =
        # wheel moves upward
        #


        self.wheel.position[1] = (

            self.base_position[1]

            +

            self.travel

        )







    # ========================================================
    # Reset
    # ========================================================


    def reset(
        self
    ):


        self.compression = 0.0

        self.travel = 0.0

        self.force = 0.0



        if self.wheel and self.base_position:


            self.wheel.position[1] = (

                self.base_position[1]

            )







    # ========================================================
    # Debug
    # ========================================================


    def info(
        self
    ):


        return {


            "Name":

                self.name,


            "Wheel":

                self.wheel.name

                if self.wheel

                else None,


            "Travel":

                self.travel,


            "Compression":

                self.compression,


            "Force":

                self.force


        }