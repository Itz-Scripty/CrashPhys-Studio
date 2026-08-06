# ============================================================
# CrashPhys Studio
# File: engine/vehicle/components/engine.py
# Version: 0.1.0
#
# Vehicle Engine Component
#
# Handles:
# - Engine power
# - Torque
# - RPM
# - Temperature
# - Oil
# - Coolant
# - Engine health
# - Failure states
#
# ============================================================


class Engine:


    def __init__(
        self,
        name="Engine"
    ):


        #
        # Identity
        #

        self.name = name

        self.type = "Engine"



        #
        # Performance
        #

        self.horsepower = 400


        self.torque = 450


        self.max_rpm = 7000


        self.rpm = 0



        #
        # Condition
        #

        self.health = 100


        self.running = False


        self.failed = False



        #
        # Fluids
        #

        self.oil = 100


        self.coolant = 100



        #
        # Temperature
        #

        self.temperature = 70



        print(
            "[Engine] Created:",
            self.name
        )





    # ========================================================
    # Start / Stop
    # ========================================================


    def start(
        self
    ):


        if self.failed:

            print(
                "[Engine] Cannot Start - Failed"
            )

            return



        self.running = True



        print(
            "[Engine] Started"
        )





    def stop(
        self
    ):


        self.running = False


        self.rpm = 0



        print(
            "[Engine] Stopped"
        )





    # ========================================================
    # Update
    # ========================================================


    def update(
        self,
        delta_time
    ):


        if not self.running:

            return



        #
        # Simulate RPM
        #

        if self.rpm < self.max_rpm:

            self.rpm += 1000 * delta_time



        #
        # Heat
        #

        self.temperature += (
            10 *
            delta_time
        )



        #
        # Overheat protection
        #

        if self.temperature > 120:

            self.apply_damage(
                5 * delta_time
            )





    # ========================================================
    # Damage
    # ========================================================


    def apply_damage(
        self,
        amount
    ):


        self.health -= amount



        if self.health < 0:

            self.health = 0



        print(
            "[Engine] Damage:",
            amount,
            "Health:",
            self.health
        )



        if self.health <= 0:

            self.fail()





    def fail(
        self
    ):


        self.failed = True


        self.running = False


        self.rpm = 0



        print(
            "[Engine] FAILURE"
        )





    def repair(
        self
    ):


        self.health = 100


        self.failed = False



        print(
            "[Engine] Repaired"
        )





    # ========================================================
    # Inspector
    # ========================================================


    def get_inspector_data(
        self
    ):


        return {


            "Component":
            self.type,


            "Horsepower":
            self.horsepower,


            "Torque":
            self.torque,


            "RPM":
            round(
                self.rpm
            ),


            "Temperature":
            self.temperature,


            "Oil":
            self.oil,


            "Coolant":
            self.coolant,


            "Health":
            self.health,


            "Running":
            self.running,


            "Failed":
            self.failed

        }