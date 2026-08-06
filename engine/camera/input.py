# ============================================================
# CrashPhys Studio
# File: engine/camera/input.py
# Version: 0.2.4
#
# Camera input controller
#
# Handles:
# - Mouse camera rotation
# - Keyboard movement
# - WASD editor controls
# - Stable mouse dragging
#
# ============================================================


class InputController:


    def __init__(
        self,
        camera
    ):


        self.camera = camera


        # ====================================================
        # Mouse
        # ====================================================

        self.mouse_down = False

        self.last_x = 0
        self.last_y = 0


        self.mouse_sensitivity = 0.15



        # ====================================================
        # Keyboard
        # ====================================================

        self.keys = set()



        print(
            "[Input] Controller Initialized"
        )





    # ========================================================
    # Keyboard
    # ========================================================


    def key_press(
        self,
        key
    ):


        self.keys.add(
            key
        )


        print(
            "[Input] Key Down:",
            key
        )





    def key_release(
        self,
        key
    ):


        if key in self.keys:

            self.keys.remove(
                key
            )


        print(
            "[Input] Key Up:",
            key
        )





    def pressed(
        self,
        key
    ):


        return key in self.keys





    # ========================================================
    # Movement
    # ========================================================


    def update(
        self,
        delta_time
    ):


        speed = (

            self.camera.speed *

            delta_time

        )



        if self.pressed("W"):

            self.camera.move_forward(
                speed
            )


        if self.pressed("S"):

            self.camera.move_backward(
                speed
            )


        if self.pressed("A"):

            self.camera.move_left(
                speed
            )


        if self.pressed("D"):

            self.camera.move_right(
                speed
            )


        if self.pressed("E"):

            self.camera.move_up(
                speed
            )


        if self.pressed("Q"):

            self.camera.move_down(
                speed
            )





    # ========================================================
    # Mouse Press
    # ========================================================


    def mouse_press(
        self,
        button,
        x,
        y
    ):


        #
        # Left mouse
        #

        if button == 1:


            self.mouse_down = True


            self.last_x = x

            self.last_y = y


            print(
                "[Input] Mouse Camera Start"
            )





    # ========================================================
    # Mouse Release
    # ========================================================


    def mouse_release(
        self,
        button
    ):


        if button == 1:


            self.mouse_down = False


            print(
                "[Input] Mouse Camera Stop"
            )





    # ========================================================
    # Mouse Move
    # ========================================================


    def mouse_move(
        self,
        x,
        y,
        dx=None,
        dy=None
    ):



        if not self.mouse_down:

            return



        #
        # Use engine supplied delta
        #

        if dx is not None and dy is not None:


            move_x = dx

            move_y = dy



        else:


            move_x = x - self.last_x

            move_y = y - self.last_y





        self.last_x = x

        self.last_y = y




        if move_x == 0 and move_y == 0:

            return





        self.camera.process_mouse(

            move_x * self.mouse_sensitivity,

            -move_y * self.mouse_sensitivity

        )


        print(
            "[Input] Camera Rotate:",
            move_x,
            move_y
        )