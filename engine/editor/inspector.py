# ============================================================
# CrashPhys Studio
# File: engine/editor/inspector.py
# Version: 0.5.0
#
# Inspector System
#
# Beta 0.1 Optimization
#
# Handles:
# - Selected object inspection
# - Vehicle data extraction
# - Component information
# - Transform information
# - Cached inspector data
# - Reduced UI rebuilds
#
# ============================================================





class Inspector:


    def __init__(
        self
    ):


        self.target = None


        #
        # Cached UI data
        #

        self.cached_data = {}


        #
        # Rebuild control
        #

        self.dirty = True



        print(

            "[Inspector] Initialized"

        )







    # ========================================================
    # Selection
    # ========================================================


    def inspect(
        self,
        obj
    ):


        self.select(

            obj

        )







    def select(
        self,
        obj
    ):


        if obj == self.target:


            return





        self.target = obj


        self.dirty = True





        print(

            "[Inspector] Selected:",

            type(obj).__name__

        )







    def clear(
        self
    ):


        self.target = None


        self.cached_data.clear()


        self.dirty = True





        print(

            "[Inspector] Cleared"

        )







    # ========================================================
    # Refresh
    # ========================================================


    def refresh(
        self
    ):


        self.cached_data = self.build_data()


        self.dirty = False







    # ========================================================
    # Data
    # ========================================================


    def get_data(
        self
    ):


        if self.dirty:


            self.refresh()





        return self.cached_data







    # ========================================================
    # Build Data
    # ========================================================


    def build_data(
        self
    ):


        if self.target is None:


            return {


                "Status":

                    "Nothing Selected"


            }





        obj = self.target



        data = {}





        #
        # Basic
        #

        data["Name"] = getattr(

            obj,

            "name",

            "Unknown"

        )



        data["Type"] = type(obj).__name__





        if hasattr(

            obj,

            "id"

        ):


            data["ID"] = obj.id





        if hasattr(

            obj,

            "enabled"

        ):


            data["Enabled"] = obj.enabled





        if hasattr(

            obj,

            "destroyed"

        ):


            data["Destroyed"] = obj.destroyed







        #
        # Transform
        #

        if hasattr(

            obj,

            "transform"

        ):



            transform = obj.transform



            data["Position"] = str(

                transform.position

            )



            data["Rotation"] = str(

                transform.rotation

            )



            data["Scale"] = str(

                transform.scale

            )







        #
        # Engine
        #

        if hasattr(

            obj,

            "engine"

        ):



            engine = obj.engine



            data["ENGINE"] = "----------"



            data["Horsepower"] = getattr(

                engine,

                "horsepower",

                0

            )



            data["Health"] = getattr(

                engine,

                "health",

                100

            )







        #
        # Body
        #

        if hasattr(

            obj,

            "body"

        ):



            data["BODY"] = "----------"



            data["Body"] = getattr(

                obj.body,

                "name",

                "Vehicle Body"

            )







        #
        # Wheels
        #

        if hasattr(

            obj,

            "wheels"

        ):



            data["WHEELS"] = "----------"



            data["Wheel Count"] = len(

                obj.wheels

            )







        #
        # Suspension
        #

        if hasattr(

            obj,

            "suspension"

        ):



            data["SUSPENSION"] = "----------"



            data["Suspension Count"] = len(

                obj.suspension

            )







        return data