from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .models import Employee, AuthorizationCode
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
data_modified = False
initial_salary = 250.

def home(request):
    template = loader.get_template('index.html')
    context = {}
    global initial_salary
    if len(list(Employee.objects.all())) == 0:
        #first name, last name
        variables = [['blue lizzard','Manuel','Gonzalez','manugonza@gmail.com','employee','sales',500.,'s3cur3P@ssw0rd_']
                    ,['green aligator','Roberto','Romero','roberrome@gmail.com','employee','develop',500.,'s3cur3P@ssw0rd_1']
                    ,['red monkey','Rodrigo','Martinez','rodrimartin@gmail.com','admin','develop',500.,'4dm1n_p@SSw0rd__']
                    ,['purple octopus','Manuel','Perez','manupere@gmail.com','employee','sales',500.,'s3cur3P@ssw0rd_2']
                    ,['white dog','Lucia','Blanco','luciblan@gmail.com','employee','sales',500.,'s3cur3P@ssw0rd_3']
                    ,['black cat','Manolo','Carrasco','manocarras@gmail.com','employee','sales',500.,'s3cur3P@ssw0rd_4']
                    ,['yellow bird','Martin','Jimenez','marjime@gmail.com','employee','develop',500.,'s3cur3P@ssw0rd_5']
                    ,['brown cow','Pedro','Gamito','pedgami@gmail.com','employee','develop',500.,'s3cur3P@ssw0rd_6']
                    ,['grey horse','Susana','Martin','susamar@gmail.com','employee','sales',500.,'s3cur3P@ssw0rd_7']
                    ,['tomcat','Tom','Cat','tomcat@gmail.com','employee','develop',initial_salary,'tomcat']]
        for i in range(0,len(variables)):
            employee = Employee()
            employee.username = variables[i][0]
            employee.first_name = variables[i][1]
            employee.last_name = variables[i][2]
            employee.email = variables[i][3]
            employee.role = variables[i][4]
            employee.business_department = variables[i][5]
            employee.salary = variables[i][6]
            employee.set_password(variables[i][7])
            employee.save()
        code = AuthorizationCode()
        code.flag = 'CTF-SQ1-Inj3cti0n-Bypass-Update-Blind'
        code.save()
    return HttpResponse(template.render(context,request))

def login_bypass(request):
    context= {}
    template = loader.get_template('login.html')
    if request.method == 'POST':
        username = request.POST.get('name',)
        password = request.POST.get('password',)
        result = Employee.objects.raw("SELECT * FROM authentication_employee WHERE username = '%s' AND password = '%s'" % (username, password))
        user = result[0]
        if user is not None:
            login(request,user)
            return redirect('/profile')
    else:
        user = request.user
        if user.is_authenticated:
            return redirect('/profile')
    return HttpResponse(template.render(context,request))

@login_required
def my_profile(request):
    template = loader.get_template('profile.html')
    user = request.user
    context = {'name':user.first_name + user.last_name,'role':user.role,'department':user.business_department}
    return HttpResponse(template.render(context,request))
    
@login_required
@user_passes_test(lambda x : x.role == 'admin')
def get_employees(request):
    global data_modified, initial_salary
    context = {}
    template = loader.get_template('list_employees.html')
    name = request.GET.get('name')
    result = Employee.objects.raw("SELECT * FROM authentication_employee WHERE first_name = '%s'" % (name))
    target = Employee.objects.get(username="tomcat")
    if target.salary > initial_salary:
        data_modified = True
    context['data_modified'] = data_modified
    context['query'] = result
    return HttpResponse(template.render(context,request))


@login_required
@user_passes_test(lambda x : x.role == 'admin')
def authorize_change_data(request):
    global data_modified, initial_salary
    template = loader.get_template('authorize.html')
    context = {'flag':False, 'method':request.method}
    if request.method == 'POST':
        code = request.POST.get('code')
        query = AuthorizationCode.objects.raw("SELECT * FROM authentication_authorizationcode WHERE flag  = '%s'" %(code))
        flag = None
        if len(query) > 0:
            flag = query[0] 
        if flag is not None:
            context['flag'] = True
        if flag is not None and flag.flag == code:
            target = Employee.objects.get(username="tomcat")
            initial_salary = target.salary
            data_modified = False
    context['ctf'] = AuthorizationCode.objects.first().flag        
    context['data_modified'] = data_modified
    return HttpResponse(template.render(context,request))