import argparse
import json
from typing import List, Dict

def parse_arguments() -> None:
    parser = argparse.ArgumentParser(description="Sets the environment variable ALL_PARTICIPANTS from a given keypath")
    parser.add_argument("keypath", type=str, default=None, help="The relative keypath to the json file containing the keys you'd like to set")
    return parser.parse_args()


def load_keys() -> List[Dict[str, str]]:
    args = parse_arguments()
    keypath = args.keypath
    
    try:
        with open(keypath, "r", encoding="utf-8") as f:
            list_of_keys = json.load(f)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    # print(keys)
    return list_of_keys


def parse_public_keys(keys: List[Dict[str, str]]) -> List[str]:
    public_keys = []
    for key in keys:
        # print(keys)
        public_keys.append(key["address"])
    # print(public_keys)
    return public_keys

def construct_string(addresses: List[str]) -> str:
    value_string = ', '.join([f'\"{address}\"' for address in addresses])
    return f"export ALL_PARTICIPANTS='[{value_string}]'"
    

def main() -> None:
    loaded_keys = load_keys()
    public_keys = parse_public_keys(loaded_keys)
    command_string = construct_string(public_keys)
    print(f"All participants command:\n{command_string}")
    
    
if __name__ == "__main__":
    main()