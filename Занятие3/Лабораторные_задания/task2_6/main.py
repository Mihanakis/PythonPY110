import json


def task():
    ent_file = "input.json"
    out_file = "output.json"
    with open(ent_file) as f:
        json_data = json.load(f)
        out_data = sorted(json_data, key=lambda item: item["length"])
        with open(out_file, "w") as fp:
            json.dump(out_data, fp, indent=4)  # дополнительно записать отсортированный список в JSON файл

    return out_data


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))