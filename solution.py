import pandas as pd
import numpy as np


chat_id = 5459656416 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    errors = np.random.uniform(-1, np.exp(1), size=len(x))
    x += errors
    time = 10
    acceleration = 2 * (np.mean(x) / time)**2
    return acceleration
