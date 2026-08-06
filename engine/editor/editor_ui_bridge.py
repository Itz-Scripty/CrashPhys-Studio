# ============================================================
# CrashPhys Studio
# File: engine/editor/editor_ui_bridge.py
# Version: 0.1.0
#
# Editor UI Bridge
#
# Handles:
# - Editor/UI communication
# - Inspector updates
#
# ============================================================





class EditorUIBridge:


    def __init__(
        self,
        editor,
        ui
    ):


        self.editor = editor

        self.ui = ui



        print(
            "[EditorUI] Bridge Initialized"
        )





    def update(
        self
    ):


        inspector = (
            self.editor.inspector
        )


        if not inspector.target:

            return



        data = inspector.get_data()



        print(
            "[EditorUI] Inspector Updated"
        )


        for key, value in data.items():


            print(
                key,
                ":",
                value
            )