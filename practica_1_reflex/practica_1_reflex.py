import reflex as rx


class State(rx.State):
    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1

    @rx.event
    def decrement(self):
        self.count -= 1


def index():
    return rx.vstack(
        rx.heading(
            "Mi Primera Página Web con Reflex",
            size="8",
            text_align="center",
        ),
        rx.text(
            "Bienvenido. Usa los botones para incrementar o decrementar el contador.",
            text_align="center",
        ),
        rx.hstack(
            rx.button(
                "Decrement",
                color_scheme="ruby",
                on_click=State.decrement,
            ),
            rx.heading(State.count, font_size="2em"),
            rx.button(
                "Increment",
                color_scheme="grass",
                on_click=State.increment,
            ),
            spacing="4",
        ),
        spacing="4",
        align="center",
        padding="40px",
    )


app = rx.App()
app.add_page(index)