import sys
from utils.ai_model_stub import predict_sentiment

if len(sys.argv) != 3:
    print(" Usage: python run_single_test.py \"<input sentence>\" \"<expected sentiment>\"")
    sys.exit(1)

test_input = sys.argv[1]
expected_output = sys.argv[2]

# Run model prediction
actual_output = predict_sentiment(test_input)

# Display results
print("----------- SENTIMENT TEST -----------")
print(f"Input: {test_input}")
print(f"Expected Output: {expected_output}")
print(f"Actual Output: {actual_output}")

# Evaluate
if actual_output == expected_output:
    print(" Test Passed")
else:
    print(" Test Failed")
