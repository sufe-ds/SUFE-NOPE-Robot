"""领域函数：把 LabVIEW 动作数据展平为关节轨迹。

``Robots/NAO/movements/*.py`` 中每个动作的 ``movements`` 结构为：
``[jointName, [[time, angle, handle_in, handle_out], ...]]``。
展平后即为 ``ALMotion.angleInterpolationBezier(names, times, angles)`` 的参数。
本函数是纯函数，与具体机器人无关。
"""

from __future__ import annotations


def flatten(
    movements: list,
) -> tuple[list[str], list[list[float]], list[list[list[float]]]]:
    names: list[str] = []
    times: list[list[float]] = []
    angles: list[list[list[float]]] = []
    for joint in movements:
        names.append(joint[0])
        keyframes = joint[1]
        times.append([float(kf[0]) for kf in keyframes])
        angles.append([[float(kf[1]), kf[2], kf[3]] for kf in keyframes])
    return names, times, angles
