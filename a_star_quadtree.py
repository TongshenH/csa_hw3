import queue
import quadtreemap


def _get_movements_4n(qtm, tile):
    neighborList = []
    neighborList.append(qtm.quadtree.tileIntersect(quadtreemap.BoundingBox(tile.boundary.x0-1, tile.boundary.y0,
                                                                    tile.boundary.width+2, tile.boundary.height)))
    neighborList.append(qtm.quadtree.tileIntersect(quadtreemap.BoundingBox(tile.boundary.x0, tile.boundary.y0-1,
                                                                    tile.boundary.width, tile.boundary.height+2)))
    movements = [(til, quadtreemap.Point.disOf2Points(tile.getCenter(), til.getCenter())) for til in neighborList]
    return movements


def _get_movements_8n(qtm: quadtreemap.QuadTreeMap, tile: quadtreemap.Tile):
    neighborList = qtm.quadtree.tileIntersect(quadtreemap.BoundingBox(tile.boundary.x0-1, tile.boundary.y0-1,
                                            tile.boundary.width+2, tile.boundary.height+2))
    movements = [(til, quadtreemap.Point.disOf2Points(tile.getCenter(), til.getCenter())) for til in neighborList]
    return movements


def a_star_quadtree(start_m, goal_m, qtm, movement='8n'):
    """
    A* for quadtree.

    :param start_m: start node (x, y) in meters
    :param goal_m: goal node (x, y) in meters
    :param qtm: the quadtree map
    :param movement: select between 4-connectivity ('4N') and 8-connectivity ('8N', default)

    :return: a tuple that contains: (the resulting path, the resulting path in data array indices)
    """
    start_m_ = quadtreemap.Point(*start_m)
    goal_m_ = quadtreemap.Point(*goal_m)

    # get array indices of start and goal
    start = qtm.quadtree.searchTileByIdx(start_m_)
    goal = qtm.quadtree.searchTileByIdx(goal_m_)

    # check if start and goal nodes correspond to free spaces
    if not start or start.tile_points:
        raise Exception('Start node is not traversable')
    if not goal or goal.tile_points:
        raise Exception('Goal node is not traversable')

    # Init variables to save intermediate results
    path_record = {}
    candidates = queue.PriorityQueue()

    # Init the first step
    start_node_cost = 0.0
    start_node_estimated_cost_to_goal = quadtreemap.Point.disOf2Points(start_m_, goal_m_) + start_node_cost
    candidates.put((start_node_estimated_cost_to_goal, start_node_cost, None, start))

    while candidates:
        # Retrieve a candidate
        estimated_cost, dis, prev_node, curr_node = candidates.get()

        # Stop if reached the goal
        if curr_node == goal:
            path_record[curr_node] = prev_node
            break

        # Continue if the node is visited
        if curr_node in path_record:
            continue

        # Record the previous node
        path_record[curr_node] = prev_node

        # Get possible movements
        if movement == '4N':
            movements = _get_movements_4n(qtm, curr_node)
        elif movement == '8N':
            movements = _get_movements_8n(qtm, curr_node)
        else:
            raise ValueError('Unknown movement')

        # Check all neighbors
        for til, delta_cost in movements:
            # check whether new position is inside the map or is an obstacle
            # if not, skip node
            if til.tile_points:
                continue

            if til not in path_record:
                new_cost = dis + delta_cost
                new_total_cost_to_goal = new_cost + quadtreemap.Point.disOf2Points(til.getCenter(), goal.getCenter())
                candidates.put((new_total_cost_to_goal, new_cost, curr_node, til))

    # reconstruct path backwards (only if we reached the goal)
    path = []
    path_idx = []

    if goal in path_record:
        node = goal
        while node:
            path_idx.append(node)
            node = path_record[node]
        # reverse so that path is from start to goal.
        path.reverse()
        path_idx.reverse()
    return path, path_idx