def manual_center(text, width):
    total_padding = width - len(text)
    if total_padding <= 0:
        return text
    left_side = total_padding // 2
    right_side = total_padding - left_side
    return (" " * left_side) + text + (" " * right_side)