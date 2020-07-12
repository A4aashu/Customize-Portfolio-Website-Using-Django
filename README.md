# -A4aashu-Portfolio-website-completely-dynamic-using-django-
Anyone can create own portfolio website

Install Python and Django

1.Clone This Project git clone  https://github.com/A4aashu/-A4aashu-Portfolio-website-completely-dynamic-using-django-.git

2.Go to Project Directory

3.Open Gitbash in same folder,create virtualenv(virtualenv -p python env) and activate that using(.env/Scripts/activate)

4.Now deploy your project on heroku 

5.Open same folder and Enter these commands in cmd-:
heroku login(LOGIN IN BROWSER SIGNUP IF YOU DONT HAVE ACCOUNT)
heroku create (TO CREATE HEROKU APP)
git init
git remote -v
git remote add heroku <url provided by heroku create command>
creating heroku -postgresql:hobby-dev(CREATING DATABASE IN HEROKU)
git add .(ADD)
git commit -m "The first commit"(COMMIT)
git push heroku master(PUSH TO HEROKU)
heroku run python manage.py migrate(TO MIGRATE DATABASE)
heroku run python manage.py createsuperuser(FOR CREATING ADMIN ACCOUNT)



If you found some issue to setup then feel free to contact me on my mail:kdsastm@gmail.com OR you can contact me on my website.
live at-:https://immense-sierra-83684.herokuapp.com/
