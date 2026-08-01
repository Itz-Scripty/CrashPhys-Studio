import os
import shutil
import subprocess


class GMADImporter:

    def __init__(self, gmad_path, workspace):

        self.gmad_path = gmad_path
        self.workspace = workspace


    # ============================================
    # Extract Workshop Addon
    # ============================================

    def extract(self, gma_file):

        if not os.path.exists(self.gmad_path):

            raise FileNotFoundError(
                "gmad.exe not found."
            )


        if not os.path.exists(gma_file):

            raise FileNotFoundError(
                "GMA file not found."
            )


        addon_name = os.path.splitext(
            os.path.basename(gma_file)
        )[0]


        output_folder = os.path.join(
            self.workspace,
            addon_name
        )


        # Clean previous extraction

        if os.path.exists(output_folder):

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


        return output_folder