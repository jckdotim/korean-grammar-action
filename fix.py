import os
import json
import html

import requests
from github import Github
from whatthepatch import parse_patch


def fix(original):
    response = requests.get(
        'https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy',
        params=dict(q=original, color_blindness=0)
    )
    return html.unescape(response.json()['message']['result']['notag_html'])

with open(os.environ.get('GITHUB_EVENT_PATH')) as gh_event:
    json_data = json.load(gh_event)
    g = Github(os.environ.get('GITHUB_TOKEN'))
    pr = g.get_repo(
        json_data['pull_request']['base']['repo']['full_name']
    ).get_pull(json_data['number'])
    for file in pr.get_files():
        for position, diff in enumerate(parse_patch(file.patch)):
            print(diff)
            for change in diff.changes:
                fixed = fix(change.line)
                if not change.old and fixed != change.line:
                    pr.create_comment(
                        f"""```suggestion\n{fixed}\n```""",
                        pr.get_commits()[0],
                        file.filename,
                        position
                    )
