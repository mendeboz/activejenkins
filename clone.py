#!/usr/bin/env python3

# Import modules
import requests
import git
import os

# Define variables
username = "your_bitbucket_username" # Change this to your Bitbucket username
password = "your_bitbucket_password" # Change this to your Bitbucket password
team = "your_bitbucket_team" # Change this to your Bitbucket team or user
clone_dir = "your_clone_directory" # Change this to your desired directory to clone the repositories

# Create a session object with authentication
session = requests.Session()
session.auth = (username, password)

# Get the list of repositories from the Bitbucket API
url = f"https://api.bitbucket.org/2.0/repositories/{team}"
response = session.get(url)
data = response.json()

# Loop through the repositories and clone them
for repo in data["values"]:
    repo_name = repo["name"]
    repo_url = repo["links"]["clone"][0]["href"]
    print(f"Cloning {repo_name} from {repo_url}")
    git.Repo.clone_from(repo_url, os.path.join(clone_dir, repo_name))
    print(f"Done cloning {repo_name}")

# Close the session
session.close()