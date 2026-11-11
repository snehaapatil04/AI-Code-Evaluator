
def evaluate_code(solution, test_cases):
    results = []

    for test in test_cases:
        try:
            actual = solution(test["input"])
            expected = test["expected"]

            passed = actual == expected

            results.append({
                "input": test["input"],
                "expected": expected,
                "actual": actual,
                "status": "PASSED" if passed else "FAILED"
            })

        except Exception as error:
            results.append({
                "input": test["input"],
                "expected": test["expected"],
                "actual": None,
                "status": "ERROR",
                "error": str(error)
            })

    return results


def generate_report(results):
    total = len(results)
    passed = sum(r["status"] == "PASSED" for r in results)
    failed = sum(r["status"] == "FAILED" for r in results)
    errors = sum(r["status"] == "ERROR" for r in results)

    print("\n========== EVALUATION REPORT ==========")
    print(f"Total test cases : {total}")
    print(f"Passed           : {passed}")
    print(f"Failed           : {failed}")
    print(f"Errors           : {errors}")

    if total:
        print(f"Pass rate        : {passed / total * 100:.1f}%")

    print("=======================================")
