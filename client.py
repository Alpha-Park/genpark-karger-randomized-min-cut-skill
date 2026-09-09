import random

class KargerMinCutSolver:
    """Karger's randomized contraction algorithm."""
    def find_min_cut(self, num_vertices: int, edges: list[tuple[int, int]], trials: int = 10) -> dict:
        best_cut = float('inf')

        for _ in range(trials):
            parent = list(range(num_vertices))
            def find(i):
                if parent[i] != i: parent[i] = find(parent[i])
                return parent[i]
            def union(i, j):
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
                    return True
                return False

            vertices_left = num_vertices
            cur_edges = list(edges)
            random.shuffle(cur_edges)

            for u, v in cur_edges:
                if union(u, v):
                    vertices_left -= 1
                    if vertices_left == 2:
                        break

            cut_size = sum(1 for u, v in edges if find(u) != find(v))
            if cut_size < best_cut:
                best_cut = cut_size

        return {
            "num_vertices": num_vertices,
            "trials_run": trials,
            "min_cut_size": best_cut
        }
