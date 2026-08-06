# ============================================================
# CrashPhys Studio
# File: engine/ui/text_renderer.py
# Version: 0.5.0
#
# UI Text Renderer
#
# Handles:
# - Cached pyglet labels
# - Real UI text drawing
# - Font connection
# - ModernGL window integration
# - Text object rendering
# - Direct widget text rendering
# - Coordinate conversion
#
# ============================================================


import pyglet





class TextRenderer:


    def __init__(
        self,
        ctx
    ):


        self.ctx = ctx


        self.enabled = True


        self.screen_height = 720


        #
        # Cached labels
        #

        self.label_cache = {}


        self.debug = False



        print(
            "[UI] Text Renderer Initialized"
        )





    # ========================================================
    # Resize
    # ========================================================


    def resize(
        self,
        width,
        height
    ):


        self.screen_height = height





    # ========================================================
    # Label Creation
    # ========================================================


    def get_label(
        self,
        key,
        text,
        x,
        y,
        size
    ):


        if key not in self.label_cache:


            self.label_cache[key] = pyglet.text.Label(

                str(text),

                x=int(x),

                y=0,

                font_name="Arial",

                font_size=size,

                color=(

                    230,

                    230,

                    230,

                    255

                )

            )



        label = self.label_cache[key]


        label.text = str(text)


        label.x = int(x)


        label.y = int(

            self.screen_height

            -

            y

            -

            size

        )


        return label





    # ========================================================
    # Direct Text Rendering
    # ========================================================


    def render(
        self,
        text,
        x,
        y,
        size=16,
        key=None
    ):


        if not self.enabled:

            return



        if key is None:


            key = (

                str(text),

                int(x),

                int(y),

                size

            )



        label = self.get_label(

            key,

            text,

            x,

            y,

            size

        )



        label.draw()



        if self.debug:


            print(

                "[UI] Draw Text:",

                text,

                "at",

                x,

                y

            )







    # ========================================================
    # Text Object Rendering
    # ========================================================


    def draw_text(
        self,
        text_object
    ):


        if not self.enabled:

            return



        if not text_object.visible:

            return



        self.render(

            text_object.value,

            text_object.x,

            text_object.y,

            text_object.size,

            key=id(text_object)

        )







    # ========================================================
    # Draw Text List
    # ========================================================


    def draw(
        self,
        texts
    ):


        if not self.enabled:

            return



        for index,text in enumerate(texts):


            self.draw_text(

                text

            )







    # ========================================================
    # Debug
    # ========================================================


    def enable_debug(
        self
    ):


        self.debug = True






    def disable_debug(
        self
    ):


        self.debug = False






    # ========================================================
    # Enable / Disable
    # ========================================================


    def enable(
        self
    ):


        self.enabled = True





    def disable(
        self
    ):


        self.enabled = False