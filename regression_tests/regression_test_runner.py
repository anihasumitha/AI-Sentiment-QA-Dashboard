import json
from utils.ai_model_stub import predict_sentiment


def run_regression_tests():
    with open('test_cases/sentiment_test_cases.json') as f:
        test_cases = json.load(f)

    total = len(test_cases)
    passed = 0

    for case in test_cases:
        result = predict_sentiment(case['input'])
        expected = case['expected']
        print(f"Input: '{case['input']}' | Expected: {expected} | Got: {result}")
        if result == expected:
            passed += 1

    print(f"\nPassed {passed} out of {total} test cases.")
    accuracy = (passed / total) * 100
    print(f"Accuracy: {accuracy:.2f}%")


if __name__ == "__main__":
    run_regression_tests()
