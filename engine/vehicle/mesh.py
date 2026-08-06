# ============================================================
# CrashPhys Studio
# File: engine/vehicle/mesh.py
# Version: 0.4.0
#
# Mesh System
#
# Handles:
# - OpenGL buffers
# - VAO creation
# - Mesh rendering
# - Primitive generation
# - Vehicle mesh support
#
# Wheel update:
# - Cylinder axis corrected to X
# - Vehicle coordinate system preserved
#
# ============================================================


import numpy as np
import moderngl
import math






class Mesh:


    def __init__(
        self,
        ctx,
        vertices
    ):


        self.ctx = ctx


        self.vertices = np.array(

            vertices,

            dtype="f4"

        )


        self.vbo = None

        self.vao = None



        print(
            "[Mesh] Created"
        )






    # ========================================================
    # VAO
    # ========================================================


    def create_vao(
        self,
        shader
    ):


        if hasattr(shader, "program"):

            program = shader.program

        else:

            program = shader




        self.vbo = self.ctx.buffer(

            self.vertices.tobytes()

        )



        self.vao = self.ctx.vertex_array(

            program,

            [

                (

                    self.vbo,

                    "3f",

                    "in_position"

                )

            ]

        )



        print(
            "[Mesh] VAO Created"
        )







    # ========================================================
    # Render
    # ========================================================


    def render(
        self,
        mode=moderngl.TRIANGLES
    ):


        if self.vao is None:

            print(
                "[Mesh] No VAO"
            )

            return



        self.vao.render(

            mode

        )







    # ========================================================
    # Destroy
    # ========================================================


    def destroy(
        self
    ):


        if self.vao:

            self.vao.release()


        if self.vbo:

            self.vbo.release()







# ============================================================
# BOX
# ============================================================


def create_box(

    width,
    height,
    length

):


    x = width / 2

    y = height / 2

    z = length / 2



    return [


        -x,-y,-z,
         x,-y,-z,
         x, y,-z,

         x, y,-z,
        -x, y,-z,
        -x,-y,-z,


        -x,-y,z,
         x,-y,z,
         x, y,z,

         x, y,z,
        -x, y,z,
        -x,-y,z,


        -x,-y,-z,
        -x, y,-z,
        -x, y,z,

        -x, y,z,
        -x,-y,z,
        -x,-y,-z,


         x,-y,-z,
         x, y,-z,
         x, y,z,

         x, y,z,
         x,-y,z,
         x,-y,-z,


        -x,-y,-z,
         x,-y,-z,
         x,-y,z,

         x,-y,z,
        -x,-y,z,
        -x,-y,-z,


        -x,y,-z,
         x,y,-z,
         x,y,z,

         x,y,z,
        -x,y,z,
        -x,y,-z,

    ]









# ============================================================
# WHEEL CYLINDER
#
# Axis:
# X = axle
#
# Radius:
# Y/Z
#
# ============================================================


def create_cylinder(

    radius,

    depth,

    segments=32

):


    vertices = []



    half = depth / 2




    for i in range(segments):


        a1 = (

            i / segments

        ) * math.tau



        a2 = (

            (i + 1) / segments

        ) * math.tau





        y1 = math.cos(a1) * radius

        z1 = math.sin(a1) * radius



        y2 = math.cos(a2) * radius

        z2 = math.sin(a2) * radius





        # side


        vertices += [


            -half,y1,z1,

             half,y1,z1,

             half,y2,z2,



            -half,y1,z1,

             half,y2,z2,

            -half,y2,z2,


        ]




        # left cap


        vertices += [


            -half,0,0,

            -half,y2,z2,

            -half,y1,z1,


        ]




        # right cap


        vertices += [


             half,0,0,

             half,y1,z1,

             half,y2,z2,


        ]




    return vertices







# ============================================================
# Vehicle Mesh
# ============================================================


class VehicleMesh(Mesh):


    def __init__(
        self,
        ctx,
        vertices
    ):


        super().__init__(

            ctx,

            vertices

        )


        print(
            "[VehicleMesh] Created"
        )