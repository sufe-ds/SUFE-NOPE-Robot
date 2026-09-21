"""动作加载器测试。"""

from __future__ import annotations

import pytest

from embodied.config import default_movement_dir
from embodied.errors import UnknownMovementError
from embodied.movements import MovementLibrary, flatten


def library() -> MovementLibrary:
    return MovementLibrary(default_movement_dir())


def test_default_directory_exists() -> None:
    assert default_movement_dir().is_dir()


@pytest.mark.parametrize("bad", ["../evil", "a/b", "..", "", "x.py"])
def test_resolve_rejects_bad_names(bad: str) -> None:
    with pytest.raises(UnknownMovementError):
        library().resolve(bad)


def test_resolve_case_insensitive() -> None:
    path = library().resolve("getlucky")
    assert path.name.lower() == "getlucky.py"


def test_prepare_move1_shape() -> None:
    posture, names, times, angles = library().prepare("move1")
    assert posture in ("Stand", "")
    assert names
    assert len(names) == len(times) == len(angles)
    assert len(times[0]) == len(angles[0])
    assert len(angles[0][0]) == 3


def test_list_includes_known_moves() -> None:
    names = {info.name.lower() for info in library().list()}
    assert "move1" in names
    assert "applaud" in names


def test_flatten_manual() -> None:
    movements = [["HeadYaw", [[1.0, 0.1, [3, 0.0, 0.0], [3, 0.0, 0.0]]]]]
    names, times, angles = flatten(movements)
    assert names == ["HeadYaw"]
    assert times == [[1.0]]
    assert angles == [[[0.1, [3, 0.0, 0.0], [3, 0.0, 0.0]]]]
