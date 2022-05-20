import traceback

from pizzabot_core.plane import Plane, Point, OutOfPlane, ImpossibleMove, WrongGeometry
from pizzabot_core.utils.route import build_route, get_optimal_points_order
from pizzabot_core.utils.point_with_action import PointWithActions


def get_movement_instructions(size_x: int, size_y: int, points: list[Point], action_sign: str):
    try:
        # Initializing plane
        plane = Plane(size_x, size_y)

        # Adding actions to the delivery points
        delivery_points = get_optimal_points_order(points)
        delivery_points_with_actions = [PointWithActions(point, [action_sign]) for point in delivery_points]

        # Get and output the result
        commands = build_route(plane, delivery_points_with_actions)
        return True, commands
    except (WrongGeometry, ImpossibleMove, OutOfPlane) as e:
        return False, e.args[0]
    except Exception:
        with open('log.txt', 'w', encoding='utf-8') as f:
            traceback.print_exc(file=f)
        return False, 'Ooops, something went wrong. We do not know what...'
