from import_utils import *


# Github access token
github_access_token = os.environ.get('GITHUB_ACCESS_TOKEN')
# Docker Hub credentials
docker_username = os.environ.get('DOCKER_USERNAME')
docker_password = os.environ.get('DOCKER_PASSWORD')
# Github repository information
github_repo_owner = 'KartikeyaReddy24'
github_repo_name = 'ExtractingEmailsOnK8s'
# Docker image information
docker_image_name = 'kartikeya24/eek8s'
docker_image_tag = 'latest'