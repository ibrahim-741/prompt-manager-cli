

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

# lets implement search functionalily

# prompt_names = list(prompt_dictionary)
# print(f"choose from this list of prompt names: ",prompt_names)
# user_input = input("Enter thr prompt name: ").strip().lower()


# if user_input != "" and user_input in prompt_names:

#     for key,value in prompt_dictionary[user_input].items():
#         print(f"{key.capitalize()}: {value}")

# else:
#     print("Invalid prompt name.")



# lets implement partial search

user_input = input("Enter thr prompt name: ").strip().lower()

#lets find all matches substring

matches = [name for name in prompt_dictionary if user_input in name.lower()]



# lets handle possible outcomes

if len(matches) == 0:
    print("Invalid prompt name.")

elif len(matches) == 1 and user_input in prompt_dictionary:  # it will make sure
    # we got out prompt name
    for key,value in prompt_dictionary[user_input].items():
         print(f"{key.capitalize()}: {value}")

else:
    # lets show menu and user will pick.
    print("The available prompt names are: ",matches)
    user_prompt_name = input("Choose any one of them: ").strip().lower()
    # still user can make mistake
    if user_prompt_name in matches:
        for key,value in prompt_dictionary[user_prompt_name].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Sorry you have entered a wrong prompt name! for security reasons we have ended the session, try login after an hour.")

