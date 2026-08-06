# ============================================================
# CrashPhys Studio
# File: engine/assets/asset.py
# Version: 0.2.0
#
# Asset Object
#
# Handles:
# - Asset identity
# - Source tracking
# - GMA ownership
# - Asset types
# - Import state
#
# ============================================================


import os



class Asset:


    def __init__(
        self,
        name="Asset",
        path=None,
        asset_type="unknown",
        source_gma=None
    ):


        #
        # Identity
        #

        self.name = name


        self.path = path


        #
        # Type
        #

        self.asset_type = asset_type


        #
        # Workshop source
        #

        self.source_gma = source_gma



        #
        # State
        #

        self.loaded = False


        self.id = None



        print(
            "[Asset] Created:",
            self.name
        )





    # ========================================================
    # Helpers
    # ========================================================


    def exists(
        self
    ):


        if not self.path:

            return False


        return os.path.exists(
            self.path
        )





    def get_extension(
        self
    ):


        if not self.path:

            return ""


        return os.path.splitext(
            self.path
        )[1].lower()





    # ========================================================
    # Load
    # ========================================================


    def load(
        self
    ):


        if not self.exists():


            print(
                "[Asset] Missing:",
                self.path
            )


            return False



        self.loaded = True


        print(
            "[Asset] Loaded:",
            self.name
        )


        return True





    # ========================================================
    # Unload
    # ========================================================


    def unload(
        self
    ):


        self.loaded = False


        print(
            "[Asset] Unloaded:",
            self.name
        )





    # ========================================================
    # Debug
    # ========================================================


    def info(
        self
    ):


        return {


            "name":
                self.name,


            "path":
                self.path,


            "type":
                self.asset_type,


            "gma":
                self.source_gma,


            "loaded":
                self.loaded


        }





    def __repr__(
        self
    ):


        return (

            f"<Asset {self.asset_type}: {self.name}>"

        )