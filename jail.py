from logging import debug, info, basicConfig
from random import choice, randrange

basicConfig(level="INFO")


def get_bitwise_result(n):
    heads = [index for index, number in enumerate(n[::-1]) if number == "1"]
    result = 0
    for value in heads:
        result = result ^ value
    debug(f"Bitwise result of heads {heads} is {result}.")
    return result


def get_coin_to_flip(board_width: int = 8, coin_layout: str = "", where_to_hide: int = -1, draw: bool = True):
    if coin_layout:
        coin_layout = ("0" * ((board_width ** 2) - len(coin_layout)) + coin_layout)
    else:
        coin_layout = "".join([choice(["0", "1"]) for i in range(board_width ** 2)])
    key_is_hidden_at = where_to_hide if where_to_hide != -1 else randrange(0, board_width ** 2)
    info(f"Board size {board_width}×{board_width}; key is hidden at square {key_is_hidden_at}.")
    debug(f"Coin layout: {coin_layout}")
    # First convict
    suggestion = get_bitwise_result(coin_layout)
    coin_to_flip = ((board_width ** 2) - 1) ^ (key_is_hidden_at ^ suggestion)
    info(f"The coin to flip is the one at square {coin_to_flip}.")
    new_layout_as_list = list(coin_layout)
    new_layout_as_list[coin_to_flip] = "1" if new_layout_as_list[coin_to_flip] == "0" else "0"
    new_coin_layout = "".join(new_layout_as_list)
    debug(f"New coin layout: {new_coin_layout}")
    # Second convict
    check_value = get_bitwise_result(new_coin_layout)
    assert check_value == key_is_hidden_at
    info(f"Successful check, key was found at: {check_value}")
    if draw:
        draw_result(board_width, coin_layout, key_is_hidden_at, coin_to_flip)


def draw_result(size: int, layout: str, key: int, flip: int):
    result = ["\n\n*: key location; @: coin to flip"]
    horizontal = "----".join((size + 1) * "+")
    for row in range(size):
        result.append(horizontal)
        column_content = []
        for column in range(size):
            value = row * size + column
            column_content.append(f"{layout[value-1]} {value:2}")
            if flip == value:
                column_content[-1] = column_content[-1][:-2] + " @"
            if key == value:
                column_content[-1] = column_content[-1][:-2] + " *"
        result.append(f"|{'|'.join(column_content)}|")
    result.append(horizontal)
    info("\n".join(result))


def mass_check():
    passed = failed = 0
    for i in range(1000):
        try:
            get_coin_to_flip(draw=False)
            passed += 1
        except AssertionError:
            failed += 1
    info(f"PASS: {passed}; FAIL: {failed}")


get_coin_to_flip()
