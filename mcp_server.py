import sys
import json
from client import KargerMinCutSolver

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "min_cut":
        solver = KargerMinCutSolver()
        return solver.find_min_cut(params.get("v", 4), [tuple(e) for e in params.get("edges", [])], params.get("trials", 10))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
