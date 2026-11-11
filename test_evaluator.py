
from evaluator import evaluate_code


def add_numbers(a, b):
    return a + b


def wrong_addition(a, b):
    return a - b


def broken_solution(a, b):
    raise ValueError("Something went wrong")


def test_correct_solution():
    test_cases = [
        {"input": (2, 3), "expected": 5},
        {"input": (0, 0), "expected": 0},
        {"input": (-2, 2), "expected": 0}
    ]

    results = evaluate_code(
        lambda values: add_numbers(*values),
        test_cases
    )

    assert all(r["status"] == "PASSED" for r in results)


def test_incorrect_solution():
    test_cases = [
        {"input": (5, 3), "expected": 8}
    ]

    results = evaluate_code(
        lambda values: wrong_addition(*values),
        test_cases
    )

    assert results[0]["status"] == "FAILED"
    assert results[0]["actual"] == 2


def test_solution_with_error():
    test_cases = [
        {"input": (5, 3), "expected": 8}
    ]

    results = evaluate_code(
        lambda values: broken_solution(*values),
        test_cases
    )

    assert results[0]["status"] == "ERROR"
    assert "Something went wrong" in results[0]["error"]



from evaluator import generate_report


def test_evaluation_report(capsys):
    results = [
        {"status": "PASSED"},
        {"status": "FAILED"},
        {"status": "ERROR"}
    ]

    generate_report(results)

    output = capsys.readouterr().out

    assert "Total test cases : 3" in output
    assert "Passed           : 1" in output
    assert "Failed           : 1" in output
    assert "Errors           : 1" in output
