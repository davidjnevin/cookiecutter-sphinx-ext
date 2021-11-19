"""
{{ cookiecutter.project_name }}

{{ cookiecutter.short_description }}
"""

if TYPE_CHECKING:
    from sphinx.application import Sphinx

__version__ = "0.1"


def setup(app: Sphinx) -> dict[str, Any]:
    return {"version": __version__, "parallel_read_safe": True}
