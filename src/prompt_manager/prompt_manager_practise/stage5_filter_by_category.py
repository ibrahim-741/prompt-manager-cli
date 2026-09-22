# lets begin

from prompt_manager.prompt_manager_practise.prompt_manager_cli import prompt_dictionary


# we shall implement the same functionality but for category

# whatever category we enter we must extract those all prompts 
#lets extract all categories
#my own logic

categories = set()  # this is imp
# lets even design a dictonary category wise
# lets extract the categories 
for key, value in prompt_dictionary.items():
    if value["category"] not in categories:
        categories.add(value["category"])


# lets even design a dictonary category wise

category_wise_prompts = {category:[] for category in categories}
for cat,prompt_list in category_wise_prompts.items():
    for key,value in prompt_dictionary.items():
        if value["category"] == cat:
            prompt_list.append(value)


# lets represent the prompts category wise 

# lets show him what all categories we have


if __name__ == "__main__":
    
    print("Here is the List of categories...")
    for category in categories:
        print(category)
    user_input = input("Enter the category name: ").strip().lower()
    #now lets see weather that prompt is there or not 

    if user_input in categories:
        print(f"========== {user_input.upper()} PROMPTS ==========")
        print(category_wise_prompts[user_input])

    else:
        print("category does not exists!")
