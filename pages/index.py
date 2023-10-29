"""The home page of the app."""

from canva import styles
from canva.templates import template

import reflex as rx


@template(route="/", title="Home", image="/github.svg")

def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """

    """ OG CODE
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.markdown(content, component_map=styles.markdown_style)
    """
    return rx.vstack(
            rx.heading("School Login", font_size="2em"),
            rx.hstack(rx.text('Username:'),
            rx.text_area()),
            rx.hstack(rx.text('Password:'),
            rx.text_area()),
            rx.button(rx.text('Enter'), variant = 'outline') #add onclick event
    )