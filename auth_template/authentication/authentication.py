# coding=utf-8
import os
import secrets
import boto3

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class user_data_c:
    def __init__(self,email):
        s3 = boto3.resource('s3')
        self.s3_object = s3.Object('wkbvitamova','users/userdata/'+email+'.json')
    def get(self):
        return json.load(self.s3_object.get()['Body'])
    def put(self,data):
        return self.s3_object.put(Body=json.dumps(data).encode("utf-8"))
    def delete(self):
        return self.s3_object.delete()
        
def code():
    
    return json.dumps(return_code)

def userpass_get():
    s3 = boto3.resource('s3')
    object = s3.Object('wkbvitamova','users/userpass.json')
    return json.load(object.get()['Body'])
    
def userpass_put(data):
    s3 = boto3.resource('s3')
    object = s3.Object('wkbvitamova','users/userpass.json')
    return object.put(Body=json.dumps(data).encode("utf-8"))

def logged_in_header():
    with open(os.path.join(BASE_DIR,"templates/sub_templates/logged_in_header.html"),"r") as f:
        return f.read()

def not_logged_in_header():
    with open(os.path.join(BASE_DIR,"templates/sub_templates/not_logged_in_header.html"),"r") as f:
        return f.read()

def check_login(request):
    if request.method == "GET":
        return False
    if "email" not in request.POST:
        return False
    
    login_email = request.POST["email"]
    login_token = request.POST["login_token"]
    if login_email != "" and login_token != "":
        s3 = boto3.resource('s3')
        object = s3.Object('wkbvitamova','users/userpass.json')
        userpass = json.load(object.get()['Body'])
    else:
        return 1
    if login_email in userpass:
        user_info = userpass[login_email]
    else:
        return 2
    if user_info["token"] == login_token:
        return 0
    else:
        return 1
        
def handle_not_logged_in(request):
    return 0
        
def home(request):
    return HttpResponseRedirect("/dashboard")

def login(request):
    if request.method == "GET":
        return render(request,'authenticator.html',{"url":"/login/"})
    else:
        logged_in = check_login(request)
        if logged_in == 0:
            return HttpResponseRedirect('/dashboard')
        else:
            if "logging_in" not in request.POST:
                return(render(request,'login.html',{"header":not_logged_in_header()}))
            else:
                email = request.POST["email"]
                userpass = userpass_get()
                if email not in userpass:
                    return render(request,'login.html',{"header":not_logged_in_header()})
                else:
                    password = request.POST["password"]
                    login_token = request.POST["login_token"]
                    pass_b = bytes(password,encoding="utf-8")
                    pash_hash = hashlib.sha256(pass_b).hexdigest()
                    if userpass[email]["password"] == pash_hash:
                        userpass[email]["token"] = login_token
                        userpass_put(userpass)
                        return HttpResponseRedirect('/dashboard')
                    else:
                        return render(request,'login.html',{"header":not_logged_in_header()})

def delete_account(request):
    check_login(request)
    
            
def logout(request):
    return render(request,'logout.html',{}) 

def signup(request):
    if request.method == "GET":
        return render(request,'signup.html',{"header":not_logged_in_header()})
    else:
        login_email = request.POST["email"]
        password = request.POST["password"]
        pass_b = bytes(password,encoding="utf-8")
        pass_hash = hashlib.sha256(pass_b).hexdigest()
        userpass = userpass_get()
        if login_email not in userpass:
            userpass.update({login_email:{"password":pass_hash,"token":""}})
            userpass_put(userpass);
            user_data = {
                "transcribe": {"level": "0"},
                "read": {"articles": 0},
                "typing": {"level": "0"},
                "start_date":str(datetime.date.today()),
                "history":[0],"points":0
            }
            user_data_c(login_email).put(user_data)
            return HttpResponseRedirect('/login')
        else:
            return render(request,'signup.html',{"header":not_logged_in_header()})
        