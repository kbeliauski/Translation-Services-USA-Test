from operator import itemgetter
from typing import List, Dict, Any, Optional
from functools import reduce

# Type alias for better readability
ArrayType = List[Dict[str, Any]]


# 1. Function to filter unique records by 'id', keeping the last occurrence
def filter_unique_records(arr: Optional[ArrayType]) -> ArrayType:
    """
    Filters the list of dictionaries to remove duplicate entries based on the 'id' key.
    Keeps the last occurrence of each unique 'id'. The input list is expected to contain
    dictionaries with at least an 'id' field.

    :param arr: Optional list of dictionaries containing 'id' and other fields.
    :return: A list of unique dictionaries by 'id'.
    :raises ValueError: If the input array is None or empty.
    :raises KeyError: If 'id' is missing from any dictionary in the input.
    """

    # 1. Handle cases where input is None or an empty list
    if not arr:
        raise ValueError(
            "Input array is empty or None. Please provide a valid list of dictionaries.")

    try:
        # 2. Sort the array by 'id' in descending order to ensure that we keep the last occurrence of each 'id'
        sorted_arr = sorted(arr, key=itemgetter("id"), reverse=True)

        # 3. Use reduce to accumulate a dictionary that removes duplicates based on 'id'
        # The lambda function merges the dictionaries and keeps the last occurrence for each 'id'
        unique_dict = reduce(lambda carry, item: {
                             **carry, item['id']: item}, sorted_arr, {})

        # 4. Return the unique records as a list
        return list(unique_dict.values())

    except KeyError as e:
        # Handle missing 'id' key in any dictionary
        raise KeyError(
            f"One or more dictionaries are missing the required 'id' key: {e}") from e
    except TypeError as e:
        # Handle invalid types being passed to the function (e.g., if 'id' is not hashable or the input isn't a list of dictionaries)
        raise TypeError(
            f"Invalid data type encountered in the input array: {e}") from e

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
        # Create a key-value dictionary from the array
        return reduce(lambda carry, item: {**carry, item['title']: item['id']}, arr, {})
    except KeyError as e:
        raise KeyError(
            f"Missing 'title' or 'id' key in one or more dictionaries: {e}") from e


def main():
    # Sample data for testing
    sample_data = [
        {'id': 1, 'title': 'First', 'create': '2024-01-01'},
        {'id': 2, 'title': 'Second', 'create': '2024-01-02'},
        {'id': 1, 'title': 'First Updated', 'create': '2024-01-03'},
        {'id': 3, 'title': 'Third', 'create': '2024-01-01'},
        {'id': 2, 'title': 'Second Updated', 'create': '2024-01-02'}
    ]

    print("Original Data:")
    print(sample_data)

    # Testing filter_unique_records
    unique_records = filter_unique_records(sample_data)
    print("\nUnique Records by 'id':")
    print(unique_records)

    # Testing sort_array_by_key
    sorted_records = sort_array_by_key(sample_data, 'create')
    print("\nSorted Records by 'create':")
    print(sorted_records)

    # Testing filter_by_condition
    filtered_records = filter_by_condition(sample_data, 'id', 1)
    print("\nFiltered Records by condition (id == 1):")
    print(filtered_records)

    # Testing transform_to_key_value
    key_value_map = transform_to_key_value(sample_data)
    print("\nTransformed to Key-Value Map (title -> id):")
    print(key_value_map)


if __name__ == "__main__":
    main()
