import os
os.chdir('C:/Users/bzmcc/Documents/PythonCrashCourse/Chapter17')

import requests

from plotly.graph_objs import Bar, Layout
from plotly import offline

# Make an API call and store the response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results
response_dict = r.json()
repo_links, stars, labels = [], [], []

print(f"Total repositories: {response_dict['total_count']}")

# Explore information about repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    
    stars.append(repo_dict['stargazers_count'])
    
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)
    
# Make visualization
data = [{'type': 'bar',
         'x': repo_links,
         'y': stars,
         'hovertext': labels}]

"""my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'xaxis': {'title', 'Repository'},
    'yaxis': {'title', 'Stars'}
    }"""

my_layout = Layout(title='Most-Starred Python Projects on GitHub')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')




