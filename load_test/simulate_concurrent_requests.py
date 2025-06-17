import concurrent.futures
from utils.ai_model_stub import predict_sentiment

test_inputs = [
                  "I love this app!",
                  "This is terrible service",
                  "It's okay, not great but not bad",
                  "Best customer service",
                  "Disappointed",
                  "Fantastic and easy to use",
              ] * 4  # 24 requests total


def run_prediction(text):
    return predict_sentiment(text)


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(run_prediction, test_inputs))

    for i, result in enumerate(results):
        print(f"Request {i + 1}: {result}")


if __name__ == "__main__":
    main()
