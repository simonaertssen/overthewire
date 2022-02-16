import os
import re
import requests


def write_to_file(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)


def crawl_bandit():
    url = "https://overthewire.org/wargames/bandit/"

    title = b'<script>renderLevelTitle("bandit", 0);</script>'

    maxgamenum = 34
    for gamenum in range(maxgamenum):
        contents = requests.get(f"{url}/bandit{gamenum}.html", stream=True)
        all_lines = contents.iter_lines()

        # Read until level title
        while True:
            line = next(all_lines)
            print(line, title, line == title)
            if line == title:
                break

        # Skip some lines
        next(all_lines)

        # # Read until level header
        # _, _, post = code.text.partition(title)
        # print(post)

        # # Get all the information
        # titlepattern = '<h2 id="level-goal">(.*?)</h2>'
        # titletext = re.search(titlepattern, post).group(1)
        # print(titletext)

        # goalpattern = '<p>(.*?)</p>'
        # goaltext = re.search(goalpattern, post).group(1)
        # print(goaltext)
        break


# def crawl():
#     requests


if __name__ == '__main__':
    crawl_bandit()
