import reflex as rx

config = rx.Config(
    app_name="practica_1_reflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)