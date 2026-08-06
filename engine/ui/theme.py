# ============================================================
# CrashPhys Studio
# File: engine/ui/theme.py
# Version: 0.2.0
#
# UI Theme System
#
# Handles:
# - Editor colors
# - Panel styling
# - Widget styling
# - UI appearance foundation
#
# ============================================================





class Theme:


    def __init__(
        self
    ):


        #
        # Backgrounds
        #

        self.background = (
            0.08,
            0.08,
            0.08
        )


        self.panel = (
            0.12,
            0.12,
            0.12
        )


        self.panel_header = (
            0.16,
            0.16,
            0.16
        )



        #
        # Text
        #

        self.text = (
            0.9,
            0.9,
            0.9
        )


        self.text_disabled = (
            0.45,
            0.45,
            0.45
        )



        #
        # Buttons
        #

        self.button = (
            0.18,
            0.18,
            0.18
        )


        self.button_hover = (
            0.25,
            0.25,
            0.25
        )


        self.button_pressed = (
            0.35,
            0.35,
            0.35
        )



        #
        # Accent
        #

        self.accent = (
            0.2,
            0.55,
            1.0
        )



        print(
            "[UI] Theme Initialized"
        )





    # ========================================================
    # Helpers
    # ========================================================


    def get_panel_color(
        self
    ):

        return self.panel





    def get_text_color(
        self
    ):

        return self.text





    def get_button_color(
        self,
        hovered=False
    ):


        if hovered:

            return self.button_hover


        return self.button







# ============================================================
# Default Theme
# ============================================================


default_theme = Theme()