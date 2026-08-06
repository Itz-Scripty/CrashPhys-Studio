# ============================================================
# CrashPhys Studio
# File: engine/renderer/shader.py
#
# Shader wrapper
#
# Handles:
# - Shader program creation
# - Matrix uniforms
# - Color uniforms
# - Vector uniforms
# - Generic uniforms
#
# ============================================================


import numpy as np



class Shader:


    def __init__(
        self,
        ctx,
        vertex_shader,
        fragment_shader
    ):


        self.ctx = ctx


        self.program = self.ctx.program(

            vertex_shader=vertex_shader,

            fragment_shader=fragment_shader

        )


        print(
            "[Shader] Created"
        )




    # ========================================================
    # Bind Shader
    # ========================================================


    def use(self):

        pass




    # ========================================================
    # Matrix
    # ========================================================


    def set_matrix(
        self,
        name,
        matrix
    ):


        if name not in self.program:

            return



        matrix = np.array(

            matrix,

            dtype="f4"

        )



        self.program[name].write(

            matrix.tobytes()

        )




    # ========================================================
    # Color Vector3
    # ========================================================


    def set_color(
        self,
        name,
        color
    ):


        self.set_vector(

            name,

            color

        )




    # ========================================================
    # Vector
    # ========================================================


    def set_vector(
        self,
        name,
        vector
    ):


        if name not in self.program:

            return



        self.program[name].value = (

            float(vector[0]),

            float(vector[1]),

            float(vector[2])

        )




    # ========================================================
    # Float
    # ========================================================


    def set_float(
        self,
        name,
        value
    ):


        if name not in self.program:

            return



        self.program[name].value = float(value)




    # ========================================================
    # Integer
    # ========================================================


    def set_int(
        self,
        name,
        value
    ):


        if name not in self.program:

            return



        self.program[name].value = int(value)




    # ========================================================
    # Generic Uniform
    # ========================================================


    def set_uniform(
        self,
        name,
        value
    ):


        if name not in self.program:

            return



        self.program[name].value = value




    # ========================================================
    # Destroy
    # ========================================================


    def destroy(self):


        if self.program:

            self.program.release()


        print(
            "[Shader] Destroyed"
        )