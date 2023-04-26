from import_utils import *
from variables import *


def listen_to_github_events():
    # Initialize Github API client
    github = Github(github_access_token)
    repo = github.get_repo(f'{github_repo_owner}/{github_repo_name}')

    # Clone the Github repository
    repo_path = f'/tmp/{github_repo_name}'
    if not os.path.exists(repo_path):
        os.system(f'git clone https://github.com/{github_repo_owner}/{github_repo_name}.git {repo_path}')

    # Initialize Docker client
    docker_client = docker.from_env()

    # Listen to Github repository events
    for event in repo.get_events():
        # Check if event is a push event
        if event.type == 'PushEvent':
            # Build the Docker image
            docker_image, build_logs = docker_client.images.build(path=repo_path, tag=f'{docker_image_name}:{docker_image_tag}')

            # Login to Docker Hub
            docker_client.login(username=docker_username, password=docker_password)

            # Push the Docker image to Docker Hub
            docker_client.images.push(repository=docker_image_name, tag=docker_image_tag)

    # Wait for 15 minutes before checking for new events
    time.sleep(900)
