def clean_data(data):
    cleaned = []

    for item in data:
        if item is not None:
            cleaned.append(item)

    return cleaned


if __name__ == "__main__":
    raw_data = [1, 2, None, 4]
    final_data = clean_data(raw_data)
    print(final_data)