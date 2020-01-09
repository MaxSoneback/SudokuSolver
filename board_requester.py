import requests
import json


def request_board(url, size, level):
    params = {
        "size": size,
        "level": level
    }
    try:
        r = requests.get(url=url, params=params, timeout=5)
        data = r.json()
        #  print(data)
        if data["response"]:
            board = generate_board(data["squares"], size)
            return board
    except requests.exceptions.ReadTimeout:
        return None


def generate_board(squares, size):
    board = []
    for i in range(size):
        empty_row = [0] * size
        board.append(empty_row)
    for square in squares:
        board[square["y"]][square["x"]] = square["value"]
    return board
