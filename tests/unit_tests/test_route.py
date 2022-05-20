from unittest import TestCase
from pizzabot_core.plane.plane import Plane
from pizzabot_core.utils.route import build_route
from pizzabot_core.utils.point_with_action import PointWithActions


class TestRoute(TestCase):
    def test_built_route(self):
        plane = Plane(5, 5)
        start_point = (0, 0)
        delivery_points = [(3, 2), (3, 3), (1, 0)]
        delivery_points_with_actions = [PointWithActions(point, ['D']) for point in delivery_points]
        expected_commands = ['N', 'N', 'E', 'E', 'E', 'D', 'N', 'D', 'S', 'S', 'S', 'W', 'W', 'D']
        commands = build_route(plane, delivery_points_with_actions, start_point)
        self.assertEqual(expected_commands, commands)
