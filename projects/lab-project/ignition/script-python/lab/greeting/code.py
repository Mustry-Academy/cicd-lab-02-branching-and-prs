"""lab.greeting -- builds the greeting shown on the Overview screen.

This is the script the lab has you edit. It has no Ignition dependencies: it's
plain Python you can read and change without knowing Perspective or the
gateway. The point of the exercises is the *Git workflow* around this file, not
the code itself.
"""

DEFAULT_NAME = "world"


def greet(name=None):
    """Return a friendly greeting for name, falling back to a default."""
    if name is None or name == "":
        name = DEFAULT_NAME
    return "Hello, %s!" % name
