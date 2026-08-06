import numpy as np
import moderngl

from engine.vehicle.mesh import Mesh



class Gizmo:


    def __init__(
        self,
        ctx,
        shader
    ):

        self.ctx = ctx
        self.shader = shader

        self.meshes = {}

        self.position = np.array(
            [
                0.0,
                0.0,
                0.0
            ],
            dtype="f4"
        )


        self.distance = 4.0
        self.size = 1.5


        self.create_axes()


        print(
            "[Crash Studio] Editor Gizmo Initialized"
        )



    # ==========================================
    # Create Axis Meshes
    # ==========================================

    def create_axes(self):


        self.build_meshes()



    def build_meshes(self):


        p = self.position
        s = self.size



        x_vertices = np.array(
            [
                p[0], p[1], p[2],
                p[0] + s, p[1], p[2]
            ],
            dtype="f4"
        )



        y_vertices = np.array(
            [
                p[0], p[1], p[2],
                p[0], p[1] + s, p[2]
            ],
            dtype="f4"
        )



        z_vertices = np.array(
            [
                p[0], p[1], p[2],
                p[0], p[1], p[2] + s
            ],
            dtype="f4"
        )



        self.meshes["X"] = Mesh(
            self.ctx,
            x_vertices
        )


        self.meshes["Y"] = Mesh(
            self.ctx,
            y_vertices
        )


        self.meshes["Z"] = Mesh(
            self.ctx,
            z_vertices
        )



        for mesh in self.meshes.values():

            mesh.create_vao(
                self.shader
            )



    # ==========================================
    # Follow Camera
    # ==========================================

    def update(
        self,
        camera
    ):


        self.position = (

            camera.position

            +

            camera.front * self.distance

            +

            camera.up * -0.5

        )


        self.build_meshes()



        print(
            "[Gizmo] Updated Position",
            self.position
        )



    # ==========================================
    # Render
    # ==========================================

    def render(self):


        print(
            "[Gizmo] Rendering"
        )


        self.shader.use()



        # X RED

        self.shader.set_vector(
            "color",
            (
                1.0,
                0.0,
                0.0
            )
        )

        self.meshes["X"].render(
            moderngl.LINES
        )



        # Y GREEN

        self.shader.set_vector(
            "color",
            (
                0.0,
                1.0,
                0.0
            )
        )

        self.meshes["Y"].render(
            moderngl.LINES
        )



        # Z BLUE

        self.shader.set_vector(
            "color",
            (
                0.0,
                0.3,
                1.0
            )
        )

        self.meshes["Z"].render(
            moderngl.LINES
        )