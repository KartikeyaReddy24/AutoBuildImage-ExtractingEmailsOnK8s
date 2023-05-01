from import_utils import *
from variables import *


def listen_to_github_events():
    # Initialize Github API client
    github = Github(github_access_token)
    repo = github.get_repo(f'{github_repo_owner}/{github_repo_name}')

    # Clone the Github repository
    repo_path = f'/tmp/{github_repo_name}'
    if not os.path.exists(repo_path):
        git.Repo.clone_from(f'https://github.com/{github_repo_owner}/{github_repo_name}.git', repo_path)

    # Listen to Github repository events
    while True:
        for event in repo.get_events():
            # Check if event is a push event
            if event.type == 'PushEvent':
                # Build the Docker image
                build_command = f'docker build -t {docker_image_name}:{docker_image_tag} {repo_path}'
                build_result = subprocess.run(build_command, shell=True, check=True)

                # Push the Docker image to Docker Hub
                login_command = f'docker login -u {docker_username} -p {docker_password}'
                login_result = subprocess.run(login_command, shell=True, check=True)

                push_command = f'docker push {docker_image_name}:{docker_image_tag}'
                push_result = subprocess.run(push_command, shell=True, check=True)

        # Wait for 15 minutes before checking for new events
        time.sleep(900)
