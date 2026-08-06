# ============================================================
# CrashPhys Studio
# File: engine/vehicle/vehicle_builder.py
# Version: 0.3.1
#
# Vehicle Builder
#
# Handles:
# - Vehicle creation
# - Component assembly
# - Wheel installation
# - Suspension installation
# - Wheel mounting positions
# - Vehicle presets
#
# ============================================================


from engine.vehicle.vehicle import Vehicle


from engine.vehicle.components.wheel import Wheel
from engine.vehicle.components.suspension import Suspension





class VehicleBuilder:



    def __init__(
        self
    ):


        print(
            "[VehicleBuilder] Initialized"
        )





    # ========================================================
    # Build Vehicle
    # ========================================================


    def build(
        self,
        name="Crash Test Vehicle"
    ):


        print(
            "[VehicleBuilder] Building:",
            name
        )



        vehicle = Vehicle(
            name
        )



        self.add_wheels(
            vehicle
        )


        self.add_suspension(
            vehicle
        )



        print(
            "[VehicleBuilder] Complete:",
            name
        )



        return vehicle





    # ========================================================
    # Wheels
    # ========================================================


    def add_wheels(
        self,
        vehicle
    ):


        #
        # Wheel mounting points
        #
        # X = left/right
        # Y = height
        # Z = front/back
        #
        # Body width = 2.8
        # Tire radius = 0.45
        #
        # Mounted slightly inside chassis
        #


        mounts = {


            Wheel.FRONT_LEFT:
            (
                -1.15,
                -0.45,
                 2.0
            ),


            Wheel.FRONT_RIGHT:
            (
                 1.15,
                -0.45,
                 2.0
            ),


            Wheel.REAR_LEFT:
            (
                -1.15,
                -0.45,
                -2.0
            ),


            Wheel.REAR_RIGHT:
            (
                 1.15,
                -0.45,
                -2.0
            )


        }





        for name, position in mounts.items():



            wheel = Wheel(
                name
            )



            wheel.set_position(

                position[0],

                position[1],

                position[2]

            )



            vehicle.add_wheel(
                wheel
            )



            print(
                "[VehicleBuilder] Mounted Wheel:",
                name,
                position
            )





    # ========================================================
    # Suspension
    # ========================================================


    def add_suspension(
        self,
        vehicle
    ):



        for wheel in vehicle.wheels:



            suspension = Suspension(

                wheel.name + " Suspension",

                wheel

            )



            wheel.attach_suspension(
                suspension
            )



            vehicle.add_suspension(
                suspension
            )



        print(
            "[VehicleBuilder] Suspension Installed:",
            len(vehicle.suspension)
        )





    # ========================================================
    # Presets
    # ========================================================


    def create_buggy(
        self
    ):


        buggy = self.build(

            "Crash Test Buggy"

        )



        #
        # Buggy tuning
        #


        buggy.engine.horsepower = 250


        buggy.engine.torque = 350



        print(
            "[VehicleBuilder] Buggy Preset Loaded"
        )



        return buggy