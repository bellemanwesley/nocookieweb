import sys
import shutil

if sys.argv[1] == "-t":
    print("Success")
    
if sys.argv[1] == "--create":
    project_name = sys.argv[2]
    shutil.copytree(pwd,"/home/"+username+"/"+project_name)
    shutil.move("/home/"+username+"/"+project_name+"/auth_template","/home/"+username+"/"+project_name+"/"+project_name)
    with open("/home/"+username+"/"+project_name+"/"+project_name+"/settings.py","r") as f:
        my_file_text = f.read()
    my_file_text = my_file_text.replace("auth_template",project_name)
    with open("/home/"+username+"/"+project_name+"/"+project_name+"/settings.py","w") as f:
        f.write(my_file_text)
    with open("/home/"+username+"/"+project_name+"/"+project_name+"/wsgi.py","r") as f:
        my_file_text = f.read()
    my_file_text = my_file_text.replace("auth_template",project_name)
    with open("/home/"+username+"/"+project_name+"/"+project_name+"/wsgi.py","w") as f:
        f.write(my_file_text)
    with open("/home/"+username+"/"+project_name+"/manage.py","r") as f:
        my_file_text = f.read()
    my_file_text = my_file_text.replace("auth_template",project_name)
    with open("/home/"+username+"/"+project_name+"/manage.py","w") as f:
        f.write(my_file_text)