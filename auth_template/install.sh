sudo cp authentication/django-auth.py /usr/bin/django-auth;
python_loc=$(which python3);
shebang="#!${python_loc}";
userassign="username = '${USER}'";
pwd=$(pwd);
pwdassign="pwd = '${pwd}'"
sudo echo $pwdassign |cat - /usr/bin/django-auth > /tmp/out;
sudo mv /tmp/out /usr/bin/django-auth;
sudo echo $userassign |cat - /usr/bin/django-auth > /tmp/out;
sudo mv /tmp/out /usr/bin/django-auth;
sudo echo $shebang |cat - /usr/bin/django-auth > /tmp/out;
sudo mv /tmp/out /usr/bin/django-auth;
sudo chmod 777 /usr/bin/django-auth;
echo "test installation with command: django-auth -t";