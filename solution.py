import pandas as pd
import numpy as np


chat_id = 5459656416 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 10  # время измерения
    numerator = np.sum(x * t)
    denominator = np.sum(t ** 2)
    return numerator / denominator
