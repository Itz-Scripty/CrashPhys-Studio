# ============================================================
# CrashPhys Studio
# File: engine/renderer/vehicle_renderer.py
#
# Vehicle Renderer v0.5.0
#
# Handles:
# - Vehicle body rendering
# - Wheel rendering
# - Suspension visualization
# - Vehicle component debug rendering
#
# IMPORTANT:
# - Wheel transforms preserved
# - Wheel mesh orientation preserved
# - Suspension added separately
#
# ============================================================


import numpy as np
import moderngl


from engine.vehicle.mesh import (
    VehicleMesh,
    create_box,
    create_cylinder
)





class VehicleRenderer:



    def __init__(
        self,
        ctx,
        shader
    ):


        self.ctx = ctx

        self.shader = shader



        print(
            "[Renderer] Creating Vehicle Renderer"
        )





        # ====================================================
        # BODY
        # ====================================================


        self.body = VehicleMesh(

            ctx,

            create_box(

                2.8,
                0.8,
                5.0

            )

        )


        self.body.create_vao(

            shader

        )






        # ====================================================
        # WHEELS
        # ====================================================


        self.wheels = {}



        for name in [

            "FrontLeft",
            "FrontRight",
            "RearLeft",
            "RearRight"

        ]:


            wheel = VehicleMesh(

                ctx,

                create_cylinder(

                    0.45,

                    0.35

                )

            )


            wheel.create_vao(

                shader

            )


            self.wheels[name] = wheel





        # ====================================================
        # SUSPENSION VISUAL
        # ====================================================


        self.suspension_parts = {}



        for name in [

            "FrontLeft",
            "FrontRight",
            "RearLeft",
            "RearRight"

        ]:


            suspension = VehicleMesh(

                ctx,

                create_cylinder(

                    0.08,

                    0.7

                )

            )


            suspension.create_vao(

                shader

            )


            self.suspension_parts[name] = suspension






        print(
            "[Renderer] Vehicle Renderer Initialized"
        )







    # ========================================================
    # Translation
    # ========================================================


    def translation_matrix(
        self,
        x,
        y,
        z
    ):


        matrix = np.identity(

            4,

            dtype="f4"

        )


        matrix[3][0] = x

        matrix[3][1] = y

        matrix[3][2] = z



        return matrix







    # ========================================================
    # Draw
    # ========================================================


    def draw(
        self,
        vehicle=None
    ):


        if vehicle is None:

            return





        vehicle_matrix = np.identity(

            4,

            dtype="f4"

        )



        if hasattr(

            vehicle,

            "transform"

        ):


            vehicle_matrix = np.array(

                vehicle.transform.get_matrix(),

                dtype="f4"

            )







        # ====================================================
        # BODY
        # ====================================================


        self.shader.set_color(

            "color",

            (
                0.8,
                0.15,
                0.1
            )

        )



        self.shader.set_matrix(

            "model",

            vehicle_matrix

        )


        self.body.render(

            moderngl.TRIANGLES

        )







        if not hasattr(

            vehicle,

            "wheels"

        ):

            return







        # ====================================================
        # WHEELS
        # ====================================================


        self.shader.set_color(

            "color",

            (
                0.03,
                0.03,
                0.03
            )

        )





        for wheel in vehicle.wheels:



            if wheel.name not in self.wheels:

                continue





            wheel_matrix = np.array(

                vehicle_matrix,

                copy=True

            )



            wheel_matrix = (

                wheel_matrix

                @

                self.translation_matrix(

                    wheel.position[0],

                    wheel.position[1],

                    wheel.position[2]

                )

            )





            self.shader.set_matrix(

                "model",

                wheel_matrix

            )



            self.wheels[wheel.name].render(

                moderngl.TRIANGLES

            )








        # ====================================================
        # SUSPENSION DEBUG
        # ====================================================


        if not hasattr(

            vehicle,

            "suspension"

        ):

            return





        self.shader.set_color(

            "color",

            (
                0.1,
                0.8,
                0.2
            )

        )






        for suspension in vehicle.suspension:



            wheel = suspension.wheel



            if wheel is None:

                continue



            if wheel.name not in self.suspension_parts:

                continue






            suspension_matrix = np.array(

                vehicle_matrix,

                copy=True

            )




            # place suspension above wheel


            suspension_matrix = (

                suspension_matrix

                @

                self.translation_matrix(

                    wheel.position[0],

                    wheel.position[1] + 0.35,

                    wheel.position[2]

                )

            )






            self.shader.set_matrix(

                "model",

                suspension_matrix

            )





            self.suspension_parts[wheel.name].render(

                moderngl.TRIANGLES

            )








    # ========================================================
    # Compatibility
    # ========================================================


    def render(

        self,

        vehicle=None

    ):


        self.draw(

            vehicle

        )