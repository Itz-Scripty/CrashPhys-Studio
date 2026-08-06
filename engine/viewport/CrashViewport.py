# ============================================================
# CrashPhys Studio
# File: engine/viewport/CrashViewport.py
# Version: 0.9.0
#
# Main 3D Viewport
#
# Handles:
# - OpenGL viewport
# - Camera
# - Editor
# - Vehicle rendering
# - Grid
# - UI
# - Mouse routing
# ============================================================


import moderngl
import moderngl_window as mglw


from engine.camera.camera import Camera
from engine.camera.input import InputController

from engine.renderer.grid import Grid
from engine.renderer.shader import Shader
from engine.renderer.vehicle_renderer import VehicleRenderer

from engine.editor import Editor

from engine.vehicle.vehicle_builder import VehicleBuilder

from engine.ui.editor_ui import EditorUI



VERTEX_SHADER = """
#version 330

in vec3 in_position;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    gl_Position =
        projection *
        view *
        model *
        vec4(in_position,1.0);
}
"""


FRAGMENT_SHADER = """
#version 330

uniform vec3 color;

out vec4 fragColor;

void main()
{
    fragColor = vec4(color,1.0);
}
"""



class CrashViewport(mglw.WindowConfig):


    gl_version = (3,3)

    title = "CrashPhys Studio Beta"

    window_size = (1280,720)



    def __init__(
        self,
        **kwargs
    ):


        super().__init__(**kwargs)


        print("[Viewport] Starting")



        #
        # Editor
        #

        self.editor = Editor()



        #
        # Camera
        #

        self.camera = Camera()

        self.input = InputController(
            self.camera
        )



        #
        # Mouse state
        #

        self.mouse_captured = False



        #
        # Shader
        #

        self.shader = Shader(
            self.ctx,
            VERTEX_SHADER,
            FRAGMENT_SHADER
        )



        #
        # Grid
        #

        self.grid = Grid(
            self.ctx,
            self.shader,
            size=20,
            spacing=1
        )



        #
        # Renderer
        #

        self.vehicle_renderer = VehicleRenderer(
            self.ctx,
            self.shader
        )



        #
        # Vehicles
        #

        self.vehicle_builder = VehicleBuilder()



        #
        # Spawn startup vehicle once
        #

        vehicle = (
            self.vehicle_builder.create_buggy()
        )


        self.editor.add_object(
            vehicle
        )



        #
        # UI
        #

        self.ui = EditorUI(
            self.ctx,
            self.editor
        )



        print("[Viewport] Ready")





    # ========================================================
    # Scene
    # ========================================================


    def render_scene(self):


        for obj in self.editor.scene.objects:


            if obj.__class__.__name__ == "Vehicle":


                self.vehicle_renderer.draw(
                    obj
                )





    # ========================================================
    # Picking
    # ========================================================


    def pick_object(
        self,
        x,
        y
    ):


        if not self.editor.scene.objects:

            return



        obj = self.editor.scene.objects[0]


        self.editor.select(
            obj
        )


        print(
            "[Viewport] Selected:",
            obj.name
        )





    # ========================================================
    # Render
    # ========================================================


    def on_render(
        self,
        time,
        frame_time
    ):


        self.input.update(
            frame_time
        )


        self.editor.update(
            frame_time
        )


        self.ui.update(
            frame_time
        )



        self.ctx.clear(
            0.15,
            0.15,
            0.15,
            1
        )



        self.shader.set_matrix(
            "view",
            self.camera.get_view_matrix()
        )


        self.shader.set_matrix(
            "projection",
            self.camera.get_projection_matrix(
                self.wnd.width,
                self.wnd.height
            )
        )



        self.grid.render()


        self.render_scene()



        #
        # UI pass
        #

        self.ctx.disable(
            moderngl.DEPTH_TEST
        )


        self.ui.draw()


        self.ctx.enable(
            moderngl.DEPTH_TEST
        )





    # ========================================================
    # Resize
    # ========================================================


    def on_resize(
        self,
        width,
        height
    ):

        self.ui.resize(
            width,
            height
        )





    # ========================================================
    # Mouse
    # ========================================================


    def on_mouse_press_event(
        self,
        x,
        y,
        button
    ):


        #
        # UI first
        #

        if self.ui.mouse_press(
            x,
            y,
            button
        ):

            return



        #
        # Camera capture
        #

        if button == 3:

            self.mouse_captured = True

            self.input.mouse_press(
                button,
                x,
                y
            )

            return



        #
        # Object select
        #

        if button == 1:

            self.pick_object(
                x,
                y
            )





    def on_mouse_release_event(
        self,
        x,
        y,
        button
    ):


        if button == 3:

            self.mouse_captured = False


        self.input.mouse_release(
            button
        )





    def on_mouse_drag_event(
        self,
        x,
        y,
        dx,
        dy
    ):


        if self.mouse_captured:

            self.input.mouse_move(
                x,
                y,
                dx,
                dy
            )





    def on_mouse_position_event(
        self,
        x,
        y,
        dx,
        dy
    ):


        self.ui.mouse_move(
            x,
            y
        )



        if self.mouse_captured:

            self.input.mouse_move(
                x,
                y,
                dx,
                dy
            )





    # ========================================================
    # Keyboard
    # ========================================================


    def on_key_event(
        self,
        key,
        action,
        modifiers
    ):


        keys = {

            119:"W",
            97:"A",
            115:"S",
            100:"D",
            101:"E",
            113:"Q"

        }



        if key not in keys:

            return



        value = keys[key]



        if str(action) == "ACTION_PRESS":

            self.input.key_press(
                value
            )


        elif str(action) == "ACTION_RELEASE":

            self.input.key_release(
                value
            )