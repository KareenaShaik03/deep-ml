import math

def softmax(scores: list[float]) -> list[float]:
    
    max_score = max(scores)

    exp_score = [math.exp(score - max_score) for score in scores]
    total = sum(exp_score)

    result = [value/total for value in exp_score]
    return [round(value, 4) for value in result]