import os
import subprocess

# Configuration
GIT_REPO_URL = "https://github.com/jamstanleyambe/Math-Expression-Parser.git"
DOCKER_IMAGE_NAME = "jamsapp"
CONTAINER_NAME = "jam"
ENV_VARIABLES = {"PORT": "8080"}  


subprocess.run(["git", "clone", GIT_REPO_URL], check=True)

os.chdir("jamapp") 

subprocess.run(["docker", "build", "-t", DOCKER_IMAGE_NAME, "."], check=True)

env_vars = sum([["-e", f"{key}={value}"] for key, value in ENV_VARIABLES.items()], [])
subprocess.run(["docker", "run", "-d", "-p", "8080:80", "--name", CONTAINER_NAME] + env_vars + [DOCKER_IMAGE_NAME], check=True)

print("Deployment completed successfully.")

