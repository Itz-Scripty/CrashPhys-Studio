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



    # ============================================
    # Scan Folder
    # ============================================

    def scan(self, folder):

        self.models.clear()


        for category in self.categories:

            self.categories[category].clear()



        if not os.path.exists(folder):

            return []



        for root, folders, files in os.walk(folder):


            for file in files:


                if file.lower().endswith(".mdl"):


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


                    category = self.classify(
                        gmod_path
                    )


                    self.models.append(
                        gmod_path
                    )


                    self.categories[category].append(
                        gmod_path
                    )



        return self.models



    # ============================================
    # Classify Model
    # ============================================

    def classify(self, model):

        lower = model.lower()



        # Vehicle models

        if any(word in lower for word in [

            "vehicle",
            "vehicles",
            "cars",
            "car",
            "truck",
            "chassis",
            "body"

        ]):

            return "vehicles"



        # Vehicle parts

        if any(word in lower for word in [

            "wheel",
            "tire",
            "tyre",
            "engine",
            "wing",
            "spoiler",
            "bumper",
            "door"

        ]):

            return "parts"



        # Weapons

        if any(word in lower for word in [

            "weapon",
            "weapons",
            "gun",
            "rifle",
            "pistol"

        ]):

            return "weapons"



        # Props

        if any(word in lower for word in [

            "props",
            "prop"

        ]):

            return "props"



        return "other"



    # ============================================
    # Get All Models
    # ============================================

    def get_models(self):

        return self.models



    # ============================================
    # Get Category
    # ============================================

    def get_category(self, category):

        return self.categories.get(
            category,
            []
        )