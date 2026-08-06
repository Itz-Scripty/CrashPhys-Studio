import json
import os
import shutil


class ProjectManager:

    def __init__(self, projects_folder="projects"):

        self.projects_folder = projects_folder
        self.current_project = None

        os.makedirs(
            self.projects_folder,
            exist_ok=True
        )

    # ============================================
    # Create Project
    # ============================================

    def create_project(self, name):

        project_path = os.path.join(
            self.projects_folder,
            name
        )

        if os.path.exists(project_path):
            raise FileExistsError(
                f"Project '{name}' already exists."
            )

        os.makedirs(project_path)

        folders = [
            "extracted",
            "profiles",
            "exports",
            "cache",
            "thumbnails"
        ]

        for folder in folders:

            os.makedirs(
                os.path.join(project_path, folder),
                exist_ok=True
            )

        project = {

            "name": name,

            "version": 1,

            "source_addon": "",

            "workspace": project_path,

            "vehicle": {

                "body": "",

                "wheels": {

                    "front_left": "",
                    "front_right": "",
                    "rear_left": "",
                    "rear_right": ""

                },

                "parts": []

            }

        }

        self.save_project(
            project_path,
            project
        )

        self.current_project = project

        return project

    # ============================================
    # Save Project
    # ============================================

    def save_project(
        self,
        project_path,
        project_data
    ):

        filename = os.path.join(
            project_path,
            "project.json"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                project_data,
                file,
                indent=4
            )

    # ============================================
    # Open Project
    # ============================================

    def open_project(self, project_path):

        filename = os.path.join(
            project_path,
            "project.json"
        )

        if not os.path.exists(filename):

            raise FileNotFoundError(
                "project.json not found."
            )

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            self.current_project = json.load(
                file
            )

        return self.current_project

    # ============================================
    # Delete Project
    # ============================================

    def delete_project(
        self,
        project_name
    ):

        project_path = os.path.join(
            self.projects_folder,
            project_name
        )

        if os.path.exists(project_path):

            shutil.rmtree(
                project_path
            )

    # ============================================
    # List Projects
    # ============================================

    def list_projects(self):

        projects = []

        for item in os.listdir(
            self.projects_folder
        ):

            path = os.path.join(
                self.projects_folder,
                item
            )

            if os.path.isdir(path):

                projects.append(item)

        return sorted(projects)

    # ============================================
    # Get Current Project
    # ============================================

    def get_current_project(self):

        return self.current_project