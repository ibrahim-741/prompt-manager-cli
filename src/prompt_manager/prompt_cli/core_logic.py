import re

from prompt_manager.prompt_cli.shared_data import temp_dictonary, prompt_dictionary


# Always use temp_dictonary, not prompt_dictionary


# 1: Prompt creation
def prompt_creation() -> None:
    """This method creates a new prompt."""

    # Let's ask the user all the necessary things
    name = input("Your prompt name: ").strip().lower()
    category = input("Enter the category: ").strip().lower()
    system_prompt = input("Enter the system prompt: ").strip()
    version = input("Enter the version (eg: 1.0.0): ").strip()
    is_active = input("Is it active (True/False): ").strip().lower()

    # We must make sure that prompt name is unique because it is the key
    VALID_CATEGORIES = {
        "general",
        "coding",
        "research",
        "support",
        "utility",
    }

    # We will do multiple checks so that every field is accurate
    if name != "" and (name not in temp_dictonary.keys()):
        # Let's validate categories
        if category != "" and category in VALID_CATEGORIES:
            # We don't need an empty system prompt
            if system_prompt != "":
                # We need to match version
                pattern = r"^\d+\.\d+\.\d+$"

                if re.match(pattern, version):
                    # We only need true/false for is_active
                    if is_active in ("true", "false"):
                        is_active = is_active == "true"  # Convert automatically
                        # Then we will insert our new dictionary
                        prompt = {
                            "name": name,
                            "category": category,
                            "system_prompt": system_prompt,
                            "version": version,
                            "is_active": is_active,
                        }

                        temp_dictonary[name] = prompt  # Add it
                        print("Prompt created successfully!")
                    else:
                        print("Invalid active status, please enter true/false.")
                else:
                    print(
                        "Invalid version. Use format: MAJOR.MINOR.PATCH (e.g. 1.0.0)"
                    )
            else:
                print("System prompt cannot be empty.")
        else:
            print("Invalid category")
    else:
        print("Prompt already exists.") if name != "" else print("name cannot be empty.")


def list_prompts(temp_dict: list[dict]) -> None:
    """This method lists the available prompts."""

    for name, info in temp_dict.items():
        print(f"\n📌 {name}")
        for field, val in info.items():
            print(f"   {field}: {val}")


def print_prompt(prompt: dict) -> None:
    """Only meant for use by search_prompts()."""

    if list(prompt.values())[0] is not None:
        print(f"\n📌 {prompt['name']}")
        for field, val in prompt.items():
            print(f"   {field}: {val}")


def search_prompts() -> None:
    """This method searches the required prompt."""

    prompt_names = list(temp_dictonary.keys())
    print("Available prompt names:\n", prompt_names)

    user_input = input("Enter the prompt name: ").strip().lower()

    # Let's find all substring matches
    matches = [name for name in temp_dictonary if user_input in name.lower()]

    # Handling the possible outcomes
    if len(matches) == 0:
        print("Invalid prompt name.")

    elif len(matches) == 1 and user_input in temp_dictonary:
        # We got our prompt name
        print_prompt(temp_dictonary[user_input])

    else:
        # Let's show the menu and the user will pick
        print("The available prompt names are: ", matches)
        user_prompt_name = input("Choose any one of them: ").strip().lower()
        # Still, the user can make a mistake
        if user_prompt_name in matches:
            return temp_dictonary[user_prompt_name]
        else:
            print(
                "Sorry you have entered a wrong prompt name! "
                "For security reasons we have ended the session, "
                "try login after an hour."
            )
    print_prompt({user_input: None})


def filter_by_category() -> None:
    """This method extracts the prompts by category."""

    # Let's extract all categories
    categories = set()

    # Let's design a dictionary category-wise
    # Let's extract the categories
    for key, value in temp_dictonary.items():
        if value["category"] not in categories:
            categories.add(value["category"])

    # Let's ask the user for the specific category
    print("Here is the list of categories...")
    for category in categories:
        print(category)

    user_input = input("Enter the category name: ").strip().lower()

    if user_input not in categories:
        print("Invalid category")
        return

    # So user input matches with the category

    # Let's design a dictionary category-wise
    category_wise_prompts = {category: [] for category in categories}
    for cat, prompt_list in category_wise_prompts.items():
        for key, value in temp_dictonary.items():
            if value["category"] == cat:
                prompt_list.append(value)

    # Let's display the prompts category-wise
    print(f"========== {user_input.upper()} PROMPTS ==========")
    needed_prompts = category_wise_prompts[user_input]
    for prompts in needed_prompts:
        print(f"\n📌 {prompts['name']}")
        for field, val in prompts.items():
            print(f"   {field}: {val}")


def update_prompt() -> None:
    """This method updates the prompt data; if it doesn't exist, creates a new prompt."""

    # Let's show all prompt names available
    prompt_names = [names for names in temp_dictonary]
    print("There are the available prompt names: ")
    print(prompt_names)

    categories = set()

    # Let's extract the categories
    for key, value in temp_dictonary.items():
        if value["category"] not in categories:
            categories.add(value["category"])

    # Let's extract every prompt key
    prompt_keys = list(temp_dictonary[prompt_names[0]].keys())[1:]  # Skip name

    user_input = input("Choose one to update: ").strip().lower()

    if user_input != "" and user_input in prompt_names:
        # Then I will update the prompt

        # Let's show the user the original prompt before update
        print("Original prompt: ")
        print(f"\n📌 {temp_dictonary[user_input]['name']}")
        for field, val in temp_dictonary[user_input].items():
            print(f"   {field}: {val}")
        print()

        print("What you want to update: ")
        for k in prompt_keys:
            print(k)

        # 1. Build metric as a single dict
        metric = {key: 0 for key in prompt_keys}

        # 2. Get user input — keep lowercase, strip spaces
        raw = input("Choose aspects to update (comma-separated): ")
        aspects = [n.strip().lower() for n in raw.split(",") if n.strip()]

        # We need to iterate that dictionary now; first, let's take the thing to be updated
        for aspect in aspects:
            if aspect in metric:
                metric[aspect] = 1
            else:
                print(f"Unknown aspect: {aspect}")

        # Finally we will update in the final dictionary
        for met, val in metric.items():
            # Let's update the one which the user chose

            # We assume the one who updates has knowledge of what he is doing,
            # so no need for pre-checks
            if met == "category" and val == 1:
                print("Available categories you can choose: ")
                print(categories)
                new_category = input("Enter the new category: ").strip().lower()
                temp_dictonary[user_input]["category"] = new_category
                print("category updated!...")

            elif met == "system_prompt" and val == 1:
                print(
                    f"Previous system prompt (FYI)\n "
                    f"{temp_dictonary[user_input]['system_prompt']}"
                )
                new_system_prompt = (
                    input("Enter the new system prompt: ").strip().lower()
                )
                temp_dictonary[user_input]["system_prompt"] = new_system_prompt
                print("system prompt updated!...")

            elif met == "version" and val == 1:
                new_version = input("Enter the new version: ").strip()
                temp_dictonary[user_input]["version"] = new_version
                print("version updated!...")

            elif met == "is_active" and val == 1:
                new_decision = (
                    input("Enter the active status (True/false): ").strip().lower()
                )
                if new_decision in ("true", "false"):
                    new_decision = new_decision == "true"  # Convert automatically
                temp_dictonary[user_input]["is_active"] = new_decision
                print("Active status updated!...")

        # Let's show the user whether the update was reflected

        if user_input in prompt_dictionary:
            print("Updated prompt: ")
            updated_prompt = temp_dictonary[user_input]
            print(f"\n📌 {updated_prompt['name']}")
            for field, val in updated_prompt.items():
                print(f"   {field}: {val}")
            print()

            # An edge case: what if I am updating a new prompt which I have added
            print("Original Prompt: ")
            print(f"\n📌 {prompt_dictionary[user_input]['name']}")
            for field, val in prompt_dictionary[user_input].items():
                print(f"   {field}: {val}")
            print()
        else:
            # I don't need to show the difference for updates on newly created prompts
            print("Updated prompt: ")
            updated_prompt = temp_dictonary[user_input]
            print(f"\n📌 {updated_prompt['name']}")
            for field, val in updated_prompt.items():
                print(f"   {field}: {val}")

    else:
        # Means the prompt name does not exist; let the user create a new prompt
        print(
            "The prompt name does not exist in the prompts library, "
            "so let's create a new prompt"
        )
        prompt_creation()


def delete_prompt() -> None:
    """This method deletes a specific prompt."""

    prompt_names = list(temp_dictonary.keys())
    print("Available prompt names:\n")
    print(prompt_names)

    prompt_name = input("Enter the prompt name you want to delete: ").strip().lower()

    while True:
        if prompt_name in prompt_names:
            # Ask for confirmation
            decision = (
                input("Are you sure you want to delete it permanently (y/n): ")
                .strip()
                .lower()
            )
            if decision == "y":
                del temp_dictonary[prompt_name]
                print("Prompt deleted")
            elif decision == "n":
                print("No deletion.")
            else:
                print("Please enter valid confirmation for deletion.")
                continue

        else:
            print("invalid prompt name")
        break  # Obviously, it will run if we hit success