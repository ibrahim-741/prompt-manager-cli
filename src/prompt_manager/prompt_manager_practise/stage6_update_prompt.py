import copy

from prompt_manager.prompt_manager_practise.prompt_manager_cli import prompt_dictionary

# we are building an update prompt guide 
#lets show all prompt names available

prompt_names = [names for names in prompt_dictionary]
print("There are the available prompt names: ")
print(prompt_names)


categories = set()  # this is imp
# lets even design a dictonary category wise
# lets extract the categories 
for key, value in prompt_dictionary.items():
    if value["category"] not in categories:
        categories.add(value["category"])

# now lets ask user the prompt name

temp = copy.deepcopy(prompt_dictionary) #for safety and after the update i will revert back those changes

# we shall update in temp

#lets extract the every prompt keys 

prompt_keys = list(prompt_dictionary[prompt_names[0]].keys())[1:] # i dont need the name

user_input = input("Choose one to update: ").strip().lower()

if user_input in prompt_names:
    #then i will update the prompt
    print("What you want to update: ")
    for k in prompt_keys:
        print(k)

    # 1. Build metric as a single dict
    metric = {key: 0 for key in prompt_keys}
  # 2. Get user input — keep lowercase, strip spaces
    raw = input("Choose aspects to update (comma-separated): ")
    aspects = [n.strip().lower() for n in raw.split(",") if n.strip()]

    # we need to iterate that dictonary now first lets take the thing to be updated

    for aspect in aspects:
        if aspect in metric:
            metric[aspect] = 1

        else:
            print(f"Unknown aspect: {aspect}")

    print(metric)


else:
    print("Invalid prompt name")
    


# its working from here

# lets update each n every step

# finally we will update in the temp actual dictonary


for met in metric:
    # lets update the one whoch the user choosed 
    if met == "category":
        print("Available categories you can choose: ")
        print(categories)
        new_category = input("Enter the new category: ").strip().lower()
        temp[user_input]["category"] = new_category
        print("category updated!...")

    if met == "system_prompt":
        print(f"Previous system prompt(FYI)\n {temp[user_input]["system_prompt"]}")
        new_system_prompt = input("Enter the new system prompt: ").strip().lower()
        temp[user_input]["system_prompt"] = new_system_prompt
        print("system prompt updated!...")

    if met == "version":
        new_version = input("Enter the new version: ").strip()
        temp[user_input]["version"] = new_version
        print("version updated!...")

    if met == "is_active":
        new_decision = input("Enter the active status(True/false): ").strip().lower()
        if new_decision in ("true","false"):
                    new_decision = (new_decision == "true") # it will conver automatically
        temp[user_input]["is_active"] = new_decision
        print("Active status updated!...")



# lets compare 

print("===========================================")
print("\n")
print("Before update")
print(prompt_dictionary[user_input])

print("After update")

print(temp[user_input])
