import reflex as rx


class State(rx.State):
    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1

    @rx.event
    def decrement(self):
        self.count -= 1

    @rx.event
    def reset_counter(self):
        self.count = 0


def index():
    return rx.center(
        rx.box(
            rx.vstack(
                rx.badge(
                    "Práctica 1 · Reflex",
                    color_scheme="violet",
                    variant="solid",
                    size="2",
                ),
                rx.heading(
                    "Mi Primera Página Web con Reflex",
                    size="8",
                    text_align="center",
                    color="white",
                    font_weight="800",
                ),
                rx.text(
                    "Bienvenido a una aplicación interactiva creada con Python usando el ejemplo oficial del contador de Reflex.",
                    text_align="center",
                    color="rgba(255,255,255,0.72)",
                    font_size="17px",
                    max_width="520px",
                ),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "CONTADOR ACTUAL",
                            color="rgba(255,255,255,0.55)",
                            font_size="13px",
                            font_weight="700",
                            letter_spacing="2px",
                        ),
                        rx.heading(
                            State.count,
                            font_size="90px",
                            color="white",
                            font_weight="900",
                            line_height="1",
                        ),
                        rx.text(
                            rx.cond(
                                State.count > 0,
                                "El contador está en positivo.",
                                rx.cond(
                                    State.count < 0,
                                    "El contador está en negativo.",
                                    "El contador está en cero.",
                                ),
                            ),
                            color="rgba(255,255,255,0.70)",
                            font_size="15px",
                        ),
                        spacing="3",
                        align="center",
                    ),
                    background="rgba(255,255,255,0.08)",
                    border="1px solid rgba(255,255,255,0.14)",
                    border_radius="22px",
                    padding="35px",
                    width="100%",
                ),
                rx.hstack(
                    rx.button(
                        "− Decrement",
                        color_scheme="ruby",
                        on_click=State.decrement,
                        size="3",
                        width="150px",
                        variant="solid",
                    ),
                    rx.button(
                        "Reset",
                        color_scheme="gray",
                        on_click=State.reset_counter,
                        size="3",
                        width="110px",
                        variant="solid",
                    ),
                    rx.button(
                        "Increment +",
                        color_scheme="grass",
                        on_click=State.increment,
                        size="3",
                        width="150px",
                        variant="solid",
                    ),
                    spacing="3",
                    justify="center",
                    wrap="wrap",
                ),
                rx.text(
                    "",
                    text_align="center",
                    color="rgba(255,255,255,0.45)",
                    font_size="13px",
                    max_width="520px",
                ),
                spacing="5",
                align="center",
            ),
            background="rgba(15, 23, 42, 0.88)",
            border_radius="28px",
            padding="55px",
            width="650px",
            max_width="90%",
            box_shadow="0 25px 80px rgba(0,0,0,0.45)",
            border="1px solid rgba(255,255,255,0.12)",
        ),
        min_height="100vh",
        background="linear-gradient(135deg, #020617, #111827, #312e81)",
        padding="30px",
    )


app = rx.App()
app.add_page(index)