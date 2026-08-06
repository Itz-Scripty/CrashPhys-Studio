# ============================================================
# CrashPhys Studio
# File: engine/core/object.py
# Version: 0.4.0
#
# Studio Object System
#
# Handles:
# - Object identity
# - Transform system
# - Object state
# - Update loop
# - Destruction
# - Transform access
#
# ============================================================





class Transform:


    def __init__(
        self
    ):


        #
        # Position
        #

        self.position = [

            0.0,
            0.0,
            0.0

        ]



        #
        # Rotation
        #

        self.rotation = [

            0.0,
            0.0,
            0.0

        ]



        #
        # Scale
        #

        self.scale = [

            1.0,
            1.0,
            1.0

        ]





class StudioObject:


    #
    # Global ID counter
    #

    _next_id = 1





    def __init__(
        self,
        name="Object"
    ):


        #
        # Identity
        #

        self.id = StudioObject._next_id


        StudioObject._next_id += 1



        self.name = name



        #
        # State
        #

        self.enabled = True

        self.destroyed = False



        #
        # Transform
        #

        self.transform = Transform()



        print(
            "[Object] Created:",
            self.name,
            "ID:",
            self.id
        )





    # ========================================================
    # Transform Helpers
    # ========================================================


    def set_position(
        self,
        x,
        y,
        z
    ):


        self.transform.position = [

            x,
            y,
            z

        ]





    def set_rotation(
        self,
        x,
        y,
        z
    ):


        self.transform.rotation = [

            x,
            y,
            z

        ]





    def set_scale(
        self,
        x,
        y,
        z
    ):


        self.transform.scale = [

            x,
            y,
            z

        ]





    # ========================================================
    # Transform Access
    # ========================================================


    def get_position(
        self
    ):


        return self.transform.position





    def get_rotation(
        self
    ):


        return self.transform.rotation





    def get_scale(
        self
    ):


        return self.transform.scale





    # ========================================================
    # Update
    # ========================================================


    def update(
        self,
        delta_time
    ):


        if not self.enabled:

            return



        if self.destroyed:

            return



        #
        # Override in child classes
        #

        pass





    # ========================================================
    # State
    # ========================================================


    def enable(
        self
    ):


        self.enabled = True





    def disable(
        self
    ):


        self.enabled = False





    # ========================================================
    # Destroy
    # ========================================================


    def destroy(
        self
    ):


        if self.destroyed:

            return



        self.destroyed = True


        self.enabled = False



        print(
            "[Object] Destroyed:",
            self.name
        )