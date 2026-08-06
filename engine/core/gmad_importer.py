# ============================================================
# CrashPhys Studio
# File: engine/core/gmad_importer.py
# Version: 0.2.0
#
# GMAD Importer
#
# Handles:
# - GMA extraction
# - Workshop addon unpacking
# - Extraction workspace
# - Import tracking
# - Scanner handoff
#
# ============================================================


import os
import shutil
import subprocess





class GMADImporter:


    def __init__(
        self,
        gmad_path,
        workspace
    ):


        self.gmad_path = gmad_path

        self.workspace = workspace


        self.imported = []



        print(

            "[GMAD] Importer Initialized"

        )





    # ========================================================
    # Extract GMA
    # ========================================================


    def extract(
        self,
        gma_file
    ):


        print(

            "[GMAD] Extracting:",

            gma_file

        )



        if not os.path.exists(

            self.gmad_path

        ):


            raise FileNotFoundError(

                "gmad.exe not found."

            )





        if not os.path.exists(

            gma_file

        ):


            raise FileNotFoundError(

                "GMA file not found."

            )





        addon_name = os.path.splitext(

            os.path.basename(

                gma_file

            )

        )[0]





        output_folder = os.path.join(

            self.workspace,

            addon_name

        )





        #
        # Remove old extraction
        #

        if os.path.exists(

            output_folder

        ):


            shutil.rmtree(

                output_folder

            )





        os.makedirs(

            output_folder,

            exist_ok=True

        )





        command = [


            self.gmad_path,


            "extract",


            "-file",

            gma_file,


            "-out",

            output_folder,


            "-quiet"


        ]





        result = subprocess.run(

            command,

            capture_output=True,

            text=True

        )





        if result.returncode != 0:


            raise RuntimeError(

                result.stderr

            )





        #
        # Verify extraction
        #

        if not os.path.exists(

            output_folder

        ):


            raise RuntimeError(

                "Extraction failed."

            )





        addon = {


            "name": addon_name,


            "source": gma_file,


            "output": output_folder


        }





        self.imported.append(

            addon

        )





        print(

            "[GMAD] Extracted:",

            output_folder

        )



        return output_folder





    # ========================================================
    # Get Imports
    # ========================================================


    def get_imports(
        self
    ):


        return self.imported





    # ========================================================
    # Check Tool
    # ========================================================


    def validate(
        self
    ):


        return os.path.exists(

            self.gmad_path

        )