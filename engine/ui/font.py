# ============================================================
# CrashPhys Studio
# File: engine/ui/font.py
# Version: 0.2.0
#
# UI Font System
#
# Handles:
# - Font loading foundation
# - Text rendering interface
# - UI text preparation
#
# ============================================================


class Font:


    def __init__(
        self,
        name="Default",
        size=16
    ):


        self.name = name

        self.size = size


        self.loaded = False


        self.color = (
            0.9,
            0.9,
            0.9
        )


        print(
            "[UI] Font Created:",
            self.name,
            self.size
        )





    # ========================================================
    # Load
    # ========================================================


    def load(
        self,
        path=None
    ):


        self.loaded = True


        print(
            "[UI] Font Loaded:",
            self.name
        )





    # ========================================================
    # Draw Text
    # ========================================================


    def draw_text(
        self,
        text,
        x,
        y
    ):


        if not self.loaded:

            return



        print(
            "[UI] Draw Text:",
            text,
            "at",
            x,
            y
        )





    # ========================================================
    # Size
    # ========================================================


    def set_size(
        self,
        size
    ):


        self.size = size





    def get_size(
        self
    ):


        return self.size





    # ========================================================
    # Color
    # ========================================================


    def set_color(
        self,
        color
    ):


        self.color = color





    def get_color(
        self
    ):


        return self.color





# ============================================================
# Default Font
# ============================================================


default_font = Font()

default_font.load()