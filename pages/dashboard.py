"""The dashboard page."""
from canva.templates import template

import reflex as rx


@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.button_group(
            rx.vstack(
                rx.button(
                    rx.vstack(
                        rx.text("CS 61A", font_size="2em"),
                    ),
                    variant = 'outline',
                    size = 'lg'
                ),
                rx.spacer(),
                rx.spacer(),
                rx.spacer(),
                rx.spacer(),
                rx.spacer(),
                rx.spacer(),
                rx.button(
                    rx.text("MATH 54", font_size="2em"),
                    variant = 'outline',
                    size = 'lg'
                ),
                rx.spacer(),
                rx.spacer(),
                rx.spacer(),
                rx.spacer(),
                rx.spacer(),
                rx.spacer(),
                rx.button(
                    rx.text("PSYCH 1", font_size="2em"),
                    variant = 'outline',
                    size = 'lg'
                ),
                rx.spacer(),
                rx.spacer(),
                rx.spacer(),
                rx.spacer(),
                rx.spacer(),
                rx.spacer(),
                rx.button(
                    rx.text("ART 12", font_size="2em"),
                    variant = 'outline',
                    size = 'lg'
                )
            )
        )

    """
"""