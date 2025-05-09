import json
from src.utils import generate_creative_brief
from src.models import UserInput
from src.constants import user_input_data

def main():

    user_input = UserInput(**user_input_data)
    result = generate_creative_brief(user_input)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
