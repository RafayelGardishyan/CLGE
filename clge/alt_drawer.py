from . import drawer


class Screen(drawer.Screen):
    def render_frame(self):
        self.rendered_frame = ""
        if self.border:
            self.rendered_frame += self.default_symbol * (self.field_width + 2)
            self.rendered_frame += "\n"

        for row in range(self.field_height):
            if self.border:
                self.rendered_frame += self.default_symbol

            for column in range(self.field_width):
                self.rendered_frame += self.frame[(row * self.field_width) + column]

            if self.border:
                self.rendered_frame += self.default_symbol

            self.rendered_frame += "\n"

        if self.border:
            self.rendered_frame += self.default_symbol * (self.field_width + 2)

    def draw(self, objects):
        self.frame = [" "] * (self.field_width * self.field_height)

        for x in objects:
            try:
                self.frame[(x[1] * self.field_width) + x[0]] = x[2]
            except IndexError:
                self.frame.append(x[2])
        self.render_frame()
