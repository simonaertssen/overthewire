import os
import re
import requests


def write_to_file(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)


def read_bandit_page(levelnum):
    """Read a single bandit page."""
    # Open the right output file in the right directory
    if not os.path.isdir('./bandit'):
        os.mkdir('./bandit')

    filename = f'./bandit/bandit{levelnum}.html'
    f = open(filename, 'w')
    f.write('<html>\n')

    # Fetch url contents
    url = "https://overthewire.org/wargames/bandit/"
    response = requests.get(f"{url}/bandit{levelnum}.html", stream=True)
    content = response.iter_lines()

    # Read until level title
    title = b'<script>renderLevelTitle("bandit", 0);</script>'
    while True:
        line = next(content)
        if line == title:
            break

    # Read html until last interesting piece of data
    lookfor = b'<h2 id="helpful-reading-material">Helpful Reading Material</h2>'
    while True:
        line = next(content)
        if not line:
            continue
        if line == lookfor:
            break
        f.write(line.decode("utf-8") + '\n')

    lookfor = b'</ul>'
    while True:
        line = next(content)
        if not line:
            continue
        if line == lookfor:
            break
        f.write(line.decode("utf-8") + '\n')

    # Get last line
    f.write(line.decode("utf-8") + '\n')

    # End the file and close it
    f.write('</html>')
    f.close()
    return 0


def crawl_bandit():
    maxlevel = 34
    for level in range(maxlevel):
        read_bandit_page(level)
        break


if __name__ == '__main__':
    crawl_bandit()
