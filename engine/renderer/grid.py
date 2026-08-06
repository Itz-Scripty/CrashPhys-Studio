# ============================================================
# CrashPhys Studio Engine
#
# File:
# grid.py
#
# Version:
# 0.1.0
#
# Description:
# World editor grid renderer.
# Provides the base 3D workspace reference plane.
#
# ============================================================


import numpy as np
import moderngl

from engine.vehicle.mesh import Mesh



class Grid:



    def __init__(
        self,
        ctx,
        shader,
        size=20,
        spacing=1
    ):


        self.ctx = ctx

        self.shader = shader


        self.size = size

        self.spacing = spacing



        self.vertices = self.generate()



        self.mesh = Mesh(
            self.ctx,
            self.vertices
        )



        self.mesh.create_vao(
            self.shader
        )



    # ========================================================
    # Generate Grid Vertices
    # ========================================================

    def generate(self):


        vertices = []


        half = self.size // 2



        for i in range(
            -half,
            half + 1
        ):


            offset = (
                i *
                self.spacing
            )



            # X axis lines

            vertices.extend(
                [
                    -half * self.spacing,
                    0.0,
                    offset,

                    half * self.spacing,
                    0.0,
                    offset
                ]
            )



            # Z axis lines

            vertices.extend(
                [
                    offset,
                    0.0,
                    -half * self.spacing,

                    offset,
                    0.0,
                    half * self.spacing
                ]
            )



        return np.array(
            vertices,
            dtype="f4"
        )



    # ========================================================
    # Render Grid
    # ========================================================

    def render(self):


        self.shader.use()



        self.shader.set_vector(
            "color",
            (
                0.35,
                0.35,
                0.35
            )
        )



        self.mesh.render(
            moderngl.LINES
        )