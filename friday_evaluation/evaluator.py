from .loader import load_json

class Evaluator:
    def __init__(self, task_path, dataset_path, rubric_path):
        self.task = load_json(task_path)
        self.dataset = load_json(dataset_path)
        self.rubric = load_json(rubric_path)

    def score(self, pred, expected):
        return 1.0 if pred == expected else 0.0

    def run(self, mock_mode=True):
        results = []
        for test in self.dataset.get("tests", []):
            expected = test["expected"]
            pred = expected if mock_mode else None
            results.append({
                "input": test["input"],
                "expected": expected,
                "predicted": pred,
                "score": self.score(pred, expected)
            })
        return results

    def print_report(self, results):
        total = sum(r["score"] for r in results)
        pct = (total / len(results)) * 100
        print("===== Friday Evaluation Demo =====")
        print(f"Task: {self.task['task_name']}")
        print(f"Tests: {len(results)}")
        print("\nResults:")
        for r in results:
            print(f"- {r['input']} → Score: {r['score']}")
        print(f"\nFinal Score: {pct:.1f}%")
