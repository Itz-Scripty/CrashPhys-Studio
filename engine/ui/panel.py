
# ============================================================
# CrashPhys Studio
# File: engine/ui/panel.py
# Version: 0.4.0
#
# UI Panel System
#
# Handles:
# - Panel layout
# - Visibility
# - Titles
# - Children
# - Position syncing
# - Text syncing
# - Title bars
#
# ============================================================


from engine.ui.theme import default_theme
from engine.ui.titlebar import TitleBar





class Panel:


    def __init__(
        self,
        name,
        x=0,
        y=0,
        width=200,
        height=200
    ):


        #
        # Identity
        #

        self.name = name

        self.title = name



        #
        # Transform
        #

        self.x = x

        self.y = y

        self.width = width

        self.height = height



        #
        # State
        #

        self.visible = True

        self.enabled = True

        self.active = False



        #
        # Hierarchy
        #

        self.children = []

        self.parent = None



        #
        # Text holders
        #

        self.lines = []



        #
        # Theme
        #

        self.theme = default_theme



        #
        # Title Bar
        #

        self.titlebar = TitleBar(
            self
        )



        print(
            "[UI] Panel Created:",
            self.name
        )





    # ========================================================
    # Update
    # ========================================================


    def update(
        self,
        delta_time
    ):


        if not self.visible:

            return



        for child in self.children:

            child.update(
                delta_time
            )





    # ========================================================
    # Draw
    # ========================================================


    def draw(
        self
    ):


        if not self.visible:

            return



        self.titlebar.draw()



        for line in self.lines:

            line.draw()



        for child in self.children:

            child.draw()





    # ========================================================
    # Child Panels
    # ========================================================


    def add_child(
        self,
        panel
    ):


        panel.parent = self


        self.children.append(
            panel
        )





    def remove_child(
        self,
        panel
    ):


        if panel in self.children:


            panel.parent = None


            self.children.remove(
                panel
            )





    # ========================================================
    # Layout
    # ========================================================


    def resize(
        self,
        width,
        height
    ):


        self.width = width

        self.height = height





    def move(
        self,
        x,
        y
    ):


        self.x = x

        self.y = y



        #
        # Move text with panel
        #

        offset = 40


        for line in self.lines:


            line.set_position(

                self.x + 10,

                self.y + offset

            )


            offset += 22



        #
        # Move children
        #

        for child in self.children:


            child.move(

                child.x,

                child.y

            )





        #
        # Refresh title bar
        #

        if self.titlebar:

            self.titlebar.update_position()





    # ========================================================
    # Visibility
    # ========================================================


    def show(
        self
    ):


        self.visible = True





    def hide(
        self
    ):


        self.visible = False





    # ========================================================
    # State
    # ========================================================


    def enable(
        self
    ):


        self.enabled = True





    def disable(
        self
    ):


        self.enabled = False
