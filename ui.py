import tkinter as tk
from tkinter import filedialog
import os

from version import CRASHPHYS_VERSION
from workshop_manager import WorkshopManager
from gmad_importer import GMADImporter
from gmod_scanner import GModScanner
from vehicle_builder import VehicleBuilder



class CrashPhysUI:


    def __init__(self, window):

        self.window = window


        self.window.title(
            "CrashPhys Studio"
        )


        self.window.geometry(
            "1200x750"
        )



        # =====================================
        # Core Systems
        # =====================================

        self.workshop = WorkshopManager(

            r"C:\Program Files (x86)\Steam\steamapps\workshop\content\4000"

        )


        self.importer = GMADImporter(

            r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmad.exe",

            "workspace"

        )


        self.scanner = GModScanner()


        self.builder = VehicleBuilder()



        # =====================================
        # Current Data
        # =====================================

        self.selected_model = ""


        self.current_wheel_slot = tk.StringVar()

        self.current_wheel_slot.set(

            "front_left"

        )



        # =====================================
        # Start UI
        # =====================================

        self.build_ui()



    # =====================================
    # Main Window
    # =====================================

    def build_ui(self):


        title = tk.Label(

            self.window,

            text=f"CrashPhys Studio {CRASHPHYS_VERSION}",

            font=(

                "Arial",

                26,

                "bold"

            )

        )


        title.pack(

            pady=10

        )



        self.main_frame = tk.Frame(

            self.window

        )


        self.main_frame.pack(

            fill="both",

            expand=True,

            padx=10,

            pady=10

        )



        # LEFT PANEL

        self.left_panel = tk.Frame(

            self.main_frame

        )


        self.left_panel.pack(

            side="left",

            fill="y",

            padx=10

        )



        # RIGHT PANEL

        self.right_panel = tk.Frame(

            self.main_frame

        )


        self.right_panel.pack(

            side="left",

            fill="both",

            expand=True,

            padx=10

        )



        self.build_workshop_panel()


        self.build_model_panel()


        self.build_vehicle_panel()



        # STATUS

        self.status = tk.Label(

            self.window,

            text="Ready",

            anchor="w"

        )


        self.status.pack(

            fill="x",

            side="bottom"

        )
            # =====================================
    # Workshop Panel
    # =====================================

    def build_workshop_panel(self):


        frame = tk.LabelFrame(

            self.left_panel,

            text="Workshop Addons"

        )


        frame.pack(

            fill="y",

            pady=5

        )



        self.addon_box = tk.Listbox(

            frame,

            width=35,

            height=25

        )


        self.addon_box.pack(

            padx=10,

            pady=10

        )



        tk.Button(

            frame,

            text="SCAN WORKSHOP",

            command=self.scan_workshop

        ).pack(

            pady=5

        )



        tk.Button(

            frame,

            text="IMPORT ADDON",

            command=self.import_addon

        ).pack(

            pady=5

        )



    # =====================================
    # Model Panel
    # =====================================

    def build_model_panel(self):


        frame = tk.LabelFrame(

            self.right_panel,

            text="Model Browser"

        )


        frame.pack(

            fill="both",

            expand=True,

            pady=5

        )



        # Category

        tk.Label(

            frame,

            text="Category"

        ).pack(

            anchor="w"

        )



        self.category = tk.StringVar()


        self.category.set(

            "all"

        )



        tk.OptionMenu(

            frame,

            self.category,

            "all",

            "vehicles",

            "parts",

            "weapons",

            "props",

            "other",

            command=lambda x:self.refresh_models()

        ).pack(

            pady=5

        )



        # Model List

        tk.Label(

            frame,

            text="Models"

        ).pack(

            anchor="w"

        )



        self.model_box = tk.Listbox(

            frame,

            width=80,

            height=20

        )


        self.model_box.pack(

            padx=10,

            pady=10

        )



        self.model_box.bind(

            "<Double-Button-1>",

            self.select_model

        )



        # Selected model

        tk.Label(

            frame,

            text="Selected Model"

        ).pack(

            anchor="w"

        )


        self.model_entry = tk.Entry(

            frame,

            width=90

        )


        self.model_entry.pack(

            pady=5

        )



    # =====================================
    # Scan Workshop
    # =====================================

    def scan_workshop(self):


        self.addon_box.delete(

            0,

            tk.END

        )


        self.workshop.scan()



        for addon in self.workshop.get_names():

            self.addon_box.insert(

                tk.END,

                addon

            )



        self.status.config(

            text="Workshop scanned."

        )



    # =====================================
    # Import Addon
    # =====================================

    def import_addon(self):


        selected = self.addon_box.curselection()



        if not selected:


            self.status.config(

                text="Select an addon first."

            )


            return



        try:


            path = self.workshop.get_path(

                selected[0]

            )



            self.status.config(

                text="Extracting addon..."

            )



            self.window.update()



            folder = self.importer.extract(

                path

            )



            self.status.config(

                text="Scanning models..."

            )



            self.window.update()



            self.scanner.scan(

                folder

            )



            self.refresh_models()



            self.status.config(

                text="Import complete."

            )



        except Exception as error:


            self.status.config(

                text=f"Import failed: {error}"

            )



    # =====================================
    # Refresh Models
    # =====================================

    def refresh_models(self):


        self.model_box.delete(

            0,

            tk.END

        )



        category = self.category.get()



        if category == "all":

            models = self.scanner.get_models()


        else:

            models = self.scanner.get_category(

                category

            )



        for model in models:


            self.model_box.insert(

                tk.END,

                model

            )



    # =====================================
    # Select Model
    # =====================================

    def select_model(self,event):


        selected = self.model_box.curselection()



        if not selected:

            return



        model = self.model_box.get(

            selected[0]

        )


        self.selected_model = model



        self.model_entry.delete(

            0,

            tk.END

        )


        self.model_entry.insert(

            0,

            model

        )
            # =====================================
    # Vehicle Builder Panel
    # =====================================

    def build_vehicle_panel(self):


        frame = tk.LabelFrame(

            self.right_panel,

            text="Vehicle Builder"

        )


        frame.pack(

            fill="x",

            pady=10

        )



        # Vehicle Name

        tk.Label(

            frame,

            text="Vehicle Name"

        ).pack(

            anchor="w"

        )



        self.vehicle_name = tk.Entry(

            frame,

            width=60

        )


        self.vehicle_name.pack(

            pady=5

        )



        # Chassis

        tk.Button(

            frame,

            text="SET CHASSIS",

            command=self.set_chassis

        ).pack(

            pady=5

        )



        # Wheel selector

        tk.Label(

            frame,

            text="Wheel Position"

        ).pack(

            anchor="w"

        )



        self.current_wheel_slot.set(

            "front_left"

        )



        tk.OptionMenu(

            frame,

            self.current_wheel_slot,

            "front_left",

            "front_right",

            "rear_left",

            "rear_right"

        ).pack(

            pady=5

        )



        tk.Button(

            frame,

            text="SET WHEEL",

            command=self.set_wheel

        ).pack(

            pady=5

        )



        # Save / Load

        buttons = tk.Frame(

            frame

        )


        buttons.pack(

            pady=10

        )



        tk.Button(

            buttons,

            text="SAVE VEHICLE",

            command=self.save_vehicle

        ).pack(

            side="left",

            padx=5

        )



        tk.Button(

            buttons,

            text="LOAD VEHICLE",

            command=self.load_vehicle

        ).pack(

            side="left",

            padx=5

        )



    # =====================================
    # Set Chassis
    # =====================================

    def set_chassis(self):


        model = self.model_entry.get()



        if not model:


            self.status.config(

                text="No model selected."

            )


            return



        self.builder.set_body(

            model

        )


        self.status.config(

            text="Chassis assigned."

        )



    # =====================================
    # Set Wheel
    # =====================================

    def set_wheel(self):


        model = self.model_entry.get()



        if not model:


            self.status.config(

                text="No model selected."

            )


            return



        slot = self.current_wheel_slot.get()



        self.builder.set_wheel(

            slot,

            model

        )



        self.status.config(

            text=f"{slot} assigned."

        )



    # =====================================
    # Save Vehicle
    # =====================================

    def save_vehicle(self):


        name = self.vehicle_name.get()



        self.builder.set_name(

            name

        )



        filename = filedialog.asksaveasfilename(

            initialdir="profiles",

            defaultextension=".json",

            filetypes=[

                (

                    "CrashPhys Vehicle",

                    "*.json"

                )

            ]

        )



        if not filename:

            return



        try:


            self.builder.save(

                filename

            )


            self.status.config(

                text="Vehicle saved."

            )



        except Exception as error:


            self.status.config(

                text=f"Save failed: {error}"

            )



    # =====================================
    # Load Vehicle
    # =====================================

    def load_vehicle(self):


        filename = filedialog.askopenfilename(

            initialdir="profiles",

            filetypes=[

                (

                    "CrashPhys Vehicle",

                    "*.json"

                )

            ]

        )


        if not filename:

            return



        self.status.config(

            text="Vehicle loaded."

        )