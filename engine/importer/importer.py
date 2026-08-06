# ============================================================
# CrashPhys Studio
# File: engine/importer/importer.py
# Version: 0.1.0
#
# Asset Importer System
#
# Handles:
# - File importing foundation
# - Asset detection
# - Import pipeline preparation
#
# ============================================================


import os





class Importer:


    def __init__(
        self
    ):


        print(
            "[Importer] Initialized"
        )





    # ========================================================
    # Detect File
    # ========================================================


    def detect_type(
        self,
        path
    ):


        extension = os.path.splitext(
            path
        )[1].lower()



        if extension in [

            ".obj",

            ".fbx",

            ".gltf",

            ".glb"

        ]:


            return "model"



        if extension in [

            ".png",

            ".jpg",

            ".jpeg"

        ]:


            return "texture"



        return "unknown"





    # ========================================================
    # Import
    # ========================================================


    def import_file(
        self,
        path
    ):


        if not os.path.exists(
            path
        ):


            print(
                "[Importer] Missing:",
                path
            )


            return None





        asset_type = self.detect_type(
            path
        )



        print(
            "[Importer] Importing:",
            path,
            "Type:",
            asset_type
        )


        return {


            "path": path,

            "type": asset_type


        }