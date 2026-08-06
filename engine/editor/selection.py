# ============================================================
# CrashPhys Studio
# File: engine/editor/selection.py
# Version: 0.2.0
#
# Selection System
#
# Handles:
# - Selected object
# - Hover object
# - Selection state
# - Selection events
# - Highlight foundation
#
# ============================================================



class Selection:


    def __init__(
        self
    ):


        self.selected = None

        self.hovered = None


        self.changed = False


        self.listeners = []


        print(
            "[Selection] Initialized"
        )





    # ========================================================
    # Select
    # ========================================================


    def select(
        self,
        obj
    ):


        if self.selected == obj:

            return



        #
        # Clear old selection
        #

        if self.selected:


            if hasattr(
                self.selected,
                "selected"
            ):

                self.selected.selected = False



        self.selected = obj



        if obj:


            if hasattr(
                obj,
                "selected"
            ):

                obj.selected = True



            print(
                "[Selection] Selected:",
                obj.name
            )


        else:

            print(
                "[Selection] Cleared"
            )



        self.changed = True



        self.notify()





    # ========================================================
    # Hover
    # ========================================================


    def hover(
        self,
        obj
    ):


        self.hovered = obj





    def get_hovered(
        self
    ):


        return self.hovered





    # ========================================================
    # Clear
    # ========================================================


    def clear(
        self
    ):


        self.select(
            None
        )





    # ========================================================
    # Get
    # ========================================================


    def get(
        self
    ):


        return self.selected





    # ========================================================
    # Events
    # ========================================================


    def add_listener(
        self,
        callback
    ):


        self.listeners.append(
            callback
        )





    def notify(
        self
    ):


        for callback in self.listeners:


            try:

                callback(
                    self.selected
                )


            except Exception as error:


                print(
                    "[Selection] Event Error:",
                    error
                )