import json

def save_dict_to_json(file_name: str, data: dict) -> None:
    with open(file_name, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__=='__main__':
    file_name = r"testing_creation.json"
    example_dict = {
        "nested_dict": {
            "subdict_item_1": 'foo',
            "subdict_item_2": 'bar',
        },
        "nested_dict": {
            "subdict_item_1": 'foo',
            "subdict_item_2": 'bar',
        }
    }
    save_dict_to_json(file_name, example_dict)