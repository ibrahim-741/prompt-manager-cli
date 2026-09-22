from prompt_manager.prompt_cli.shared_data import prompt_dictionary, temp_dictonary
from prompt_manager.prompt_cli.core_logic import (
    prompt_creation,
    list_prompts,
    search_prompts,
    print_prompt,
    filter_by_category,
    update_prompt,
    delete_prompt,
)


def show_menu() -> None:
    print("=" * 50)
    print("🤖 Prompt Manager".center(50))
    print("=" * 50)
    print(
        """
1. Create Prompt
2. List Prompts
3. Search Prompt
4. Filter by Category
5. Update Prompt
6. Delete Prompt
7. Exit
"""
    )
    print("=" * 50)


def main() -> None:
    show_menu()

    i = 1
    while True:
        # Ask if the user wants to continue (skip on first iteration)
        if i > 1:
            decision = input("You wanna continue (yes/no): ").strip().lower()
            if decision == "no":
                print(
                    "Thank you for choosing Ibrahim prompt management services.\n"
                    "Visit again :)"
                )
                break
            else:
                show_menu()

        # Ask for the option
        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            i += 1
            continue

        # Handle the option
        if option == 1:
            prompt_creation()
        elif option == 2:
            list_prompts(temp_dictonary)
        elif option == 3:
            search_prompts()
        elif option == 4:
            filter_by_category()
        elif option == 5:
            update_prompt()
        elif option == 6:
            delete_prompt()
        elif option == 7:
            print(
                "Thank you for choosing Ibrahim prompt management services.\n"
                "Visit again :)"
            )
            break
        else:
            print("❌ Invalid option. Please choose 1–7.")

        i += 1


if __name__ == "__main__":
    main()