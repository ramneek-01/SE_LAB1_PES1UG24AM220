def parse_request(text):
    if not isinstance(text, str):
        raise TypeError("request must be a string")

    parts = text.split("->")
    if len(parts) != 2:
        raise ValueError("request must contain one '->' separator")

    start_text, end_text = (part.strip() for part in parts)
    if not start_text or not end_text:
        raise ValueError("both start and destination floors are required")

    try:
        start = int(start_text)
        end = int(end_text)
    except ValueError as exc:
        raise ValueError("floors must be integers") from exc

    return start, end


def total_travel(floors_csv):
    if not isinstance(floors_csv, str):
        raise TypeError("floor list must be a string")

    if not floors_csv.strip():
        raise ValueError("at least one floor is required")

    values = floors_csv.split(",")
    if any(not value.strip() for value in values):
        raise ValueError("floor list contains an empty value")

    try:
        floors = [int(value.strip()) for value in values]
    except ValueError as exc:
        raise ValueError("all floors must be integers") from exc

    return sum(abs(floors[index + 1] - floors[index]) for index in range(len(floors) - 1))


def load_percent(text):
    if not isinstance(text, str):
        raise TypeError("load must be provided as a string")

    parts = text.split(" of ")
    if len(parts) != 2:
        raise ValueError("load must use the format 'X of Y'")

    load_text, capacity_text = (part.strip() for part in parts)
    if not load_text or not capacity_text:
        raise ValueError("load and capacity are required")

    try:
        load = int(load_text)
        capacity = int(capacity_text)
    except ValueError as exc:
        raise ValueError("load and capacity must be integers") from exc

    if load < 0:
        raise ValueError("load cannot be negative")
    if capacity <= 0:
        raise ValueError("capacity must be greater than zero")

    return load * 100 // capacity


def main():
    print("==== Running parse_request ====")
    user_input = input("Enter a request as FROM->TO (e.g. 5->9): ")
    result = parse_request(user_input)
    print("From and To:", result)

    print("\n==== Running total_travel ====")
    user_input = input("Enter floors visited as CSV (e.g. 1,5,3,9): ")
    result = total_travel(user_input)
    print("Floors Travelled:", result)

    print("\n==== Running load_percent ====")
    user_input = input("Enter load as 'X of Y' (e.g. 450 of 630): ")
    result = load_percent(user_input)
    print("Load Percent:", result)


if __name__ == "__main__":
    main()
