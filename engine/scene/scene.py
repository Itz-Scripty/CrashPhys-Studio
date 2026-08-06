# ============================================================
# CrashPhys Studio
# File: engine/scene.py
# Version: 0.2.0
#
# Scene System
#
# Handles:
# - Object storage
# - Object updates
# - Object drawing
# - Scene management
#
# ============================================================



class Scene:



    def __init__(
        self,
        name="Scene"
    ):


        self.name = name


        self.objects = []



        print(
            "[Scene] Created:",
            self.name
        )





    # ========================================================
    # Add Object
    # ========================================================


    def add_object(
        self,
        obj
    ):


        self.objects.append(
            obj
        )


        print(
            "[Scene] Added:",
            obj.name
        )





    # ========================================================
    # Remove Object
    # ========================================================


    def remove_object(
        self,
        obj
    ):


        if obj in self.objects:


            self.objects.remove(
                obj
            )


            print(
                "[Scene] Removed:",
                obj.name
            )





    # ========================================================
    # Update
    # ========================================================


    def update(
        self,
        delta_time
    ):


        for obj in self.objects:



            if hasattr(
                obj,
                "update"
            ):


                try:

                    obj.update(
                        delta_time
                    )


                except Exception as error:


                    print(
                        "[Scene] Update Error:",
                        error
                    )





    # ========================================================
    # Draw
    # ========================================================


    def draw(
        self
    ):


        for obj in self.objects:



            if hasattr(
                obj,
                "draw"
            ):


                try:

                    obj.draw()


                except Exception as error:


                    print(
                        "[Scene] Draw Error:",
                        error
                    )





    # ========================================================
    # Find
    # ========================================================


    def find(
        self,
        name
    ):


        for obj in self.objects:


            if obj.name == name:

                return obj



        return None