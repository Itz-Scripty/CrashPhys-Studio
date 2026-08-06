# ============================================================
# CrashPhys Studio
# File: engine/editor/transform.py
# Version: 0.1.0
#
# Transform Controller
#
# Handles:
# - Position editing
# - Rotation editing
# - Scale editing
# - Editor transform state
#
# ============================================================





class TransformController:


    def __init__(
        self
    ):


        self.target = None


        self.mode = "translate"



        print(
            "[Transform] Initialized"
        )





    # ========================================================
    # Target
    # ========================================================


    def set_target(
        self,
        obj
    ):


        self.target = obj



        if obj:


            print(
                "[Transform] Target:",
                obj.name
            )





    def clear_target(
        self
    ):


        self.target = None



        print(
            "[Transform] Target Cleared"
        )





    # ========================================================
    # Modes
    # ========================================================


    def set_mode(
        self,
        mode
    ):


        valid = [

            "translate",

            "rotate",

            "scale"

        ]



        if mode not in valid:

            return



        self.mode = mode



        print(
            "[Transform] Mode:",
            mode
        )





    # ========================================================
    # Position
    # ========================================================


    def move(
        self,
        x,
        y,
        z
    ):


        if not self.target:

            return



        self.target.transform.position = [

            x,

            y,

            z

        ]





    # ========================================================
    # Rotation
    # ========================================================


    def rotate(
        self,
        x,
        y,
        z
    ):


        if not self.target:

            return



        self.target.transform.rotation = [

            x,

            y,

            z

        ]





    # ========================================================
    # Scale
    # ========================================================


    def scale(
        self,
        x,
        y,
        z
    ):


        if not self.target:

            return



        self.target.transform.scale = [

            x,

            y,

            z

        ]





    # ========================================================
    # Debug
    # ========================================================


    def debug(
        self
    ):


        if not self.target:

            print(
                "[Transform] No Target"
            )

            return



        print(
            "========== TRANSFORM =========="
        )


        print(
            "Object:",
            self.target.name
        )


        print(
            "Position:",
            self.target.transform.position
        )


        print(
            "Rotation:",
            self.target.transform.rotation
        )


        print(
            "Scale:",
            self.target.transform.scale
        )


        print(
            "==============================="
        )