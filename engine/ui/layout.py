# ============================================================
# CrashPhys Studio
# File: engine/ui/layout.py
# Version: 0.1.0
#
# UI Layout System
#
# Handles:
# - Panel positioning
# - Window resizing
# - Editor layout foundation
#
# ============================================================



class EditorLayout:


    def __init__(
        self
    ):


        self.left_width = 250

        self.right_width = 280


        print(
            "[UI] Layout Initialized"
        )





    # ========================================================
    # Apply Layout
    # ========================================================


    def apply(
        self,
        panels,
        window_width,
        window_height
    ):


        if len(panels) < 2:

            return



        project = panels[0]

        inspector = panels[1]



        #
        # Left panel
        #

        project.x = 0

        project.y = 0

        project.width = self.left_width

        project.height = window_height



        #
        # Right panel
        #

        inspector.x = (
            window_width -
            self.right_width
        )

        inspector.y = 0

        inspector.width = self.right_width

        inspector.height = window_height





    # ========================================================
    # Settings
    # ========================================================


    def set_left_width(
        self,
        width
    ):

        self.left_width = width




    def set_right_width(
        self,
        width
    ):

        self.right_width = width