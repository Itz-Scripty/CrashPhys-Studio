# ============================================================
# CrashPhys Studio
# File: engine/editor/picking.py
# Version: 0.1.0
#
# Object Picking System
#
# Handles:
# - Mouse position
# - Screen ray creation
# - Object hit testing
# - Editor selection support
#
# ============================================================


import math





class PickingSystem:


    def __init__(
        self,
        camera
    ):


        self.camera = camera


        self.mouse_x = 0

        self.mouse_y = 0



        print(
            "[Picking] Initialized"
        )





    # ========================================================
    # Mouse
    # ========================================================


    def set_mouse_position(
        self,
        x,
        y
    ):


        self.mouse_x = x

        self.mouse_y = y





    # ========================================================
    # Ray Creation
    # ========================================================


    def create_ray(
        self,
        width,
        height
    ):


        #
        # Convert mouse to normalized coordinates
        #

        ndc_x = (
            (2.0 * self.mouse_x)
            /
            width
        ) - 1.0



        ndc_y = 1.0 - (
            (2.0 * self.mouse_y)
            /
            height
        )



        #
        # Temporary camera ray
        #
        # Later:
        # projection inverse
        # view inverse
        #

        direction = self.camera.front



        origin = self.camera.position



        return (

            origin,

            direction

        )





    # ========================================================
    # Object Test
    # ========================================================


    def test_object(
        self,
        ray,
        obj
    ):


        if not hasattr(
            obj,
            "transform"
        ):

            return False



        origin, direction = ray



        position = (
            obj.transform.position
        )



        #
        # Temporary radius
        #
        # Replace with mesh bounds later
        #

        radius = 2.0



        to_object = (

            position[0] - origin[0],

            position[1] - origin[1],

            position[2] - origin[2]

        )



        distance = (

            to_object[0] * direction[0]

            +

            to_object[1] * direction[1]

            +

            to_object[2] * direction[2]

        )



        if distance < 0:

            return False



        closest = (

            origin[0] + direction[0] * distance,

            origin[1] + direction[1] * distance,

            origin[2] + direction[2] * distance

        )



        difference = (

            position[0] - closest[0],

            position[1] - closest[1],

            position[2] - closest[2]

        )



        hit_distance = math.sqrt(

            difference[0] ** 2

            +

            difference[1] ** 2

            +

            difference[2] ** 2

        )



        return hit_distance <= radius





    # ========================================================
    # Pick
    # ========================================================


    def pick(
        self,
        scene,
        width,
        height
    ):


        ray = self.create_ray(

            width,

            height

        )



        for obj in scene.objects:


            if self.test_object(

                ray,

                obj

            ):


                print(

                    "[Picking] Hit:",
                    obj.name

                )


                return obj



        return None