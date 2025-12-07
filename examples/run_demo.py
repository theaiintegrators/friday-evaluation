import os
from friday_evaluation.evaluator import Evaluator

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))

if __name__ == "__main__":
    evaluator = Evaluator(
        task_path=os.path.join(ROOT_DIR, "evaluations/tasks/sample_task.json"),
        dataset_path=os.path.join(ROOT_DIR, "evaluations/datasets/sample_dataset.json"),
        rubric_path=os.path.join(ROOT_DIR, "evaluations/rubrics/sample_rubric.json"),
    )
    results = evaluator.run(mock_mode=True)
    evaluator.print_report(results)
