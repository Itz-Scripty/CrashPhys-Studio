# ============================================================
# CrashPhys Studio
# File: engine/core/workshop_manager.py
# Version: 0.3.0
#
# Garry's Mod Workshop Manager
#
# Handles:
# - Workshop scanning
# - GMA discovery
# - Addon metadata
# - GMAD extraction
# - Model scanning
# - Asset registration
#
# ============================================================


import os


from engine.core.gmad_importer import GMADImporter
from engine.core.gmod_scanner import GModScanner
from engine.assets.asset_manager import AssetManager





class WorkshopManager:


    def __init__(
        self,
        workshop_folder,
        gmad_path=None,
        workspace="workspace"
    ):


        self.workshop_folder = workshop_folder


        self.workspace = workspace


        self.gmad_path = gmad_path


        self.addons = []


        self.scanner = GModScanner()


        self.assets = AssetManager()


        self.importer = None


        if gmad_path:


            self.importer = GMADImporter(

                gmad_path,

                workspace

            )



        print(

            "[Workshop] Manager Initialized"

        )





    # ========================================================
    # Scan Workshop
    # ========================================================


    def scan(
        self
    ):


        print(

            "[Workshop] Scanning:",

            self.workshop_folder

        )



        self.addons.clear()



        if not os.path.exists(

            self.workshop_folder

        ):


            print(

                "[Workshop] Folder Missing"

            )


            return []





        for root, folders, files in os.walk(

            self.workshop_folder

        ):


            for file in files:


                if not file.lower().endswith(

                    ".gma"

                ):

                    continue



                path = os.path.join(

                    root,

                    file

                )



                self.addons.append({


                    "name": file,


                    "path": path,


                    "folder": root,


                    "size": os.path.getsize(path)


                })





        print(

            "[Workshop] Found",

            len(self.addons),

            "addons"

        )


        return self.addons





    # ========================================================
    # Import Addon
    # ========================================================


    def import_addon(
        self,
        index
    ):


        if not self.importer:


            print(

                "[Workshop] GMAD Importer Missing"

            )


            return None




        path = self.get_path(

            index

        )



        if not path:


            return None




        print(

            "[Workshop] Extracting:",

            path

        )



        folder = self.importer.extract(

            path

        )



        print(

            "[Workshop] Extracted:",

            folder

        )



        return self.scan_models(

            folder

        )





    # ========================================================
    # Scan Extracted Models
    # ========================================================


    def scan_models(
        self,
        folder
    ):


        print(

            "[Workshop] Scanning Models"

        )



        models = self.scanner.scan(

            folder

        )



        for model in models:


            asset = {


                "name":

                    os.path.basename(model),


                "path":

                    model,


                "type":

                    "model"


            }



            self.assets.register(

                asset

            )



        print(

            "[Workshop] Models Found:",

            len(models)

        )


        return models





    # ========================================================
    # Access
    # ========================================================


    def get_addons(
        self
    ):


        return self.addons





    def get_names(
        self
    ):


        return [


            addon["name"]


            for addon in self.addons


        ]





    def get_path(
        self,
        index
    ):


        if index < 0:

            return None



        if index >= len(self.addons):

            return None



        return self.addons[index]["path"]





    # ========================================================
    # Find
    # ========================================================


    def find(
        self,
        name
    ):


        name = name.lower()



        for addon in self.addons:


            if addon["name"].lower() == name:


                return addon



        return None





    # ========================================================
    # Stats
    # ========================================================


    def get_stats(
        self
    ):


        return {


            "addons":

                len(self.addons),


            "assets":

                len(self.assets.assets)


        }