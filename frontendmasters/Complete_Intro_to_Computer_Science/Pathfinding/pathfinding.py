class Solution:


    def find_shortest_path_length(self, maze, start_a, start_b):
        NO_ONE = 0
        BY_A = 1
        BY_B = 2
        def get_neighbors(visited, x, y):
            neighbors = []
            if y - 1 >= 0 and not visited[y - 1][x]['closed']:
                neighbors.append(visited[y - 1][x])
            if y + 1 < len(visited) and not visited[y + 1][x]['closed']:
                neighbors.append(visited[y + 1][x])
            if x - 1 >= 0 and not visited[y][x - 1]['closed']:
                neighbors.append(visited[y][x - 1])
            if x + 1 < len(visited[0]) and not visited[y][x + 1]['closed']:
                neighbors.append(visited[y][x + 1])
            return neighbors

        visited = [
            [
                {'closed': cell == 1, 'length': 0, 'openedBy': NO_ONE, 'x': x, 'y': y}
                for x, cell in enumerate(row)
            ]
            for y, row in enumerate(maze)
        ]

        xA, yA = start_a
        xB, yB = start_b
        visited[yA][xA]['openedBy'] = BY_A
        visited[yB][xB]['openedBy'] = BY_B

        a_queue = [visited[yA][xA]]
        b_queue = [visited[yB][xB]]
        iteration = 0

        while a_queue and b_queue:
            iteration += 1
            a_neighbors = []
            for neighbor in a_queue:
                a_neighbors.extend(get_neighbors(visited, neighbor['x'], neighbor['y']))
            a_queue = []
            for neighbor in a_neighbors:
                if neighbor['openedBy'] == BY_B:
                    return neighbor['length'] + iteration
                elif neighbor['openedBy'] == NO_ONE:
                    neighbor['length'] = iteration
                    neighbor['openedBy'] = BY_A
                    a_queue.append(neighbor)

            b_neighbors = []
            for neighbor in b_queue:
                b_neighbors.extend(get_neighbors(visited, neighbor['x'], neighbor['y']))
            b_queue = []
            for neighbor in b_neighbors:
                if neighbor['openedBy'] == BY_A:
                    return neighbor['length'] + iteration
                elif neighbor['openedBy'] == NO_ONE:
                    neighbor['length'] = iteration
                    neighbor['openedBy'] = BY_B
                    b_queue.append(neighbor)

        return -1
