# -*- coding: utf-8 -*-
import os
import requests

from multiprocessing import Pool


def write_to_file(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)


def read_bandit_page(levelnum):
    """Read a single bandit page."""
    # Open the right output file in the right directory
    if not os.path.isdir('./bandit/tasks'):
        os.mkdir('./bandit/tasks')

    filename = f'./bandit/tasks/bandit{levelnum}.md'
    f = open(filename, 'w')
    f.write('<html>\n')

    # Fetch url contents
    url = "https://overthewire.org/wargames/bandit/"
    response = requests.get(f"{url}/bandit{levelnum}.html", stream=True)
    content = response.iter_lines()

    # Read until level title
    title = f'<script>renderLevelTitle("bandit", {levelnum});</script>'.encode()
    while True:
        line = next(content)
        if line == title:
            break

    f.write(f'<h1>Bandit {levelnum}</h1>\n')

    # Read task description
    while True:
        line = next(content)
        f.write(line.decode("utf-8") + '\n')
        if line.decode("utf-8").endswith('</p>'):
            break

    # Read helpful commands and material until end of info
    while True:
        line = next(content)
        if line == b'</div>':
            break
        f.write(line.decode("utf-8") + '\n')

    # Pull the solution on print to the same file as well
    if levelnum > 0:
        f.write('<h1>Solution</h1>\n\n')
        if os.path.isfile(f'./bandit/solutions/bandit{levelnum}.md'):
            with open(f'./bandit/solutions/bandit{levelnum}.md') as g:
                f.write(g.read() + '\n')  # Copy all contents into the new file

    # Write previous and next level to the bottom of the page
    if levelnum > 0:
        f.write(f'<a href="bandit/tasks/bandit{levelnum - 1}.md">Level {levelnum - 1}</a>\n')
    f.write(f'<a href="bandit/tasks/bandit{levelnum + 1}.md">Level {levelnum + 1}</a>\n')

    # End the file and close it
    f.write('</html>\n')
    f.close()
    return


def crawl_bandit():
    maxlevel = 34
    with Pool() as pool:
        pool.map(read_bandit_page, (i for i in range(maxlevel + 1)))


if __name__ == '__main__':
    crawl_bandit()
