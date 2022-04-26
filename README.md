# vtm_site
Clone this repository to local computer

Rename the directory to reflect the new project name

Delete .git folder

Create a new virtual environment

Windows: python -m venv ./venv
Mac: python3 -m venv ./venv
Activate the new virtual environment

Windows: .\venv\Scripts\activate
Mac: source ./venv/bin/activate
Install the dependencies pip install -r requirements.txt

Make a new repository by running git init in the folder.

Track all the files in the new local repository git add .

Make the first commit of this new project git commit -m 'first commit of <project name> from flask_template

On Github, create a new repository. DO NOT initialize it

Connect the local repository to the new Github repository git remote add origin <<repository_URL>>

Create and change to a new local development branch git checkout b development

Continue working with the project as you normally would.
  
install pytest: pip3 install pytest
install pytest-cov: pip3 install pytest-cov!
statrt test: python -m pytest
coverage for all file: python -m pytest --cov
