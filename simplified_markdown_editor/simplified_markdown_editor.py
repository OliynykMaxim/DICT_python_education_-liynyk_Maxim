format_dict =  {
    "plain": lambda text: text,
    "bold": lambda text: f"**{text}**",
    "italic": lambda text: f"*{text}*",
    "inline-code": lambda text: f"`{text}`",
    "link": lambda label, url: f"[{label}]({url})",
    "header": lambda level, text: f"{'#' * level} {text}\n",
    "ordered-list": lambda text: f"1. {text}\n",
    "unordered-list": lambda text: f"* {text}\n",
    "new-line": lambda _: "\n",
}


format_list = list(format_dict.keys())


def print_help():
    print("Available formatters:", *format_list)
    print("Special commands: !help !done")


def main():
    # Initialize an empty list to store the formatted text
    formatted_text = []

    while True:
        # Prompt the user for a formatting command
        user_input = input("Choose a formatter: ")

        # Check for special commands
        if user_input == "!help":
            print_help()
        elif user_input == "!done":
            # Join the formatted text list into a single string
            markdown = "".join(formatted_text)
            print(markdown)
            break
        elif user_input not in format_list:
            print("Unknown formatting type or command")
        else:
            # Prompt the user for text to format
            if user_input == "header":
                # Prompt the user for header level and text
                level = int(input("Level: "))
                if level < 1 or level > 6:
                    print("The level should be within the range of 1 to 6.")
                    continue
                text = input("Text: ")
                formatted_text.append(format_dict[user_input](level, text))
            elif user_input == "link":
                # Prompt the user for link label and URL
                label = input("Label: ")
                url = input("URL: ")
                formatted_text.append(format_dict[user_input](label, url))
            else:
                text = input("Text: ")
                formatted_text.append(format_dict[user_input](text))


if __name__ == "__main__":
    main()