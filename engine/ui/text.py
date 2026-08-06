# ============================================================
# CrashPhys Studio
# File: engine/ui/text.py
# Version: 0.2.0
#
# UI Text System
#
# Handles:
# - Text objects
# - Text positioning
# - Text rendering connection
# - UI text preparation
#
# ============================================================



from engine.ui.font import default_font





class Text:


    def __init__(
        self,
        value,
        x=0,
        y=0,
        size=None
    ):


        #
        # Content
        #

        self.value = str(value)



        #
        # Position
        #

        self.x = x

        self.y = y



        #
        # Font
        #

        self.font = default_font



        if size:

            self.size = size

        else:

            self.size = self.font.size



        #
        # Renderer connection
        #

        self.renderer = None



        #
        # State
        #

        self.visible = True



        print(
            "[UI] Text Created:",
            self.value
        )





    # ========================================================
    # Renderer
    # ========================================================


    def set_renderer(
        self,
        renderer
    ):


        self.renderer = renderer





    # ========================================================
    # Position
    # ========================================================


    def set_position(
        self,
        x,
        y
    ):


        self.x = x

        self.y = y





    # ========================================================
    # Update
    # ========================================================


    def update(
        self,
        delta_time
    ):

        pass





    # ========================================================
    # Draw
    # ========================================================


    def draw(
        self
    ):


        if not self.visible:

            return



        #
        # Send to real renderer
        #

        if self.renderer:


            self.renderer.draw_text(

                self

            )


        else:


            print(
                "[UI] Text Renderer Missing:",
                self.value
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