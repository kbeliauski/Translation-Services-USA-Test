import argparse
import json
from src import *
import os


# Import necessary modules
import os


def main():
    parser = argparse.ArgumentParser(
        description="Run array functions from the terminal.")

    # Define subcommands for each function
    subparsers = parser.add_subparsers(
        dest="command", help="Array function to run")

    # Subcommand for filter_unique_records
    parser_filter_unique = subparsers.add_parser(
        "filter_unique_records", help="Filter unique records by 'id'")
    parser_filter_unique.add_argument(
        "input_file", type=str, help="Path to JSON file containing the input array")

    # Subcommand for sort_array_by_key
    parser_sort_array = subparsers.add_parser(
        "sort_array_by_key", help="Sort array by key")
    parser_sort_array.add_argument(
        "input_file", type=str, help="Path to JSON file containing the input array")
    parser_sort_array.add_argument("key", type=str, help="Key to sort by")

    # Subcommand for filter_by_condition
    parser_filter_condition = subparsers.add_parser(
        "filter_by_condition", help="Filter array by a specific condition")
    parser_filter_condition.add_argument(
        "input_file", type=str, help="Path to JSON file containing the input array")
    parser_filter_condition.add_argument(
        "condition_key", type=str, help="Key to filter by")
    parser_filter_condition.add_argument(
        "condition_value", type=str, help="Value to filter by")

    # Subcommand for transform_to_key_value
    parser_transform = subparsers.add_parser(
        "transform_to_key_value", help="Transform array to key-value map")
    parser_transform.add_argument(
        "input_file", type=str, help="Path to JSON file containing the input array")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if no arguments were provided
    if args.command is None:
        parser.print_help()
        return

    # Check if the specified input file exists
    if not os.path.isfile(args.input_file):
        print(f"Error: The file '{args.input_file}' does not exist.")
        parser.print_help()
        return

    # Read input array from the specified file
    with open(args.input_file, 'r') as f:
        input_array = json.load(f)

    # Run the appropriate function based on the command
    if args.command == "filter_unique_records":
        result = filter_unique_records(input_array)
    elif args.command == "sort_array_by_key":
        result = sort_array_by_key(input_array, args.key)
    elif args.command == "filter_by_condition":
        result = filter_by_condition(
            input_array, args.condition_key, args.condition_value)
    elif args.command == "transform_to_key_value":
        result = transform_to_key_value(input_array)

    # Print the result in JSON format for easy viewing
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
