# # # prompt = {
# # #     "name": "code_reviewer",
# # #     "category": "coding",
# # #     "version": 1,
# # #     "is_active": True
# # # }


# # # print(prompt["name"])
# # # # print(prompt["llm"]) # not safe
# # # print(prompt.get("llm")) # returns none
# # # ans = prompt["version"] = 3.   # imp this will return the key indirectly
# # # print(ans)
# # # print(prompt)



# # # print(prompt.keys())
# # # print(prompt.items())
# # # print(prompt.values())


# # #----- exercise

# # prompt_dictionary = {
# #     "name": "assistant_general",
# #     "category": "general",
# #     "system_prompt": "You are a helpful, concise, and friendly AI assistant.",
# #     "version": "1.0.0",
# #     "is_active": True,
# # }
# # '''
# # Print the prompt name.
# # Print the category.
# # Change the version.
# # Add a description.
# # Check whether "category" exists.
# # Print all keys.
# # Print all values.
# # Print all key-value pairs.
# # Remove description.'''


# # print(prompt_dictionary["name"])
# # print(prompt_dictionary["category"])
# # prompt_dictionary["version"] = "1.1.0"

# # prompt_dictionary["description"] = "A helpful AI agent."

# # print(prompt_dictionary)

# # if prompt_dictionary.get("category") is not None:
# #     print("Exists")
# # else:
# #     print("Dosen't exists")


# # print(prompt_dictionary.keys())

# # print(prompt_dictionary.values())

# # print(prompt_dictionary.items())

# # del prompt_dictionary["description"]

# # print(prompt_dictionary)



# # -- lets increase the difficulty 

# '''Print the first prompt's name.
# Print the second prompt's category.
# Change the third prompt's version.
# Add a description to the first prompt.
# Print the total number of prompts.'''

# keys = list(prompt_dictionary.keys())
# print(keys)

# print(prompt_dictionary[keys[0]])
# print(prompt_dictionary[keys[1]])
# print(prompt_dictionary[keys[3]])

# prompt_dictionary[keys[0]]["description"] = "Most friendly AI assistant."

# for k in keys:
#     print(prompt_dictionary[k])
#     print()


# print("Total number of prompts: ",len(prompt_dictionary))




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


for idx,jso in enumerate(prompt_dictionary):   # we must know about dictonary in detail buddy
    print(idx, prompt_dictionary[jso], sep = "->") 