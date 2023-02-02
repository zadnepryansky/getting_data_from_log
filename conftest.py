import time

import pytest
import time
START = time.time()


@pytest.fixture
def lets_start():
    global START
    print(f'Test is run {START - time.time()}')

