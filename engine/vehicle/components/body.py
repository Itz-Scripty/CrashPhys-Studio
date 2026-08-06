# ============================================================
# CrashPhys Studio
# File: engine/vehicle/components/body.py
#
# Vehicle Body Component
#
# ============================================================


class Body:


    def __init__(
        self,
        name="Vehicle Body"
    ):


        self.name = name

        self.health = 100.0

        self.damage = 0.0

        self.destroyed = False


        print(
            "[Body] Created:",
            self.name
        )



    # ========================================================
    # Damage
    # ========================================================


    def apply_damage(
        self,
        amount
    ):


        self.damage += amount

        self.health -= amount


        if self.health <= 0:


            self.health = 0

            self.destroyed = True


            print(
                "[Body] Destroyed"
            )



    # ========================================================
    # Repair
    # ========================================================


    def repair(
        self,
        amount
    ):


        self.health += amount


        if self.health > 100:

            self.health = 100



        if self.health > 0:

            self.destroyed = False




    # ========================================================
    # Debug
    # ========================================================


    def info(
        self
    ):


        return {

            "Name": self.name,

            "Health": self.health,

            "Damage": self.damage,

            "Destroyed": self.destroyed

        }