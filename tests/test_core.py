import tempfile
from pathlib import Path

from doveprofuse6l_kit.core import Doveprofuse6lTool


def test_plan_empty_dir():
    with tempfile.TemporaryDirectory() as tmp:
        assert Doveprofuse6lTool(tmp).plan() == []


def test_category_of_known_and_unknown():
    sorter = Doveprofuse6lTool(".")
    assert sorter.category_of("a.png") == "images"
    assert sorter.category_of("a.unknown") == "other"


def test_apply_moves_files():
    with tempfile.TemporaryDirectory() as tmp:
        Path(tmp, "note.md").write_text("hi", encoding="utf-8")
        moved = Doveprofuse6lTool(tmp).apply()
        assert moved == [("note.md", "docs")]
        assert Path(tmp, "docs", "note.md").is_file()
