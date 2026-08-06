# ============================================================
# CrashPhys Studio
# File: engine/ui/widgets.py
# Version: 0.8.1
#
# UI Widgets
#
# Handles:
# - Base widget system
# - Labels
# - Buttons
# - Asset rows
# - Widget hierarchy
# - Horizontal layouts
# - Vertical layouts
# - Mouse routing
#
# ============================================================


class Widget:


    def __init__(
        self,
        x=0,
        y=0,
        width=100,
        height=30
    ):


        self.x = x
        self.y = y

        self.width = width
        self.height = height


        self.visible = True
        self.enabled = True


        self.renderer = None


        self.children = []


        self.hovered = False
        self.selected = False



    # ========================================================
    # Renderer
    # ========================================================


    def set_renderer(
        self,
        renderer
    ):

        self.renderer = renderer


        for child in self.children:

            child.set_renderer(
                renderer
            )



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
    # Bounds
    # ========================================================


    def inside(
        self,
        x,
        y
    ):

        return (

            x >= self.x

            and

            x <= self.x + self.width

            and

            y >= self.y

            and

            y <= self.y + self.height

        )



    # ========================================================
    # Children
    # ========================================================


    def add_child(
        self,
        widget
    ):

        self.children.append(
            widget
        )


        widget.set_renderer(
            self.renderer
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


        if not self.enabled:

            return


        self.draw_self()


        for child in self.children:

            child.draw()



    def draw_self(
        self
    ):

        pass



    # ========================================================
    # Mouse
    # ========================================================


    def mouse_move(
        self,
        x,
        y
    ):

        self.hovered = self.inside(
            x,
            y
        )


        for child in self.children:

            child.mouse_move(
                x,
                y
            )



    def mouse_press(
        self,
        x,
        y,
        button
    ):

        for child in self.children:

            child.mouse_press(
                x,
                y,
                button
            )





# ============================================================
# Label
# ============================================================


class Label(Widget):


    def __init__(
        self,
        text,
        **kwargs
    ):

        super().__init__(
            **kwargs
        )

        self.text = text



    def draw_self(
        self
    ):

        if self.renderer:

            self.renderer.draw_text(
                self.text,
                self.x,
                self.y
            )





# ============================================================
# Button
# ============================================================


class Button(Widget):


    def __init__(
        self,
        text,
        callback=None,
        **kwargs
    ):

        super().__init__(
            **kwargs
        )


        self.text = text
        self.callback = callback

        self.pressed = False



    def mouse_press(
        self,
        x,
        y,
        button
    ):

        if button != 1:

            return


        if self.inside(
            x,
            y
        ):

            self.selected = True

            self.click()



    def click(
        self
    ):

        print(
            "[UI] Button Click:",
            self.text
        )


        if self.callback:

            self.callback()



    def draw_self(
        self
    ):

        if not self.renderer:

            return


        if self.selected:

            color = (
                0.35,
                0.45,
                0.65
            )

        elif self.hovered:

            color = (
                0.30,
                0.30,
                0.40
            )

        else:

            color = (
                0.20,
                0.20,
                0.25
            )


        self.renderer.draw_rect(
            self.x,
            self.y,
            self.width,
            self.height,
            color
        )


        self.renderer.draw_text(
            self.text,
            self.x + 8,
            self.y + 8
        )
        # ============================================================
# Asset Row
#
# Used by Project Browser
# ============================================================


class AssetRow(Widget):


    def __init__(
        self,
        name,
        callback=None,
        **kwargs
    ):

        # FIX:
        # Prevent duplicate width/height keyword crash.
        #
        # ProjectPanel was passing:
        # width=...
        # height=...
        #
        # while AssetRow was also forcing:
        # width=220
        # height=24
        #
        # Now defaults are only applied if missing.

        kwargs.setdefault(
            "width",
            220
        )

        kwargs.setdefault(
            "height",
            24
        )


        super().__init__(
            **kwargs
        )


        self.name = name

        self.callback = callback



    def mouse_press(
        self,
        x,
        y,
        button
    ):

        if button != 1:

            return


        if self.inside(
            x,
            y
        ):

            self.selected = True


            print(
                "[Asset] Selected:",
                self.name
            )


            if self.callback:

                self.callback(
                    self.name
                )



    def draw_self(
        self
    ):


        if not self.renderer:

            return



        if self.selected:

            color = (
                0.25,
                0.35,
                0.55
            )


        elif self.hovered:

            color = (
                0.25,
                0.25,
                0.30
            )


        else:

            color = (
                0,
                0,
                0
            )



        self.renderer.draw_rect(
            self.x,
            self.y,
            self.width,
            self.height,
            color
        )


        self.renderer.draw_text(
            self.name,
            self.x + 8,
            self.y + 5
        )





# ============================================================
# VBox
# ============================================================


class VBox:


    def __init__(
        self,
        x,
        y,
        spacing=5
    ):

        self.x = x
        self.y = y

        self.spacing = spacing

        self.widgets = []

        self.renderer = None



    def set_renderer(
        self,
        renderer
    ):

        self.renderer = renderer


        for widget in self.widgets:

            widget.set_renderer(
                renderer
            )



    def add(
        self,
        widget
    ):

        offset = 0


        for item in self.widgets:

            offset += (
                item.height
                +
                self.spacing
            )


        widget.set_position(
            self.x,
            self.y + offset
        )


        widget.set_renderer(
            self.renderer
        )


        self.widgets.append(
            widget
        )



    def update(
        self,
        delta_time
    ):

        for widget in self.widgets:

            widget.update(
                delta_time
            )



    def draw(
        self
    ):

        for widget in self.widgets:

            widget.draw()



    def mouse_move(
        self,
        x,
        y
    ):

        for widget in self.widgets:

            widget.mouse_move(
                x,
                y
            )



    def mouse_press(
        self,
        x,
        y,
        button
    ):

        for widget in self.widgets:

            widget.mouse_press(
                x,
                y,
                button
            )





# ============================================================
# HBox
#
# Toolbar layout
# ============================================================


class HBox:


    def __init__(
        self,
        x,
        y,
        spacing=6
    ):

        self.x = x
        self.y = y

        self.spacing = spacing

        self.widgets = []

        self.renderer = None



    def set_renderer(
        self,
        renderer
    ):

        self.renderer = renderer


        for widget in self.widgets:

            widget.set_renderer(
                renderer
            )



    def add(
        self,
        widget
    ):

        offset = 0


        for item in self.widgets:

            offset += (
                item.width
                +
                self.spacing
            )


        widget.set_position(
            self.x + offset,
            self.y
        )


        widget.set_renderer(
            self.renderer
        )


        self.widgets.append(
            widget
        )



    def update(
        self,
        delta_time
    ):

        for widget in self.widgets:

            widget.update(
                delta_time
            )



    def draw(
        self
    ):

        for widget in self.widgets:

            widget.draw()



    def mouse_move(
        self,
        x,
        y
    ):

        for widget in self.widgets:

            widget.mouse_move(
                x,
                y
            )



    def mouse_press(
        self,
        x,
        y,
        button
    ):

        for widget in self.widgets:

            widget.mouse_press(
                x,
                y,
                button
            )