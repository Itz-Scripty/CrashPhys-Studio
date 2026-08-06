# ============================================================
# CrashPhys Studio
# File: engine/editor/editor.py
# Version: 0.8.2
#
# Editor System
#
# Handles:
# - Project connection
# - Scene management
# - Vehicle spawning
# - Object selection
# - Inspector connection
# - Transform editing
# - Gizmo connection
# - GMA Asset pipeline
#
# ============================================================


from engine.scene import Scene
from engine.projects import Project


from engine.editor.inspector import Inspector
from engine.editor.selection import Selection
from engine.editor.transform import TransformController
from engine.editor.picking import PickingSystem
from engine.editor.gizmo import Gizmo


from engine.vehicle.vehicle_builder import VehicleBuilder


from engine.assets.asset_scanner import AssetScanner
from engine.assets.asset_manager import AssetManager





class Editor:


    def __init__(
        self,
        camera=None
    ):


        #
        # Project
        #

        self.project = None



        #
        # Assets
        #
        # GMA Pipeline:
        #
        # Workshop .gma
        #       |
        # GMAD Importer
        #       |
        # workspace/
        #       |
        # Asset Scanner
        #

        self.asset_scanner = AssetScanner(

            "workspace"

        )


        self.asset_manager = AssetManager()


        self.assets = []



        print(
            "[Editor] Asset System Connected"
        )





        #
        # Scene
        #

        self.scene = Scene(

            "Editor Scene"

        )





        #
        # Inspector
        #

        self.inspector = Inspector()





        #
        # Selection
        #

        self.selection = Selection()





        #
        # Transform
        #

        self.transform = TransformController()





        #
        # Gizmo
        #

        self.gizmo = Gizmo()





        #
        # Vehicle Builder
        #

        self.vehicle_builder = VehicleBuilder()





        #
        # Picking
        #

        self.picking = None



        if camera:

            self.set_camera(

                camera

            )





        #
        # State
        #

        self.running = True





        #
        # Initial Asset Scan
        #

        self.scan_assets()





        print(
            "[Editor] Initialized"
        )





    # ========================================================
    # Assets
    # ========================================================


    def scan_assets(
        self
    ):


        scanned = self.asset_scanner.scan(

            "workspace"

        )



        self.assets = scanned



        for asset in scanned:


            self.asset_manager.register(

                asset

            )



        print(

            "[Editor] Assets Loaded:",

            len(self.assets)

        )





    def get_assets(
        self
    ):


        return self.asset_manager.list_assets()





    # ========================================================
    # Camera / Picking
    # ========================================================


    def set_camera(
        self,
        camera
    ):


        self.picking = PickingSystem(

            camera

        )


        print(

            "[Editor] Camera Connected"

        )





    def click_select(
        self,
        mouse_x,
        mouse_y,
        width,
        height
    ):


        if not self.picking:

            return



        self.picking.set_mouse_position(

            mouse_x,

            mouse_y

        )



        obj = self.picking.pick(

            self.scene,

            width,

            height

        )



        if obj:


            self.select(

                obj

            )


        else:


            self.clear_selection()





    # ========================================================
    # Vehicle
    # ========================================================


    def spawn_vehicle(
        self,
        name="Crash Test Buggy"
    ):


        vehicle = self.vehicle_builder.build(

            name

        )



        self.add_object(

            vehicle

        )



        self.select(

            vehicle

        )



        print(

            "[Editor] Vehicle Spawned:",

            name

        )



        return vehicle





    # ========================================================
    # Project
    # ========================================================


    def create_project(
        self,
        name,
        path
    ):


        self.project = Project(

            name,

            path

        )


        self.project.create()





    def load_project(
        self,
        project
    ):


        self.project = project





    # ========================================================
    # Objects
    # ========================================================


    def add_object(
        self,
        obj
    ):


        self.scene.add_object(

            obj

        )





    def remove_object(
        self,
        obj
    ):


        self.scene.remove_object(

            obj

        )



        if self.selection.get() == obj:


            self.clear_selection()





    # ========================================================
    # Selection
    # ========================================================


    def select(
        self,
        obj
    ):


        self.selection.select(

            obj

        )


        self.transform.set_target(

            obj

        )


        self.gizmo.set_target(

            obj

        )


        self.inspector.inspect(

            obj

        )



        print(

            "[Editor] Selected:",

            obj.name

        )





    def clear_selection(
        self
    ):


        self.selection.clear()


        self.transform.clear_target()


        self.gizmo.clear_target()


        self.inspector.clear()





    def get_selected(
        self
    ):


        return self.selection.get()





    # ========================================================
    # Transform
    # ========================================================


    def move_selected(
        self,
        x,
        y,
        z
    ):


        self.transform.move(

            x,

            y,

            z

        )





    def rotate_selected(
        self,
        x,
        y,
        z
    ):


        self.transform.rotate(

            x,

            y,

            z

        )





    def scale_selected(
        self,
        x,
        y,
        z
    ):


        self.transform.scale(

            x,

            y,

            z

        )





    # ========================================================
    # Update
    # ========================================================


    def update(
        self,
        delta_time
    ):


        if not self.running:

            return



        self.scene.update(

            delta_time

        )


        self.gizmo.update(

            delta_time

        )





    # ========================================================
    # Draw
    # ========================================================


    def draw(
        self
    ):


        if not self.running:

            return



        self.scene.draw()


        self.gizmo.draw()


        self.inspector.draw()





    # ========================================================
    # Shutdown
    # ========================================================


    def shutdown(
        self
    ):


        self.running = False



        print(

            "[Editor] Shutdown"

        )