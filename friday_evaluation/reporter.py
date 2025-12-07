def generate_summary(results):
    total = sum(r["score"] for r in results)
    return {
        "total_tests": len(results),
        "average_score": total / len(results)
    }
