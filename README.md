# LangCite
 
This is a Django project meant to be used for a language translation education service. It uses Django, Bootstrap, Apache, and various other technologies. This was created as a project for Ivy Tech Community College's SDEV 265 class in Spring 2021. This was developed by Craig Carson, Corey Teeter, Jeffery Patton, and Josh Chapman.

## How to install
First you should install a Linux distro of your choice. We used Ubuntu 20.04 and Debian 10 (Jeffery, the author of this README, transitioned to the latter the night this README was made) to deploy this project, and thus those two are what the instructions were provided for. It should be possible on any other distribution though, with some hard work and research.

Here are then the instructions on how to deploy on Debian/Ubuntu, instructions are based off of https://www.youtube.com/watch?v=Sa_kQheCnds from some guy named  Corey Schafer.

1. Update to the newest version of the distro with `sudo apt update`.
2. Install the following packages: `sudo apt install python3-pip python3-venv git libapache2-mod-wsgi-py3 apache2 sqlite3`
3. Clone the git repo into your home folder and cd into its app folder: `git clone https://github.com/ccarson1/LangCite.git && cd LangCite/app`
4. Edit settings.py in the app folder within the app folder to your liking and in particular change the allowed host IP address and langImport absolute directory, which are at lines 29 and 60: `vi or nano app/settings.py`
5. Create the venv in the first app directory and activate it for the shell session: `python3 -m venv venv && source venv/bin/activate`
6. Install the wheel Python pip package required by other packages, YOU MUST DO THIS FIRST BEFORE INSTALLING THE REST: `pip3 install wheel`
7. Then install the rest of the needed pip packages: `pip3 install appdirs django google-trans-new jsonfield Pillow pdf2image PyDictionary PyPDF2 translate wheel youtube-transcript-api image pytesseract'
8. Then collect the static Django files: `python manage.py collectstatic`
9. Then go to `/etc/apache2/sites-available` and create a django_debian.conf file, copying and pasting or downloading the code from https://github.com/CoreyMSchafer/code_snippets/blob/master/Django_Blog/snippets/django_project.conf: `cd /etc/apache2/sites-available && sudo nano django_debian.conf` or `cd /etc/apache2/sites-available && sudo wget https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Django_Blog/snippets/django_project.conf && mv django_project.conf django_debian.conf`
10. Continuing on that same file, replace all the place holder path information with your specific information of where LangCite is and called. Note that the proper Django project folder is actually at "app," not at "LangCite."
11. Then enable the Django project and disable the default Apache webpage: `sudo a2ensite django_debian && sudo a2dissite 000-default`
12. Then return with `cd` back to LangCite and set the permissions for Apache to handle the project: `sudo chmod -R 775 app && sudo chown -R :www-data app && sudo chmod 664 app/db.sqlite3`
13. Then restart the Apache daemon: `sudo systemctl restart apache2.service`

### And there you go, you have set up LangCite and it should work now! :D

## How to update though?

Ummm, well, here's the steps:
1. `git pull` You need to pull first if you need to stash or not
2. `git stash`If you see conflicts and it tells you to stash or add/commit changes, then stash
3. `git pull` Then pull for real
4. `git stash pop` then pop the stashed changes back to repo
5. `git reset HEAD .` then reset the status of git repo so that there aren't any weird stuff like in progress commits and then you can git pull again in the future.
