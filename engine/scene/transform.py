# ============================================================
# CrashPhys Studio
# File: engine/scene/transform.py
#
# Core Transform System
#
# Used by:
# - Vehicles
# - Mesh Objects
# - Editor Objects
#
# Beta 0.1
# ============================================================


import numpy as np
from math import radians, sin, cos



class Transform:


    def __init__(self):

        self.position = np.array(
            [
                0.0,
                0.0,
                0.0
            ],
            dtype="f4"
        )


        self.rotation = np.array(
            [
                0.0,
                0.0,
                0.0
            ],
            dtype="f4"
        )


        self.scale = np.array(
            [
                1.0,
                1.0,
                1.0
            ],
            dtype="f4"
        )


        print(
            "[Transform] Created"
        )



    # --------------------------------------------------------
    # Matrix
    # --------------------------------------------------------


    def get_matrix(self):


        matrix = np.identity(
            4,
            dtype="f4"
        )


        # Scale

        matrix[0][0] *= self.scale[0]
        matrix[1][1] *= self.scale[1]
        matrix[2][2] *= self.scale[2]



        # Translation

        matrix[3][0] = self.position[0]
        matrix[3][1] = self.position[1]
        matrix[3][2] = self.position[2]



        return matrix



    # --------------------------------------------------------
    # Helpers
    # --------------------------------------------------------


    def set_position(
        self,
        x,
        y,
        z
    ):

        self.position[:] = [
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

        self.rotation[:] = [
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

        self.scale[:] = [
            x,
            y,
            z
        ]



    def reset(self):

        self.position[:] = 0

        self.rotation[:] = 0

        self.scale[:] = 1



    def __repr__(self):

        return (
            f"Transform("
            f"pos={self.position}, "
            f"rot={self.rotation}, "
            f"scale={self.scale})"
        )