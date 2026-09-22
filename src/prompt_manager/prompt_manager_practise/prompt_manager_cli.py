#lets build the project

import re
import sys



def print_prompt_dictonary(data:dict) -> dict:

    k = data.keys()

    for idx,k in enumerate(data,1):
        print(f"{idx}: {data[k]}")





prompt_dictionary = {
    "assistant_general": {
        "name": "assistant_general",
        "category": "general",
        "system_prompt": "You are a helpful, concise, and friendly AI assistant.",
        "version": "1.0.0",
        "is_active": True,
    },
    "coder_python": {
        "name": "coder_python",
        "category": "coding",
        "system_prompt": "You are a senior Python engineer. Write clean, PEP 8-compliant, well-documented code.",
        "version": "1.2.0",
        "is_active": True,
    },
    "researcher_analyst": {
        "name": "researcher_analyst",
        "category": "research",
        "system_prompt": "You are a meticulous research analyst. Break problems into sub-questions and present structured findings.",
        "version": "1.0.1",
        "is_active": True,
    },
    "customer_support": {
        "name": "customer_support",
        "category": "support",
        "system_prompt": "You are a polite customer support agent. Acknowledge the issue and give clear step-by-step help.",
        "version": "1.1.0",
        "is_active": True,
    },
    "summarizer": {
        "name": "summarizer",
        "category": "utility",
        "system_prompt": "You are a summarization expert. Condense input into key bullet points without inventing details.",
        "version": "1.0.0",
        "is_active": True,
    },
    "legacy_translator": {
        "name": "legacy_translator",
        "category": "utility",
        "system_prompt": "You are a translator. Translate input into the target language while preserving tone.",
        "version": "0.9.0",
        "is_active": False,
    },
}



# lets display all prompt names

# print(list(prompt_dictionary.keys()))

# # finsing one prompt by name

# if "customer_support" in prompt_dictionary.keys():
#     print(prompt_dictionary["customer_support"])
# else:
#     print("Prompt does not exist")



# # imagine user provides

# name = input("Your prompt name: ").strip().lower()
# category = input("Enter the category: ").strip().lower()
# system_prompt = input("Enter the system prompt: ").strip().lower()
# version = input("Enter the version(eg: 1.0.0)").strip()
# is_active = input("Is it active(True/False): ")  # because any non empty string is true

# is_active = True if is_active!="" and is_active == True else False


# # lets build a dictionary

# prompt = {
#     "name":name,
#     "category":category,
#     "system_prompt":system_prompt,
#     "version":version,
#     "is_active":is_active
# }

# prompt_dictionary[name] = prompt # it will add 



# print(prompt_dictionary[name])

# print(f"Total number of prompts: {len(prompt_dictionary)}")




# assignment 2 Stage 2 — Create Prompt + Validation


# name = input("Your prompt name: ").strip().lower()
# category = input("Enter the category: ").strip().lower()
# system_prompt = input("Enter the system prompt: ").strip()
# version = input("Enter the version (eg: 1.0.0): ").strip()
# is_active = input("Is it active(True/False): ").strip().lower()  # because any non empty string is true



# #;ets validate 

# VALID_CATEGORIES = {
#     "general",
#     "coding",
#     "research",
#     "support",
#     "utility"
# }


# # we don;t want duplicate names 

# if name!= "" and (name  not in  prompt_dictionary.keys()):
#     #lets validate categoroes
#     if category != "" and category in VALID_CATEGORIES:
#         # we dont need empty system prompt
#         if system_prompt != "":
#             # we need to match version
#             pattern = r"^\d+\.\d+\.\d+$"

#             if re.match(pattern, version):
#             # we only need true/false for 
#                 if is_active in ("true","false"):
#                     is_active = (is_active == "true") # it will conver automatically
#                     #Then we will insert our new dictonary
#                     prompt = {
#                                     "name":name,
#                                     "category":category,
#                                     "system_prompt":system_prompt,
#                                     "version":version,
#                                     "is_active":is_active
#                                 }

#                     prompt_dictionary[name] = prompt # it will add 
#                     print("Prompt created successfully!")


#                     # lets print that prompt 

#                     print_prompt_dictonary(prompt_dictionary)
#                 else:
#                     print("Invalid active status, please enter true/false.")
#             else:
#                 print("Invalid version. Use format: MAJOR.MINOR.PATCH (e.g. 1.0.0)")
#         else:
#             print("System prompt cannot be empty.")
#     else:
#         print("Invalid categor.y")
# else:
#     print("Prompt already exists.") if name != "" else print("name cannot be empty.")





# lets perform our tasks


# print("========== PROMPTS ==========")


# for idx,prompt_key in enumerate(prompt_dictionary,1):

#     if prompt_dictionary[prompt_key]["is_active"]:
#          print(f"{idx}. {prompt_key} - Active")
#     else:
#          print(f"{idx}. {prompt_key} - Inactive")


# print("==============================")

# print(f"Total Prompts: {len(prompt_dictionary)}")




