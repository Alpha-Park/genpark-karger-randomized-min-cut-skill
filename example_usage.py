from client import KargerMinCutSolver

def main():
    print("=== Karger Randomized Min Cut Solver ===")
    solver = KargerMinCutSolver()
    # 4-cycle graph has min cut 2
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    res = solver.find_min_cut(4, edges, trials=15)
    print("Min Cut Result:", res)
    assert res["min_cut_size"] == 2

    print("Karger Min Cut Solver verified successfully!")

if __name__ == "__main__":
    main()
