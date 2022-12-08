def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return max(len(word) for word in list_words)

# Альтернатива, но не генератор: max(map(lambda x: len(x), list_words)

if __name__ == "__main__":
    print(task())
