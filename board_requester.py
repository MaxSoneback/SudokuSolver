import requests
import json


def request_board(url, size, level):
    params = {
        "size": size,
        "level": level
    }
    r = requests.get(url=url, params=params)
    data = r.json()

    if data["response"]:
        board = generate_board(data["squares"], size)
        return board
    return None


def generate_board(squares, size):
    board = []
    for i in range(size):
        empty_row = [0] * size
        board.append(empty_row)
    for square in squares:
        board[square["y"]][square["x"]] = square["value"]
    return board
