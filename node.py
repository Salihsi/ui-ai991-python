import anytree as at
from base import Action


class Node(at.Node):

    def __init__(self, graph_node: 'str', parent: 'str'):
        super().__init__(graph_node, parent=parent)
        self.action = None
        if parent:
            parentX, parentY = tuple([int(number)
                                      for number in parent.split(',')])
            x, y = tuple([int(number) for number in graph_node.split(',')])
