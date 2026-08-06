# ============================================================
# CrashPhys Studio
# File: engine/core/workshop_browser.py
# Version: 0.1.0
#
# Workshop Browser
#
# Handles:
# - Workshop addon discovery
# - Addon selection
# - GMA extraction
# - Model scanning
# - Asset registration
#
# ============================================================


from engine.core.workshop_manager import WorkshopManager
from engine.core.gmad_importer import GMADImporter
from engine.core.gmod_scanner import GModScanner





class WorkshopBrowser:


    def __init__(
        self,
        workshop_folder,
        gmad_path,
        workspace,
        asset_manager
    ):


        print(
            "[Workshop] Browser Initialized"
        )


        self.asset_manager = asset_manager



        self.manager = WorkshopManager(

            workshop_folder

        )


        self.importer = GMADImporter(

            gmad_path,

            workspace

        )


        self.scanner = GModScanner()



        self.addons = []





    # ========================================================
    # Scan Workshop
    # ========================================================


    def scan_workshop(
        self
    ):


        self.addons = self.manager.scan()


        print(

            "[Workshop] Addons Found:",

            len(self.addons)

        )


        return self.addons





    # ========================================================
    # Get Addon List
    # ========================================================


    def get_addons(
        self
    ):


        return self.manager.get_names()





    # ========================================================
    # Load Addon
    # ========================================================


    def load_addon(
        self,
        index
    ):


        path = self.manager.get_path(

            index

        )


        if not path:


            print(

                "[Workshop] Invalid Addon"

            )


            return []





        print(

            "[Workshop] Extracting:",

            path

        )



        extracted = self.importer.extract(

            path

        )



        print(

            "[Workshop] Extracted:",

            extracted

        )





        models = self.scanner.scan(

            extracted

        )



        print(

            "[Workshop] Models Found:",

            len(models)

        )





        self.asset_manager.import_models(

            models

        )



        return models