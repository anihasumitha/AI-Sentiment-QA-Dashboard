def predict_sentiment(text):
    text = text.lower()
    if any(word in text for word in ['love', 'best', 'happy', 'amazing', 'fantastic', 'great']):
        return "Positive"
    elif any(word in text for word in ['terrible', 'horrible', 'bad', 'waste', 'disappointed', 'crash']):
        return "Negative"
    else:
        return "Neutral"
