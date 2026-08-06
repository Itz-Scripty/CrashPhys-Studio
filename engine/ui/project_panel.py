# ============================================================
# CrashPhys Studio
# File: engine/ui/project_panel.py
# Version: 0.4.0
#
# Project Browser Panel
#
# Handles:
# - Workshop display
# - Model asset display
# - Clickable model rows
# - Project tree foundation
#
# Filters:
# - Displays ONLY .mdl files
#
# ============================================================


from engine.ui.panel import Panel
from engine.ui.text import Text
from engine.ui.widgets import AssetRow





class ProjectPanel(Panel):


    MODEL_EXTENSIONS = (
        ".mdl",
    )



    def __init__(
        self,
        asset_manager=None,
        workshop_manager=None,
        **kwargs
    ):


        super().__init__(
            "Project",
            **kwargs
        )


        self.asset_manager = asset_manager

        self.workshop_manager = workshop_manager


        self.lines = []

        self.asset_rows = []


        self.renderer = None


        self.selected_asset = None


        print(
            "[UI] Project Panel Created"
        )


        self.refresh()





    # ========================================================
    # Renderer
    # ========================================================


    def set_renderer(
        self,
        renderer
    ):


        self.renderer = renderer


        for line in self.lines:

            line.set_renderer(
                renderer
            )


        for row in self.asset_rows:

            row.set_renderer(
                renderer
            )


        print(
            "[UI] Project Panel Renderer Connected"
        )





    # ========================================================
    # Asset Filter
    # ========================================================


    def is_model_asset(
        self,
        asset
    ):


        name = asset.name.lower()


        for ext in self.MODEL_EXTENSIONS:

            if name.endswith(ext):

                return True


        return False





    # ========================================================
    # Refresh
    # ========================================================


    def refresh(
        self
    ):


        self.lines.clear()

        self.asset_rows.clear()



        y = self.y + 40



        #
        # Workshop
        #

        self.add_text(
            "Workshop",
            self.x + 10,
            y
        )


        y += 25



        if self.workshop_manager:


            addons = self.workshop_manager.get_addons()


            for addon in addons:


                self.add_text(
                    addon["name"],
                    self.x + 20,
                    y
                )


                y += 20



        else:


            self.add_text(
                "No Workshop Loaded",
                self.x + 20,
                y
            )


            y += 20





        #
        # Assets
        #

        y += 15


        self.add_text(
            "Models",
            self.x + 10,
            y
        )


        y += 30





        model_count = 0



        if self.asset_manager:


            assets = self.asset_manager.list_assets()



            for asset in assets:



                if not self.is_model_asset(asset):

                    continue



                row = AssetRow(

                    asset.name,

                    self.select_asset,

                    x=self.x + 15,

                    y=y,

                    width=self.width - 30,

                    height=24

                )



                self.asset_rows.append(
                    row
                )


                y += 28


                model_count += 1



        else:


            self.add_text(
                "No Assets",
                self.x + 20,
                y
            )



        print(
            "[UI] Models Loaded:",
            model_count
        )



        if self.renderer:


            self.set_renderer(
                self.renderer
            )





    # ========================================================
    # Text Helper
    # ========================================================


    def add_text(
        self,
        text,
        x,
        y
    ):


        line = Text(
            text,
            x,
            y
        )


        self.lines.append(
            line
        )


        if self.renderer:


            line.set_renderer(
                self.renderer
            )





    # ========================================================
    # Selection
    # ========================================================


    def select_asset(
        self,
        asset_name
    ):


        self.selected_asset = asset_name


        print(
            "[Project] Model Selected:",
            asset_name
        )





    # ========================================================
    # Update
    # ========================================================


    def update(
        self,
        delta_time
    ):


        super().update(
            delta_time
        )


        for row in self.asset_rows:

            row.update(
                delta_time
            )





    # ========================================================
    # Move
    # ========================================================


    def move(
        self,
        x,
        y
    ):


        super().move(
            x,
            y
        )


        self.refresh()





    # ========================================================
    # Mouse
    # ========================================================


    def mouse_move(
        self,
        x,
        y
    ):


        for row in self.asset_rows:

            row.mouse_move(
                x,
                y
            )





    def mouse_press(
        self,
        x,
        y,
        button
    ):


        for row in self.asset_rows:

            row.mouse_press(
                x,
                y,
                button
            )





    # ========================================================
    # Draw
    # ========================================================


    def draw(
        self
    ):


        super().draw()



        for line in self.lines:

            line.draw()



        for row in self.asset_rows:

            row.draw()