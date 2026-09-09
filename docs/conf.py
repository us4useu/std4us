# SPDX-FileCopyrightText: Copyright (c) 2024-2026 us4us Ltd.
# SPDX-License-Identifier: MIT

import datetime
import os
import re

# -- Project ---------------------------------------------------------------

project = "nson"
author = "us4us Ltd."
copyright = f"{datetime.date.today().year}, us4us Ltd."


def _read_version() -> str:
    """Pick the version from recipes/nson/config.yml (single source of truth)."""
    config_yml = os.path.join(os.path.dirname(__file__), "..", "recipes", "nson", "config.yml")
    with open(config_yml, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r'\s*"([^"]+)"\s*:\s*$', line)
            if match:
                return match.group(1)
    return "unknown"


release = _read_version()
version = ".".join(release.split(".")[:2])

# -- General ---------------------------------------------------------------

extensions = ["breathe"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML ------------------------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- Breathe ---------------------------------------------------------------

breathe_projects = {
    "nson": os.path.join(os.path.dirname(__file__), "_build", "doxygen", "xml"),
}
breathe_default_project = "nson"
breathe_default_members = ("members",)
breathe_domain_by_extension = {"h": "cpp"}
