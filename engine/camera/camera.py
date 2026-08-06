# ============================================================
# CrashPhys Studio
# File: engine/camera/camera.py
# Version: 0.2.1
#
# 3D Editor Camera System
#
# Handles:
# - Camera rotation
# - Position movement
# - View matrix
# - Projection matrix
#
# Changes:
# - Added delta time movement
# - Added editor movement speed
#
# ============================================================


import numpy as np
import math



class Camera:


    def __init__(self):


        self.position = np.array(
            [0.0, 6.0, 12.0],
            dtype="f4"
        )


        self.world_up = np.array(
            [0.0,1.0,0.0],
            dtype="f4"
        )


        self.front = np.array(
            [0.0,0.0,-1.0],
            dtype="f4"
        )


        self.right = np.array(
            [1.0,0.0,0.0],
            dtype="f4"
        )


        self.up = self.world_up.copy()



        self.yaw = -90.0

        self.pitch = -25.0



        self.sensitivity = 0.15


        # Editor movement speed

        self.speed = 10.0



        self.update_vectors()



    # ========================================================
    # Mouse Look
    # ========================================================


    def process_mouse(
        self,
        dx,
        dy
    ):


        self.yaw += dx * self.sensitivity

        self.pitch -= dy * self.sensitivity



        self.pitch = max(
            -89,
            min(
                89,
                self.pitch
            )
        )



        self.update_vectors()



    # ========================================================
    # Movement
    # ========================================================


    def move(
        self,
        direction,
        delta_time
    ):


        velocity = (
            self.speed *
            delta_time
        )


        self.position += (
            direction *
            velocity
        )



    def move_forward(
        self,
        delta_time
    ):

        self.move(
            self.front,
            delta_time
        )



    def move_backward(
        self,
        delta_time
    ):

        self.move(
            -self.front,
            delta_time
        )



    def move_right(
        self,
        delta_time
    ):

        self.move(
            self.right,
            delta_time
        )



    def move_left(
        self,
        delta_time
    ):

        self.move(
            -self.right,
            delta_time
        )



    def move_up(
        self,
        delta_time
    ):

        self.move(
            self.world_up,
            delta_time
        )



    def move_down(
        self,
        delta_time
    ):

        self.move(
            -self.world_up,
            delta_time
        )



    # ========================================================
    # Vector Update
    # ========================================================


    def update_vectors(self):


        yaw = math.radians(
            self.yaw
        )


        pitch = math.radians(
            self.pitch
        )



        direction = np.array(
            [
                math.cos(yaw)*math.cos(pitch),
                math.sin(pitch),
                math.sin(yaw)*math.cos(pitch)
            ],
            dtype="f4"
        )


        self.front = (
            direction /
            np.linalg.norm(direction)
        )


        self.right = np.cross(
            self.front,
            self.world_up
        )


        self.right /= np.linalg.norm(
            self.right
        )


        self.up = np.cross(
            self.right,
            self.front
        )



    # ========================================================
    # Matrices
    # ========================================================


    def get_view_matrix(self):

        return self.look_at(
            self.position,
            self.position+self.front,
            self.up
        )



    def get_projection_matrix(
        self,
        width,
        height
    ):


        aspect = width / height

        fov = math.radians(45)

        near = 0.1

        far = 1000.0



        f = 1.0 / math.tan(
            fov/2
        )


        matrix = np.zeros(
            (4,4),
            dtype="f4"
        )


        matrix[0][0] = f / aspect

        matrix[1][1] = f

        matrix[2][2] = (
            far+near
        )/(near-far)

        matrix[2][3] = -1

        matrix[3][2] = (
            2*far*near
        )/(near-far)


        return matrix



    def look_at(
        self,
        eye,
        target,
        up
    ):


        forward = target-eye

        forward /= np.linalg.norm(
            forward
        )


        right = np.cross(
            forward,
            up
        )


        right /= np.linalg.norm(
            right
        )


        camera_up = np.cross(
            right,
            forward
        )



        matrix = np.identity(
            4,
            dtype="f4"
        )


        matrix[0,:3] = right

        matrix[1,:3] = camera_up

        matrix[2,:3] = -forward


        matrix[3,0] = -np.dot(
            right,
            eye
        )

        matrix[3,1] = -np.dot(
            camera_up,
            eye
        )

        matrix[3,2] = np.dot(
            forward,
            eye
        )


        return matrix