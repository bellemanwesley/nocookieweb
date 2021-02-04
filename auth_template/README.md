# Authentication Template
This project builds django projects with pre-installed authentication tools. This project is a go-to starting point for your website that requires user authentication.

## Install django-auth
#### First clone the repository:
git clone https://github.com/bellemanwesley/security.git

#### Move into the django_auth directory
cd security/auth_template

#### Run the shell script
sh install.sh

#### Test the install
django-auth -t

## Create a new django project
django-auth --create [projectname]

## Update an existing project
django-auth --update [/absolute/project/directory]

# Limitations
Right now this project only supports new projects or updates to projects that were created with this tool. The tool does not retrofit old projects that were not created with this tool.
