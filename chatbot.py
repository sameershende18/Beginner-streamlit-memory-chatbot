import config
import llm_client
import memory

EXIT_COMMAND = ["exit","quit"]




def build_message(user_input: str) -> list[dict]:
    messages = [
        {"role": "system", "content": config.SYSTEM_PROMPT}
    ]

   
    messages.extend(memory.get_history())

    messages.append({
        "role": "user",
        "content": user_input
    })


    return messages



def main() -> None:
    print("CHATBOT WITH MEMORY")
    print(f"Provider: {config.LLM_PROVIDER}")
    print("Type 'exit' or 'quite to stop\n")

    configuration_error = config.get_configuration_error()

    if configuration_error:
        print(f"Configuration Problem: {configuration_error}")
        return

    while True:

        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!!")
            return
        if not user_input:
            print("Please type a question.\n")
            return
        if user_input in EXIT_COMMAND:
            print("\nGoodbye!!")
            return

        try:
            reply = llm_client.get_llm_reponse(build_message(user_input))
        except Exception as error:
            print(f"\nSorry, something went wrong: {error}\n")
            continue

        memory.add_user_message(user_input)
        memory.add_assistant_message(reply)

        print(f"\nAssistant: {reply}\n")


if __name__ == "__main__":
    main()