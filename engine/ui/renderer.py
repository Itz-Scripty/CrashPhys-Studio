# ============================================================
# CrashPhys Studio
# File: engine/ui/renderer.py
# Version: 0.8.5
#
# UI Renderer
#
# Handles:
# - Editor panel rendering
# - Toolbar rendering
# - OpenGL UI rectangles
# - Theme colors
# - Text renderer connection
# - Widget rendering
# - Resize synchronization
#
# ============================================================


import moderngl
import numpy as np


from engine.ui.text_renderer import TextRenderer





class UIRenderer:


    def __init__(
        self,
        ctx
    ):


        self.ctx = ctx

        self.enabled = True


        self.screen = (

            1280,

            720

        )


        self.ctx.enable(

            moderngl.BLEND

        )


        self.ctx.blend_func = (

            moderngl.SRC_ALPHA,

            moderngl.ONE_MINUS_SRC_ALPHA

        )



        self.text_renderer = TextRenderer(

            ctx

        )



        self.program = self.ctx.program(

            vertex_shader="""


            #version 330


            in vec2 in_position;


            uniform vec2 screen;


            void main()

            {

                vec2 pos =

                    in_position /

                    screen;


                pos *= 2.0;


                pos.x -= 1.0;


                pos.y =

                    1.0 -

                    pos.y;


                gl_Position = vec4(

                    pos,

                    0.0,

                    1.0

                );

            }

            """,


            fragment_shader="""


            #version 330


            uniform vec4 color;


            out vec4 fragColor;


            void main()

            {

                fragColor = color;

            }

            """

        )


        print(

            "[UI] Renderer Initialized"

        )





    # ========================================================
    # Resize
    # ========================================================


    def resize(
        self,
        width,
        height
    ):


        self.screen = (

            width,

            height

        )


        self.text_renderer.resize(

            width,

            height

        )





    # ========================================================
    # Rectangle
    # ========================================================


    def draw_rect(
        self,
        x,
        y,
        width,
        height,
        color
    ):


        vertices = np.array([

            x, y,

            x + width, y,

            x, y + height,


            x + width, y,

            x + width, y + height,

            x, y + height

        ],
        dtype="f4")



        vbo = self.ctx.buffer(

            vertices.tobytes()

        )


        vao = self.ctx.simple_vertex_array(

            self.program,

            vbo,

            "in_position"

        )


        self.program["screen"].value = self.screen


        self.program["color"].value = (

            color[0],

            color[1],

            color[2],

            1.0

        )


        vao.render(

            moderngl.TRIANGLES

        )


        vao.release()

        vbo.release()





    # ========================================================
    # Text
    # ========================================================


    def draw_text(
        self,
        text,
        x,
        y
    ):


        self.text_renderer.render(

            text,

            x,

            y

        )





    # ========================================================
    # Panel
    # ========================================================


    def draw_panel(
        self,
        panel
    ):


        if not panel.visible:

            return


        print(

            "[UI] Draw Panel:",

            panel.name

        )


        self.draw_rect(

            panel.x,

            panel.y,

            panel.width,

            panel.height,

            panel.theme.get_panel_color()

        )


        self.connect_text(

            panel

        )


        panel.draw()





    def connect_text(
        self,
        panel
    ):


        if not hasattr(

            panel,

            "lines"

        ):

            return


        for text in panel.lines:

            text.set_renderer(

                self.text_renderer

            )





    # ========================================================
    # Toolbar
    # ========================================================


    def draw_toolbar(
        self,
        toolbar
    ):


        if toolbar is None:

            return


        print(

            "[UI] Draw Toolbar"

        )


        toolbar.draw()





    # ========================================================
    # Draw Everything
    # ========================================================


    def draw(
        self,
        panels,
        toolbar=None
    ):


        if not self.enabled:

            return



        #
        # BACKGROUND UI FIRST
        #

        for panel in panels:

            self.draw_panel(

                panel

            )



        #
        # TOOLBAR LAST
        # Always on top
        #

        if toolbar:

            self.draw_toolbar(

                toolbar

            )





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