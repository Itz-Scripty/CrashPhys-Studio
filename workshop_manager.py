import os


class WorkshopManager:

    def __init__(self, workshop_folder):

        self.workshop_folder = workshop_folder

        self.addons = []


    # ============================================
    # Scan Workshop
    # ============================================

    def scan(self):

        self.addons.clear()


        if not os.path.exists(self.workshop_folder):

            return []


        for root, folders, files in os.walk(self.workshop_folder):

            for file in files:

                if file.lower().endswith(".gma"):

                    full_path = os.path.join(
                        root,
                        file
                    )


                    self.addons.append({

                        "name": file,

                        "path": full_path

                    })


        return self.addons


    # ============================================
    # Names
    # ============================================

    def get_names(self):

        return [

            addon["name"]

            for addon in self.addons

        ]


    # ============================================
    # Path
    # ============================================

    def get_path(self, index):

        if index < 0 or index >= len(self.addons):

            return None


        return self.addons[index]["path"]