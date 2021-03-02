#!/usr/bin/env python3

import os
import re
import sys

from github import Github

DEFAULT_LABEL = 'change:standard'
valid_labels = set(['change:standard', 'change:impactful', 'change:emergency'])

repo_name = os.environ.get('GITHUB_REPOSITORY')
github_ref = os.environ.get('GITHUB_REF')

pr_number = int(re.search('refs/pull/([0-9]+)/merge', github_ref).group(1))

pr = Github(sys.argv[1]).get_repo(repo_name).get_pull(pr_number)

found_labels = set(map(lambda x: x.name, pr.get_labels()))

if (valid_labels & found_labels):
    print("Found labels on PR", found_labels)
    exit(0)
else:
    print("Missing required label from PR! Adding the default ones", valid_labels)
    pr.add_to_labels(self.DEFAULT_LABEL)
    exit(0)
