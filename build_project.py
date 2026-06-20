# SPDX-FileCopyrightText: 2026 Haruno YUZUNOKI
# SPDX-License-Identifier: (MIT OR Beerware)

import datetime
import re
import shutil
import subprocess
from collections.abc import Generator
from enum import StrEnum
from pathlib import Path


class GitHub(StrEnum):
    url = "https://github.com/yuzunoki-haruno/python-project-template.git"
    repository = "python-project-template"
    branch = "project-template"


def main():
    # Setup placeholders.
    placeholder_replacements = setup_placeholders()

    # Clone project directory.
    root = Path(".")
    root = clone_repository(root, placeholder_replacements)

    # Fill placeholders.
    for filename in find_files(root):
        content = fill_placeholder(filename, placeholder_replacements)
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(content)


def setup_placeholders() -> dict[str, str]:
    """Setup placeholders.

    Returns:
        dict[str, str]: placeholder replacements
    """
    # initialize placeholder replacements.
    today = datetime.date.today()
    placeholder_replacements = {
        "project-template": "my-project",
        "description": "Python project",
        "author": "Example Author",
        "email": "example.com",
        "version": "0.1.0",
        "date": str(today),
        "year": str(today.year),
    }
    # setup placeholder replacements from commandline.
    for placeholder in placeholder_replacements:
        if placeholder == "year":
            continue

        if placeholder == "project-template":
            default = placeholder_replacements[placeholder]
            input_str = input(f"> project name [{default}]:")
        else:
            default = placeholder_replacements[placeholder]
            input_str = input(f"> {placeholder} [{default}]:")

        if input_str:
            if placeholder == "date":
                input_dt = datetime.datetime.strptime(input_str, r"%Y-%m-%d").date()
                placeholder_replacements[placeholder] = str(input_dt)
                placeholder_replacements["year"] = str(input_dt.year)
            else:
                placeholder_replacements[placeholder] = input_str

    return placeholder_replacements


def clone_repository(root: Path, placeholder_replacements: dict[str, str]) -> Path:
    """Clone Repository from GitHub.

    Args:
        root (Path): root directory where project directory will be created.

    Returns:
        Path: path of project directory
    """
    pj_dir = root / GitHub.repository
    new_name = placeholder_replacements["project-template"]
    # Clone project directory from GitHub.
    git_args = ["git", "clone", GitHub.url, "-b", GitHub.branch]
    subprocess.run(git_args, check=True)
    # Delete .git folder from project directory.
    shutil.rmtree(root / GitHub.repository / ".git")
    # Rename src directory in project directory.
    src_dir = pj_dir / "src" / "{{project-template}}"
    src_dir.rename(src_dir.parent / new_name.replace("-", "_"))
    # Rename project directory.
    new_root = pj_dir.rename(pj_dir.parent / new_name)
    return new_root


def find_files(root: Path) -> Generator[Path, None, None]:
    """Find files containing placeholders.

    Args:
        root (Path): directory to search in for files containing placeholders

    Yields:
        Generator[Path, None, None]: files containing placeholders
    """
    yield root / "pyproject.toml"
    yield root / "README.md"
    yield root / "LICENSE"
    for filename in (root / "LICENSES").glob("*.txt"):
        yield filename
    for filename in (root / "docs").glob("**/*.md"):
        yield filename
    for filename in (root / "src").glob("**/*.py"):
        yield filename
    for filename in (root / "tests").glob("**/*.py"):
        yield filename


def fill_placeholder(filename: Path, placeholder_replacements: dict[str, str]) -> str:
    """Fill in the placeholders.

    Args:
        filename (Path): files containing placeholder

    Returns:
        str: result of filling in placeholders
    """
    with open(filename, encoding="utf-8") as f:
        content = f.read()

    for placeholder in re.findall(r"\{\{(.*?)\}\}", content):
        before = "{{" + placeholder + "}}"
        after = placeholder_replacements[placeholder]
        content = content.replace(before, after)

    return content


if __name__ == "__main__":
    main()
