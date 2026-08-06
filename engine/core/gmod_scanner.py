# ============================================================
# CrashPhys Studio
# File: engine/core/gmod_scanner.py
# Version: 0.2.0
#
# GMod Workshop Model Scanner
#
# Handles:
# - Garry's Mod addon scanning
# - Workshop model discovery
# - MDL detection
# - Model categorization
# - Asset metadata
#
# ============================================================


import os





class GModScanner:


    def __init__(self):


        self.models = []


        self.categories = {


            "vehicles": [],

            "parts": [],

            "weapons": [],

            "props": [],

            "other": []


        }



        print(

            "[GMod Scanner] Initialized"

        )





    # ========================================================
    # Scan Folder
    # ========================================================


    def scan(
        self,
        folder
    ):


        print(

            "[GMod Scanner] Scanning:",

            folder

        )



        self.models.clear()



        for category in self.categories:

            self.categories[category].clear()





        if not os.path.exists(folder):


            print(

                "[GMod Scanner] Folder Missing"

            )


            return []





        for root, folders, files in os.walk(folder):


            for file in files:


                if not file.lower().endswith(".mdl"):

                    continue



                full_path = os.path.join(

                    root,

                    file

                )



                relative = os.path.relpath(

                    full_path,

                    folder

                )



                gmod_path = relative.replace(

                    "\\",

                    "/"

                )



                asset = {


                    "name": file,


                    "path": gmod_path,


                    "full_path": full_path,


                    "category": self.classify(

                        gmod_path

                    )


                }





                self.models.append(

                    asset

                )



                self.categories[

                    asset["category"]

                ].append(

                    asset

                )





        print(

            "[GMod Scanner] Found:",

            len(self.models),

            "models"

        )



        return self.models





    # ========================================================
    # Classify
    # ========================================================


    def classify(
        self,
        model
    ):


        lower = model.lower()





        if any(word in lower for word in [

            "vehicle",

            "vehicles",

            "cars",

            "car",

            "truck",

            "jeep",

            "chassis",

            "body"

        ]):


            return "vehicles"







        if any(word in lower for word in [


            "wheel",

            "tire",

            "tyre",

            "engine",

            "spoiler",

            "bumper",

            "door"


        ]):


            return "parts"







        if any(word in lower for word in [


            "weapon",

            "weapons",

            "gun",

            "rifle",

            "pistol"


        ]):


            return "weapons"







        if any(word in lower for word in [


            "props",

            "prop"


        ]):


            return "props"





        return "other"





    # ========================================================
    # Get Models
    # ========================================================


    def get_models(
        self
    ):


        return self.models





    # ========================================================
    # Get Category
    # ========================================================


    def get_category(
        self,
        category
    ):


        return self.categories.get(

            category,

            []

        )





    # ========================================================
    # Stats
    # ========================================================


    def get_stats(
        self
    ):


        return {


            "total": len(self.models),


            "vehicles": len(

                self.categories["vehicles"]

            ),


            "parts": len(

                self.categories["parts"]

            ),


            "weapons": len(

                self.categories["weapons"]

            ),


            "props": len(

                self.categories["props"]

            )


        }