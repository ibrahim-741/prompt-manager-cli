import copy

from prompt_manager.prompt_manager_practise.prompt_manager_cli import prompt_dictionary

temp = copy.deepcopy(prompt_dictionary)


# lets delete

prompt_names = list(temp.keys())
print("Available prompt names:\n")
print(prompt_names)
prompt_name = input("Enter the prompt name you want to delete: ").strip().lower()

if prompt_name in prompt_names:

    # ask for conformation 
    decision = input("Are you sure you want to delete it permanently(y/n): ").strip().lower()
    if decision == "y":
        del temp[prompt_name]
    elif decision == "n":
        print("No deletion.")

    else:
        print("please enter valid conformation for deletion.")

else:
    print("invalid prompt name")



print(prompt_dictionary[prompt_name])


print(temp.get(prompt_name)) # will return none is deleted