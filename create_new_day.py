from dotenv import load_dotenv
import os
import argparse
import requests
from bs4 import BeautifulSoup
import html2text

#define language current options: python, go
LANG = "python"
#define what day to create
DAY = "20"
#define if u want to omit day via arg
PARSE_DAY = False
#your advent of code dir
PROJECT_DIR = ""

def generate_files(day, lang):
    
    if lang == "python":
        filenames = [
            "input",
            "main_part_1",
            "main_part_2",
            "problem_1.md",
            "problem_2.md",
        ]
        file_ext = ".py"
    elif lang == "go":
        filenames = [
            "input",
            "main",
            "problem_1.md",
            "problem_2.md",
        ]
        file_ext = ".go"

    for i in range(len(filenames)):
        if "." not in filenames[i]:
            filenames[i] += file_ext

    template_path = "./day_00_template/" + lang
    if PROJECT_DIR:
        output_dir = os.path.join(PROJECT_DIR, f"day_{day}")
    else:
        output_dir = f"./day_{day}"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in filenames:
        with open(os.path.join(template_path, filename), "r") as template_file:
            template_content = template_file.read()

        output_path = os.path.join(output_dir, filename)
        with open(output_path, "w") as output_file:
            if filename == "problem_1.md":
                problem_description = get_problem_description(day)
                if problem_description:
                    output_file.write(problem_description)
            if filename.find("input"):
                output_file.write(template_content.replace("00", day))
            else:
                output_file.write(template_content)
        print(f"Generated file: {output_path}")
    
    input_data = get_input_data(day)
    if input_data:
        filename = os.path.join(output_dir, "input.txt")
        with open(filename, "w") as input_file:
            input_file.write(input_data)
        print(f"Generated file: {filename}")
    else:
        print("Couldn't retrieve input data")


def get_input_data(day):
    day = day.removeprefix("0")
    url = f"https://adventofcode.com/2023/day/{day}/input"
    load_dotenv()
    session_cookie = os.getenv('COOKIE')
    if session_cookie:
        cookies = {
            'session': session_cookie
        }
        response = requests.get(url, cookies=cookies)
        if response.status_code == 200:
            return response.text
    else:
        print("Missing .env variable 'COOKIE' to retrieve personal input data")

def get_problem_description(day):
    day = day.removeprefix("0")
    url = f"https://adventofcode.com/2023/day/{day}"

    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    article = soup.find("article", class_="day-desc")
    if article:
        converter = html2text.HTML2Text()
        converter.ignore_links = False
        markdown = converter.handle(str(article))
        return markdown
    else:
        print('Article with class "day-desc" not found.')
        return False


def main():
    if PARSE_DAY:
        parser = argparse.ArgumentParser(
            description="Generate Python file from a template."
        )
        parser.add_argument("day", type=str, help="What day to create")
        args = parser.parse_args()   
        day = args.day
        generate_files(day, LANG)
    else:
        generate_files(DAY, LANG)


if __name__ == "__main__":
    main()
