# ============================================================
# CrashPhys Studio
# File: engine/ui/titlebar.py
# Version: 0.3.0
#
# UI Title Bar System
#
# Handles:
# - Panel headers
# - Panel titles
# - Title rendering
# - Panel movement tracking
#
# ============================================================


from engine.ui.font import default_font





class TitleBar:


    def __init__(
        self,
        panel,
        height=24
    ):


        #
        # Owner Panel
        #

        self.panel = panel



        #
        # Layout
        #

        self.height = height


        self.x = panel.x

        self.y = panel.y



        #
        # State
        #

        self.visible = True



        #
        # Font
        #

        self.font = default_font



        print(
            "[UI] TitleBar Created:",
            panel.name
        )





    # ========================================================
    # Position Sync
    # ========================================================


    def update_position(
        self
    ):


        #
        # Follow panel movement
        #

        self.x = self.panel.x

        self.y = self.panel.y





    # ========================================================
    # Update
    # ========================================================


    def update(
        self,
        delta_time
    ):


        self.update_position()





    # ========================================================
    # Draw
    # ========================================================


    def draw(
        self
    ):


        if not self.visible:

            return



        #
        # Keep position synced
        #

        self.update_position()



        #
        # Draw title text
        #

        x = self.x + 8

        y = self.y + 16



        self.font.draw_text(

            self.panel.title,

            x,

            y

        )





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