# ============================================================
# CrashPhys Studio
# File: engine/ui/inspector_panel.py
# Version: 0.8.1
#
# Inspector Panel
#
# Handles:
# - Selected object information
# - Inspector rendering
# - Mouse routing
# - Panel interaction
#
# ============================================================


from engine.ui.panel import Panel
from engine.ui.text import Text





class InspectorPanel(Panel):


    def __init__(
        self,
        inspector=None,
        **kwargs
    ):


        super().__init__(
            "Inspector",
            **kwargs
        )


        self.inspector = inspector


        self.lines = []


        self.renderer = None



        print(
            "[UI] Inspector Panel Created"
        )





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





    # ========================================================
    # Refresh
    # ========================================================


    def refresh(
        self
    ):


        self.lines.clear()


        if not self.inspector:


            self.add_text(
                "No Inspector",
                self.x + 10,
                self.y + 40
            )


            return





        data = self.inspector.get_data()


        y = self.y + 40



        for key, value in data.items():


            self.add_text(

                f"{key}: {value}",

                self.x + 10,

                y

            )


            y += 22





        if self.renderer:


            self.set_renderer(
                self.renderer
            )





    # ========================================================
    # Text
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
    # Update
    # ========================================================


    def update(
        self,
        delta_time
    ):


        super().update(
            delta_time
        )


        self.refresh()





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


        #
        # Needed for UI routing
        #
        # Inspector currently has no clickable controls
        #


        self.hovered = self.inside(
            x,
            y
        )





    def mouse_press(
        self,
        x,
        y,
        button
    ):


        pass





    def mouse_release(
        self,
        x,
        y,
        button
    ):


        pass





    # ========================================================
    # Draw
    # ========================================================


    def draw(
        self
    ):


        super().draw()



        for line in self.lines:

            line.draw()