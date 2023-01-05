# api req to github

import requests

response = requests.get("https://api.github.com/users/bobbyy16/repos")

myProjects = response.json()

for project in myProjects:
    print(f"Project Name: {project['name']}\n Project Url: {project['html_url']}\n")