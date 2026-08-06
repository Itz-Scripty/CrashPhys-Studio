# ============================================================
# CrashPhys Studio
# File: engine/assets/asset_manager.py
# Version: 0.6.0
#
# Asset Manager
#
# Beta 0.1 Asset Pipeline
#
# Handles:
# - MDL only asset pipeline
# - Asset registration
# - Model database
# - Folder scanning
# - Duplicate prevention
# - Asset caching
# - Fast lookup
#
# ============================================================


import os


from engine.assets.asset import Asset





class AssetManager:


    #
    # Beta 0.1
    #
    # CrashPhys Studio currently
    # only works with Source models.
    #

    ALLOWED_EXTENSION = ".mdl"





    def __init__(
        self
    ):


        #
        # Name lookup
        #

        self.assets = {}



        #
        # Full path lookup
        #

        self.path_cache = {}



        #
        # Scan cache
        #

        self.scan_cache = {}



        self.next_id = 1



        print(

            "[Asset] MDL Manager Initialized"

        )







    # ========================================================
    # Register Asset
    # ========================================================


    def register(
        self,
        asset
    ):


        if not isinstance(
            asset,
            Asset
        ):


            print(

                "[Asset] Invalid Asset"

            )


            return None





        #
        # Duplicate name
        #

        if asset.name in self.assets:


            return self.assets[asset.name]





        #
        # Assign ID
        #

        asset.id = self.next_id


        self.next_id += 1





        self.assets[asset.name] = asset



        if asset.path:


            self.path_cache[

                asset.path.lower()

            ] = asset





        print(

            "[Asset] Registered:",

            asset.name,

            "ID:",

            asset.id

        )



        return asset







    # ========================================================
    # Register MDL File
    # ========================================================


    def register_file(
        self,
        path
    ):


        extension = os.path.splitext(

            path

        )[1].lower()



        if extension != self.ALLOWED_EXTENSION:


            return None





        #
        # Already loaded
        #

        normalized = os.path.abspath(

            path

        ).lower()



        if normalized in self.path_cache:


            return self.path_cache[

                normalized

            ]





        name = os.path.basename(

            path

        )





        asset = Asset(

            name,

            path

        )



        asset.asset_type = "model"



        return self.register(

            asset

        )









    # ========================================================
    # Scan Folder
    # ========================================================


    def scan_folder(
        self,
        folder
    ):


        folder = os.path.abspath(

            folder

        )





        if not os.path.exists(

            folder

        ):


            print(

                "[Asset] Missing Folder:",

                folder

            )


            return 0





        #
        # Cached scan
        #

        if folder in self.scan_cache:


            print(

                "[Asset] Scan Cache:",

                folder

            )


            return self.scan_cache[

                folder

            ]







        print(

            "[Asset] Scanning MDL:",

            folder

        )



        count = 0





        for root, dirs, files in os.walk(

            folder

        ):



            for file in files:



                if not file.lower().endswith(

                    self.ALLOWED_EXTENSION

                ):


                    continue





                path = os.path.join(

                    root,

                    file

                )





                if self.register_file(

                    path

                ):


                    count += 1







        self.scan_cache[folder] = count





        print(

            "[Asset] MDL Scan Complete:",

            count,

            "Models"

        )



        return count







    # ========================================================
    # Lookup
    # ========================================================


    def get(
        self,
        name
    ):


        return self.assets.get(

            name

        )







    def get_by_path(
        self,
        path
    ):


        return self.path_cache.get(

            os.path.abspath(

                path

            ).lower()

        )







    # ========================================================
    # Search
    # ========================================================


    def search(
        self,
        text
    ):


        text = text.lower()



        return [

            asset

            for asset in self.assets.values()

            if text in asset.name.lower()

        ]







    # ========================================================
    # List
    # ========================================================


    def list_assets(
        self
    ):


        return list(

            self.assets.values()

        )







    # ========================================================
    # Models
    # ========================================================


    def list_models(
        self
    ):


        return [

            asset

            for asset in self.assets.values()

            if asset.asset_type == "model"

        ]







    # ========================================================
    # Remove
    # ========================================================


    def remove(
        self,
        name
    ):


        asset = self.assets.get(

            name

        )


        if not asset:


            return





        del self.assets[name]



        if asset.path:


            self.path_cache.pop(

                asset.path.lower(),

                None

            )







    # ========================================================
    # Cache
    # ========================================================


    def clear_cache(
        self
    ):


        self.scan_cache.clear()



        print(

            "[Asset] Scan Cache Cleared"

        )







    # ========================================================
    # Stats
    # ========================================================


    def stats(
        self
    ):


        return {


            "total":

                len(

                    self.assets

                ),



            "models":

                len(

                    self.list_models()

                )

        }