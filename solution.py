import pandas as pd
import numpy as np


chat_id = 5459656416 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    error = np.random.uniform(-1, np.exp(1), n)
    v = x + error
    acceleration = 2 * np.sum(v) / (n * 10)
    return acceleration
