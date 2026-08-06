import glm


class Transform:

    def __init__(self):

        self.position = glm.vec3(
            0.0,
            0.0,
            0.0
        )

        self.rotation = glm.vec3(
            0.0,
            0.0,
            0.0
        )

        self.scale = glm.vec3(
            1.0,
            1.0,
            1.0
        )

        print("[Transform] Created")

    def get_matrix(self):

        model = glm.mat4(1.0)

        model = glm.translate(
            model,
            self.position
        )

        model = glm.rotate(
            model,
            glm.radians(self.rotation.x),
            glm.vec3(1.0, 0.0, 0.0)
        )

        model = glm.rotate(
            model,
            glm.radians(self.rotation.y),
            glm.vec3(0.0, 1.0, 0.0)
        )

        model = glm.rotate(
            model,
            glm.radians(self.rotation.z),
            glm.vec3(0.0, 0.0, 1.0)
        )

        model = glm.scale(
            model,
            self.scale
        )

        return model

    def set_position(
        self,
        x,
        y,
        z
    ):

        self.position = glm.vec3(
            x,
            y,
            z
        )

    def translate(
        self,
        x,
        y,
        z
    ):

        self.position += glm.vec3(
            x,
            y,
            z
        )

    def set_rotation(
        self,
        x,
        y,
        z
    ):

        self.rotation = glm.vec3(
            x,
            y,
            z
        )

    def rotate(
        self,
        x,
        y,
        z
    ):

        self.rotation += glm.vec3(
            x,
            y,
            z
        )

    def set_scale(
        self,
        x,
        y,
        z
    ):

        self.scale = glm.vec3(
            x,
            y,
            z
        )

    def uniform_scale(
        self,
        value
    ):

        self.scale = glm.vec3(
            value,
            value,
            value
        )

    def reset(self):

        self.position = glm.vec3(
            0.0,
            0.0,
            0.0
        )

        self.rotation = glm.vec3(
            0.0,
            0.0,
            0.0
        )

        self.scale = glm.vec3(
            1.0,
            1.0,
            1.0
        )

    def __str__(self):

        return (
            f"Transform("
            f"Position={tuple(self.position)}, "
            f"Rotation={tuple(self.rotation)}, "
            f"Scale={tuple(self.scale)})"
        )