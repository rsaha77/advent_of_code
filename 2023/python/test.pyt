def shortestPath(self, src: int):
        # Create a priority queue to store vertices that
        # are being preprocessed
        pq = []
        heapq.heappush(pq, (0, src))
 
        # Create a vector for distances and initialize all
        # distances as infinite (INF)
        dist = [float('inf')] * self.V
        dist[src] = 0
 
        while pq:
            # The first vertex in pair is the minimum distance
            # vertex, extract it from priority queue.
            # vertex label is stored in second of pair
            d, u = heapq.heappop(pq)
 
            # 'i' is used to get all adjacent vertices of a
            # vertex
            for v, weight in self.adj[u]:
                # If there is shorted path to v through u.
                if dist[v] > dist[u] + weight:
                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
 
        # Print shortest distances stored in dist[]
        for i in range(self.V):
            print(f"{i} \t\t {dist[i]}")
            print(f"{i} \t\t {dist[i]}")