# ============================================================
# CrashPhys Studio
# File: engine/assets/asset_scanner.py
# Version: 0.3.0
#
# GMA Asset Scanner
#
# Handles:
# - Extracted GMA scanning
# - Models
# - Materials
# - Textures
# - Scripts
# - Asset indexing
#
# Pipeline:
#
# .gma
#   |
# GMAD Importer
#   |
# Extracted Folder
#   |
# Asset Scanner
#   |
# Asset Manager
#
# ============================================================


import os


from engine.assets.asset import Asset





class AssetScanner:


    def __init__(
        self,
        workspace=None
    ):


        self.workspace = workspace


        self.assets = []


        print(
            "[Assets] GMA Scanner Initialized"
        )





    # ========================================================
    # Scan Extracted GMA
    # ========================================================


    def scan(
        self,
        folder
    ):


        if not folder:


            print(
                "[Assets] No folder supplied"
            )


            return []



        if not os.path.exists(folder):


            print(
                "[Assets] Missing:",
                folder
            )


            return []



        self.assets.clear()



        print(
            "[Assets] Scanning GMA:",
            folder
        )



        for root, dirs, files in os.walk(folder):


            for file in files:


                asset_type = self.get_asset_type(
                    file
                )


                if not asset_type:

                    continue



                path = os.path.join(
                    root,
                    file
                )



                asset = Asset(

                    file,

                    path

                )


                asset.asset_type = asset_type



                self.assets.append(
                    asset
                )



        print(
            "[Assets] Found:",
            len(self.assets)
        )



        return self.assets





    # ========================================================
    # Compatibility
    # ========================================================


    def scan_addons(
        self,
        addons_path=None
    ):


        print(
            "[Assets] scan_addons deprecated - use scan()"
        )


        return []





    # ========================================================
    # Detect Type
    # ========================================================


    def get_asset_type(
        self,
        filename
    ):


        extension = os.path.splitext(
            filename
        )[1].lower()



        types = {


            ".mdl":
            "model",


            ".vmt":
            "material",


            ".vtf":
            "texture",


            ".lua":
            "script",


            ".json":
            "config",


            ".txt":
            "text"


        }



        return types.get(
            extension
        )





    # ========================================================
    # Query
    # ========================================================


    def get_assets(
        self,
        asset_type=None
    ):


        if not asset_type:

            return self.assets



        return [

            asset

            for asset in self.assets

            if asset.asset_type == asset_type

        ]





    # ========================================================
    # Debug
    # ========================================================


    def print_assets(
        self
    ):


        print(
            "========== GMA ASSETS =========="
        )


        for asset in self.assets:


            print(

                asset.asset_type,

                ":",

                asset.path

            )


        print(
            "==============================="
        )