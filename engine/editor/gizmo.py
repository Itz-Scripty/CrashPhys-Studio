# ============================================================
# CrashPhys Studio
# File: engine/editor/gizmo.py
# Version: 0.1.0
#
# Transform Gizmo
#
# Handles:
# - Selected object transform
# - Move tool
# - Rotate tool
# - Scale tool
# - Gizmo drawing foundation
#
# ============================================================



class Gizmo:


    MOVE = "move"
    ROTATE = "rotate"
    SCALE = "scale"



    def __init__(
        self
    ):


        self.target = None


        self.mode = Gizmo.MOVE


        self.visible = True


        self.active_axis = None


        print(
            "[Gizmo] Initialized"
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
                "[Gizmo] Target:",
                obj.name
            )



    def clear_target(
        self
    ):


        self.target = None

        self.active_axis = None



    # ========================================================
    # Mode
    # ========================================================


    def set_mode(
        self,
        mode
    ):


        self.mode = mode


        print(
            "[Gizmo] Mode:",
            mode
        )



    # ========================================================
    # Axis
    # ========================================================


    def begin_drag(
        self,
        axis
    ):


        self.active_axis = axis


        print(
            "[Gizmo] Drag:",
            axis
        )



    def end_drag(
        self
    ):


        self.active_axis = None



    # ========================================================
    # Update
    # ========================================================


    def update(
        self,
        delta_time
    ):


        if not self.target:

            return


        #
        # Drag logic will be added later.
        #



    # ========================================================
    # Draw
    # ========================================================


    def draw(
        self
    ):


        if not self.visible:

            return


        if not self.target:

            return


        if not hasattr(
            self.target,
            "transform"
        ):

            return


        position = self.target.transform.position


        print(
            "[Gizmo] Draw",
            self.mode,
            "at",
            position
        )