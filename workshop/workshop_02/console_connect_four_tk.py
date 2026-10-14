import tkinter as tk
from tkinter import messagebox

ROWS = 6
COLS = 7
SLOTS = 4


class FullColumnError(Exception):
    pass


def place_player_choice(ma, c, player_n):
    for r in range(len(ma) - 1, -1, -1):
        if ma[r][c] == 0:
            ma[r][c] = player_n
            return r, c
    raise FullColumnError


def is_player_num(ma, r, c, player_n):
    if r < 0 or c < 0 or r >= len(ma) or c >= len(ma[0]):
        return False
    return ma[r][c] == player_n


def is_vertical_win(ma, r, c, player_n, slots):
    return all(is_player_num(ma, r + idx, c, player_n) for idx in range(slots))


def is_horizontal_win(ma, r, c, player_n, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r, c + idx, player_n):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r, c - idx, player_n):
            filled += 1
        else:
            break
    return filled >= slots


def is_right_diagonal_win(ma, r, c, player_n, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c + idx, player_n):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c - idx, player_n):
            filled += 1
        else:
            break
    return filled >= slots


def is_left_diagonal_win(ma, r, c, player_n, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c - idx, player_n):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c + idx, player_n):
            filled += 1
        else:
            break
    return filled >= slots


def is_winner(ma, r, c, player_n, slots):
    return (is_vertical_win(ma, r, c, player_n, slots) or \
            is_horizontal_win(ma, r, c, player_n, slots) or \
            is_right_diagonal_win(ma, r, c, player_n, slots) or \
            is_left_diagonal_win(ma, r, c, player_n, slots))


def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def update_ui(labels, row, col, player_num):
    color = "red" if player_num == 1 else "blue"
    labels[row][col].config(bg=color)


def handle_column_click(ma, labels, column_num, player_num, rows, cols, slots, counter, root):
    try:
        row, col = place_player_choice(ma, column_num, player_num)
        update_ui(labels, row, col, player_num)
        counter += 1

        if is_winner(ma, row, col, player_num, slots):
            color_name = "Червеният (Играч 1)" if player_num == 1 else "Синият (Играч 2)"
            messagebox.showinfo("Победа!", f"Поздравления! {color_name} спечели!")
            root.destroy()
            return player_num, counter

        if counter == rows * cols:
            messagebox.showinfo("Равенство", "Играта приключи без победител!")
            root.destroy()
            return player_num, counter

        next_player = 2 if player_num == 1 else 1
        return next_player, counter

    except FullColumnError:
        messagebox.showerror("Невалиден ход", "Тази колона е пълна! Изберете друга.")
        return player_num, counter


def create_ui(root, rows, cols, slots):
    matrix = create_matrix(rows, cols)
    labels = [[tk.Label(root, text=" ", relief="solid", width=4, height=2) \
               for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            labels[r][c].grid(row=r + 1, column=c)

    player_state = {"player_num": 1, "counter": 0}

    def on_click(column_num):
        player_state["player_num"], player_state["counter"] = handle_column_click(
            matrix, labels, column_num, player_state["player_num"], rows, cols, slots, player_state["counter"], root
        )

    buttons = [tk.Button(root, text="↓", width=4, height=2, bg="yellow", command=lambda c_idx=col: on_click(c_idx)) \
               for col in range(cols)]

    for col, button in enumerate(buttons):
        button.grid(row=0, column=col)


def start_game():
    root = tk.Tk()
    root.title("Connect Four")
    create_ui(root, ROWS, COLS, SLOTS)
    root.mainloop()


if __name__ == '__main__':
    start_game()