import pyperclip
import inquirer


def normalized_file_name_from_url(url: str) -> None:
    parts = url.split("/problems")

    if len(parts) <= 1:
        return

    problem_name = parts[1].split("/")[1]
    question = [
        inquirer.List(
            "choice",
            message="Select file naming convention:",
            choices=["snake_case", "kebab-case"],
        )
    ]

    response = inquirer.prompt(question)
    replacement_char = "_" if response["choice"] == "snake_case" else "-"

    problem_name = str.lower(problem_name).replace("-", replacement_char)
    print(f'copied "{problem_name}" to clipboard')
    pyperclip.copy(problem_name)


if __name__ == "__main__":
    url = input("Enter the LeetCode problem url: ")
    normalized_file_name_from_url(url)
