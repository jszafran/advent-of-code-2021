import time
from datetime import timedelta
from functools import wraps


def measure_execution_time(f):
    @wraps(f)
    def inner(*args, **kwargs):
        start_time = time.monotonic()
        result = f(*args, **kwargs)
        time_elapsed = round(time.monotonic() - start_time, 2)
        print(f"Execution time: {timedelta(seconds=time_elapsed)}")
        return result

    return inner
