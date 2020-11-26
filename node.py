import anytree as at
from base import Action


class Node(at.Node):

    def __init__(self, graph_node: 'str', parent=None):
        super().__init__(graph_node, parent=parent)
        self.action = None
        self.g = self.get_g()
        if self.parent:
            parentY, parentX = tuple([int(number)
                                      for number in parent.name.split(',')])
            y, x = tuple([int(number) for number in graph_node.split(',')])
            diff_x = parentX - x
            diff_y = parentY - y
            if diff_x == 1 and diff_y == 0:
                self.action = Action.LEFT
            elif diff_x == -1 and diff_y == 0:
                self.action = Action.RIGHT
            elif diff_x == 0 and diff_y == 1:
                self.action = Action.UP
            elif diff_x == 0 and diff_y == -1:
                self. action = Action.DOWN
            else:
                pass

    def get_g(self):
        if self.parent:
            return self.parent.get_g() + 1
        else:
            return 0
