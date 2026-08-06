# ============================================================
# CrashPhys Studio
# File: engine/project/project.py
# Version: 0.2.0
#
# Project System
#
# Handles:
# - Project creation
# - Project loading
# - Project saving
# - Project metadata
# - Scene tracking
# - Asset tracking
#
# ============================================================


import os
import json





class Project:


    def __init__(
        self,
        name="Untitled Project",
        path=None
    ):


        #
        # Identity
        #

        self.name = name


        #
        # Location
        #

        self.path = path



        #
        # State
        #

        self.loaded = False



        #
        # Project Data
        #

        self.data = {


            "name": self.name,

            "version": "0.2.0",


            "assets": [],


            "scenes": [],


            "active_scene": None,


            "settings": {


                "engine": "CrashPhys Studio",

                "beta": True

            }

        }



        print(
            "[Project] Initialized:",
            self.name
        )





    # ========================================================
    # Create Project
    # ========================================================


    def create(
        self
    ):


        if not self.path:


            print(
                "[Project] No Path"
            )


            return False





        folders = [


            self.path,


            os.path.join(
                self.path,
                "assets"
            ),


            os.path.join(
                self.path,
                "scenes"
            )


        ]



        for folder in folders:


            os.makedirs(
                folder,
                exist_ok=True
            )



        self.save()


        self.loaded = True



        print(
            "[Project] Created:",
            self.path
        )


        return True





    # ========================================================
    # Save
    # ========================================================


    def save(
        self
    ):


        if not self.path:


            return False





        file_path = os.path.join(

            self.path,

            "project.json"

        )



        with open(

            file_path,

            "w"

        ) as file:


            json.dump(

                self.data,

                file,

                indent=4

            )



        print(
            "[Project] Saved"
        )


        return True





    # ========================================================
    # Load
    # ========================================================


    def load(
        self
    ):


        if not self.path:


            return False





        file_path = os.path.join(

            self.path,

            "project.json"

        )



        if not os.path.exists(
            file_path
        ):


            print(
                "[Project] Missing project.json"
            )


            return False





        with open(

            file_path,

            "r"

        ) as file:


            self.data = json.load(
                file
            )



        self.name = self.data.get(

            "name",

            self.name

        )



        self.loaded = True



        print(
            "[Project] Loaded:",
            self.name
        )


        return True





    # ========================================================
    # Scenes
    # ========================================================


    def add_scene(
        self,
        scene_name
    ):


        if scene_name not in self.data["scenes"]:


            self.data["scenes"].append(
                scene_name
            )



            print(
                "[Project] Scene Added:",
                scene_name
            )





    def set_active_scene(
        self,
        scene_name
    ):


        self.data["active_scene"] = scene_name



        print(
            "[Project] Active Scene:",
            scene_name
        )





    # ========================================================
    # Assets
    # ========================================================


    def add_asset(
        self,
        asset_path
    ):


        if asset_path not in self.data["assets"]:


            self.data["assets"].append(
                asset_path
            )



            print(
                "[Project] Asset Added:",
                asset_path
            )





    # ========================================================
    # Data Access
    # ========================================================


    def set_data(
        self,
        key,
        value
    ):


        self.data[key] = value





    def get_data(
        self,
        key,
        default=None
    ):


        return self.data.get(

            key,

            default

        )