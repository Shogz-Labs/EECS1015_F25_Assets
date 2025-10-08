import time
from typing import Generator, Any

def stream(message: str) -> Generator[Any, Any, Any]:
    for word in message.split():
        yield word + " "
        time.sleep(0.1)

def write(message: str):
    for word in stream(message):
        print(word, end="") 
    print()

if __name__ == '__main__':
    print('The module is bring executed as the main script!')