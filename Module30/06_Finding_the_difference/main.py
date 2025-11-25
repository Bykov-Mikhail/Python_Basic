import json
from typing import Any, Dict, List, Union

def find_values_by_key(data: Union[Dict, List], target_key: str) -> List[Any]:
    """
    Рекурсивно находит все значения по ключу в JSON-подобной структуре.
    """
    results = []
    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                results.append(value)
            results.extend(find_values_by_key(value, target_key))
    elif isinstance(data, list):
        for item in data:
            results.extend(find_values_by_key(item, target_key))
    return results


def compare_json_files(
        old_data: Dict[str, Any],
        new_data: Dict[str, Any],
        diff_list: List[str]
) -> Dict[str, Any]:
    """
    Сравнивает два JSON и возвращает словарь {ключ: новое_значение} для ключей из diff_list,
    если значение изменилось.
    """
    result = {}
    for key in diff_list:
        old_values = find_values_by_key(old_data, key)
        new_values = find_values_by_key(new_data, key)

        # Если значения разные (даже количество)
        if old_values != new_values:
            # Берём первое найденное новое значение (как в примере)
            if new_values:
                result[key] = new_values[0]
    return result


# Основной код
if __name__ == "__main__":
    with open('json_old.json', 'r', encoding='utf-8') as f:
        old_json = json.load(f)
    with open('json_new.json', 'r', encoding='utf-8') as f:
        new_json = json.load(f)

    diff_list = ["services", "staff", "datetime"]

    result = compare_json_files(old_json, new_json, diff_list)

    print(result)

    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)





