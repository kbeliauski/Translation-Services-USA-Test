from operator import itemgetter
from typing import List, Dict, Any, Optional

# Type alias for better readability
ArrayType = List[Dict[str, Any]]

# 1. Function to filter unique records by 'id', keeping the last occurrence
def filter_unique_records(arr: Optional[ArrayType]) -> ArrayType:
    """
    Filters the list of dictionaries to remove duplicate entries based on 'id'.
    Keeps the last occurrence of each unique 'id'.
    
    :param arr: List of dictionaries containing 'id' and other fields.
    :return: List of unique dictionaries by 'id'.
    :raises ValueError: If the input array is None or empty.
    :raises KeyError: If 'id' is missing from any dictionary.
    """
    if not arr:
        raise ValueError("Input array is empty or None.")

    try:
        sorted_arr = sorted(arr, key=itemgetter(
            "id"), reverse=True)  # Sort by 'id' descending
        # Dictionary to remove duplicates
        unique_dict = {item["id"]: item for item in sorted_arr}
        return list(unique_dict.values())
    except KeyError as e:
        raise KeyError(
            f"Missing 'id' key in one or more dictionaries: {e}") from e

# 2. Function to sort an array of dictionaries by a given key


def sort_array_by_key(arr: Optional[ArrayType], key: str) -> ArrayType:
    """
    Sorts the list of dictionaries by a specified key.
    
    :param arr: List of dictionaries.
    :param key: Key to sort by (e.g., 'create').
    :return: Sorted list of dictionaries.
    :raises ValueError: If the input array is None or empty.
    :raises KeyError: If the provided key is not present in the dictionaries.
    """
    if not arr:
        raise ValueError("Input array is empty or None.")

    try:
        return sorted(arr, key=itemgetter(key))  # Sort by the provided key
    except KeyError as e:
        raise KeyError(f"Key '{key}' not found in array elements.") from e

# 3. Function to filter records by a condition on a specific key


def filter_by_condition(arr: Optional[ArrayType], condition_key: str, condition_value: Any) -> ArrayType:
    """
    Filters the list of dictionaries based on a specific condition (key-value pair).
    
    :param arr: List of dictionaries.
    :param condition_key: The key to apply the filter on.
    :param condition_value: The value to match.
    :return: Filtered list of dictionaries.
    :raises ValueError: If the input array is None or empty.
    :raises KeyError: If the provided key is not present in the dictionaries.
    """
    if not arr:
        raise ValueError("Input array is empty or None.")

    try:
        return list(filter(lambda x: x.get(condition_key) == condition_value, arr))
    except KeyError as e:
        raise KeyError(
            f"Key '{condition_key}' not found in array elements.") from e

# 4. Function to transform array structure to a key-value map (title as key, id as value)


def transform_to_key_value(arr: Optional[ArrayType]) -> Dict[str, int]:
    """
    Transforms the array into a key-value dictionary where 'title' is the key and 'id' is the value.
    
    :param arr: List of dictionaries.
    :return: Dictionary where keys are 'title' and values are 'id'.
    :raises ValueError: If the input array is None or empty.
    :raises KeyError: If 'title' or 'id' are missing from any dictionary.
    """
    if not arr:
        raise ValueError("Input array is empty or None.")

    try:
        return {item["title"]: item["id"] for item in arr}
    except KeyError as e:
        raise KeyError(
            f"Missing 'title' or 'id' key in one or more dictionaries: {e}") from e
