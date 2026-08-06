# ============================================================
# CrashPhys Studio
# File: engine/ui/editor_ui.py
# Version: 0.9.0
#
# Editor UI Manager
#
# Handles:
# - Top toolbar
# - Project asset browser
# - Inspector
# - UI layout
# - Renderer connection
# - Mouse ownership
# - Input routing
#
# ============================================================


from engine.ui.inspector_panel import InspectorPanel
from engine.ui.project_panel import ProjectPanel
from engine.ui.renderer import UIRenderer
from engine.ui.layout import EditorLayout

from engine.ui.widgets import Button, HBox





class EditorUI:


    def __init__(
        self,
        ctx,
        editor=None
    ):


        print(
            "[UI] Starting Editor UI"
        )


        self.editor = editor


        self.renderer = UIRenderer(
            ctx
        )


        self.layout = EditorLayout()


        self.toolbar_height = 45



        #
        # Toolbar
        #

        self.toolbar = HBox(

            10,

            8,

            spacing=8

        )


        self.toolbar.set_renderer(

            self.renderer

        )


        self.buttons = []


        self.create_toolbar()



        #
        # Panels
        #

        self.project_panel = ProjectPanel(

            asset_manager=getattr(

                editor,

                "asset_manager",

                None

            ),

            workshop_manager=getattr(

                editor,

                "workshop_manager",

                None

            ),

            width=250,

            height=600

        )


        self.project_panel.set_renderer(

            self.renderer

        )




        self.inspector_panel = InspectorPanel(

            getattr(

                editor,

                "inspector",

                None

            ),

            width=280,

            height=600

        )



        self.panels = [

            self.project_panel,

            self.inspector_panel

        ]



        self.visible = True



        print(

            "[UI] Editor UI Ready"

        )







    # ========================================================
    # Toolbar
    # ========================================================


    def create_toolbar(
        self
    ):


        self.add_button(

            "Spawn Vehicle",

            self.spawn_vehicle,

            190

        )


        self.add_button(

            "Delete",

            self.delete_selected

        )


        self.add_button(

            "Save",

            self.save_project

        )


        self.add_button(

            "Load",

            self.load_project

        )






    def add_button(
        self,
        text,
        callback,
        width=120
    ):


        button = Button(

            text,

            callback,

            width=width,

            height=32

        )


        self.toolbar.add(

            button

        )


        self.buttons.append(

            button

        )







    # ========================================================
    # Actions
    # ========================================================


    def spawn_vehicle(
        self
    ):


        if self.editor:


            print(

                "[UI] Spawn Vehicle"

            )


            self.editor.spawn_vehicle()





    def delete_selected(
        self
    ):


        if self.editor:


            obj = self.editor.get_selected()


            if obj:

                self.editor.remove_object(

                    obj

                )





    def save_project(
        self
    ):


        print(

            "[UI] Save Project"

        )





    def load_project(
        self
    ):


        print(

            "[UI] Load Project"

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



        self.toolbar.update(

            delta_time

        )


        for panel in self.panels:


            panel.update(

                delta_time

            )







    # ========================================================
    # Resize
    # ========================================================


    def resize(
        self,
        width,
        height
    ):


        self.layout.apply(

            self.panels,

            width,

            height - self.toolbar_height

        )


        for panel in self.panels:


            panel.move(

                panel.x,

                panel.y + self.toolbar_height

            )



        self.toolbar.x = 10

        self.toolbar.y = 8



        self.renderer.resize(

            width,

            height

        )







    # ========================================================
    # Mouse Ownership
    # ========================================================


    def wants_mouse(
        self,
        x,
        y
    ):


        #
        # Toolbar
        #

        for button in self.buttons:


            if button.inside(

                x,

                y

            ):


                return True





        #
        # Panels
        #

        for panel in self.panels:


            if panel.inside(

                x,

                y

            ):


                return True



        return False







    # ========================================================
    # Mouse Routing
    # ========================================================


    def mouse_move(
        self,
        x,
        y
    ):


        self.toolbar.mouse_move(

            x,

            y

        )


        for panel in self.panels:


            panel.mouse_move(

                x,

                y

            )







    def mouse_press(
        self,
        x,
        y,
        button
    ):


        self.toolbar.mouse_press(

            x,

            y,

            button

        )


        for panel in self.panels:


            panel.mouse_press(

                x,

                y,

                button

            )







    def mouse_release(
        self,
        x,
        y,
        button
    ):


        for panel in self.panels:


            if hasattr(

                panel,

                "mouse_release"

            ):


                panel.mouse_release(

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


        if not self.visible:

            return



        self.toolbar.draw()



        self.renderer.draw(

            self.panels

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