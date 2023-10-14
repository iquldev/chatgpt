import openai
from colorama import Fore
from colorama import just_fix_windows_console
just_fix_windows_console()

# Enter API key - platform.openai.com
openai.api_key = "API_KEY"

def chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input(Fore.CYAN + "Enter response: ")
        if user_input.lower() in ["stop", "exit"]:
            break

        response = chatgpt(user_input)
        print(Fore.CYAN + "ChatGPT: ", response)
