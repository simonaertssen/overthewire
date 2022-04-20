# -*- coding: utf-8 -*-
import os
import requests
from itertools import repeat
from multiprocessing import Pool


def read_page(game, levelnum):
    """Read a single bandit page."""
    # Open the right output file in the right directory
    if not os.path.isdir(f'./{game}/tasks'):
        os.mkdir(f'./{game}/tasks')

    filename = f'./{game}/tasks/{levelnum}.md'
    f = open(filename, 'w')

    # Fetch url contents
    url = f"https://overthewire.org/wargames/{game}/"
    response = requests.get(f"{url}/{game}{levelnum}.html", stream=True)
    content = response.iter_lines()

    # Read until level title
    title = f'<script>renderLevelTitle("{game}", {levelnum});</script>'.encode()
    while True:
        line = next(content)
        if line == title:
            break

    f.write(f'<h1>{game.capitalize()} {levelnum}</h1>\n')

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
        if os.path.isfile(f'./{game}/solutions/{levelnum}.md'):
            with open(f'./{game}/solutions/{levelnum}.md') as g:
                f.write(g.read() + '\n')  # Copy all contents into the new file

    # Write previous and next level to the bottom of the page
    if levelnum > 0:
        # f.write(f'<a href="{game}{levelnum - 1}.md">Level {levelnum - 1}</a>\n')
        # f.write(f'[{game} level {levelnum - 1}]({game}/tasks/{levelnum - 1}.md)\n')
        f.write(f'[{game} level {levelnum - 1}]({levelnum - 1}.md)\n')

    # f.write(f'<a href="{game}{levelnum + 1}.md">Level {levelnum + 1}</a>\n')
    # f.write(f'[{game} level {levelnum + 1}]({game}/tasks/{levelnum + 1}.md)\n')
    f.write(f'[{game} level {levelnum - 1}]({levelnum + 1}.md)\n')

    # End the file and close it
    f.close()


def crawl(game, maxlevel):
    with Pool() as pool:
        pool.starmap(read_page, zip(repeat(game), (i for i in range(maxlevel + 1))))
