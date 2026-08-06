# ============================================================
# CrashPhys Studio
# File: engine/scene/object.py
#
# Base Scene Object
#
# Used by:
# - Vehicles
# - Props
# - Editor objects
#
# ============================================================


from engine.core.transform import Transform



class SceneObject:


    _next_id = 1



    def __init__(
        self,
        name="Object"
    ):


        self.id = SceneObject._next_id

        SceneObject._next_id += 1



        self.name = name


        # Editor state

        self.enabled = True

        self.visible = True



        # Transform

        self.transform = Transform()



        print(
            "[SceneObject] Created:",
            self.name,
            "ID:",
            self.id
        )




    # ========================================================
    # Update
    # ========================================================

    def update(
        self,
        delta_time
    ):

        pass




    # ========================================================
    # Render Hook
    # ========================================================

    def render(
        self
    ):

        pass




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
    # Debug
    # ========================================================


    def __repr__(self):

        return (
            f"<SceneObject "
            f"{self.name} "
            f"ID={self.id}>"
        )