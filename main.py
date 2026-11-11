
from evaluator import evaluate_code, generate_report


# Sample solution to evaluate
def candidate_solution(numbers):
    return sum(numbers)


# Test cases
test_cases = [
    {"input": [1, 2, 3], "expected": 6},
    {"input": [0, 0, 0], "expected": 0},
    {"input": [-1, 1], "expected": 0},
    {"input": [10, 20], "expected": 30},
    {"input": [5, 5], "expected": 11},  # Intentional failure
    {"input": [], "expected": 0},
    {"input": [7], "expected": 7},
    {"input": [-5, -10], "expected": -15},
    {"input": [1000000, 2000000], "expected": 3000000}
]


# Run evaluation
results = evaluate_code(candidate_solution, test_cases)

print("\n========== INDIVIDUAL TEST RESULTS ==========")

for index, result in enumerate(results, start=1):
    print(f"\nTest Case {index}")
    print(f"Input: {result['input']}")
    print(f"Expected: {result['expected']}")
    print(f"Actual: {result['actual']}")
    print(f"Status: {result['status']}")

    if "error" in result:
        print(f"Error: {result['error']}")


# Generate final report
generate_report(results)
