from django import forms
from django.http import HttpResponse
from django.shortcuts import render,redirect
from matplotlib.style import context
from pendulum import instance

from libmanagement.models import Books,Author,Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

# Register Form

class UserRegistration(forms.Form):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="email",error_messages={'required': 'Please enter your email'})
    pass1 = forms.CharField(max_length=32, widget=forms.PasswordInput,label="password")
    pass2 = forms.CharField(max_length=32, widget=forms.PasswordInput,label = "confirm your password")
    #day = forms.DateField(initial=datetime.date.today)
fm = UserRegistration()



# Create your views here.
def index(request):
    books = Books.objects.all()
    context = {
        'books': books
    }
    return render(request,"libmanagement/index.html",context)

def signup(request):
    return render(request,"libmanagement/signup.html")





def signup(request):
    fm = UserRegistration()
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username =  username):
            messages.error(request,"Username already exists")
            return redirect('/signin')
        
        if User.objects.filter(email = email).exists():
            messages.error(request,"email already Registered")
            return redirect('/signin')
            
        if len(username)>20:
            messages.error(request,"username should be lower than 20 chracter")
            return redirect('/signin')
            
        if pass1 != pass2:
            messages.error(request,"passwords didnt match")
        myuser = User.objects.create_user(username,email,pass1)
        myuser.is_active = True
        myuser.save()
        messages.success(request,"congrats for successfully Registration")
        return redirect('/signin')
    
    return render(request,"libmanagement/signup.html",{
        "fm":fm
    })
    
    
    
def signin(request):
    
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            
            return redirect("/actions")

        else:
            # No backend authenticated the credentials
            # messages.error(request,"seems like your account doesnt exist")
            return HttpResponse("your account doesnt exist!! please signup")
            # return redirect("/signup")
            
            

    return render(request, 'libmanagement/signin.html',{
        "fm":fm
    })

def addingbooks(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        author_name = request.POST['author_name']
        ISBN = request.POST['ISBN']
        quantity = request.POST['quantity']
        category = request.POST['category']
        location = request.POST['location']
        new_book = Books(book_name = book_name, author_name_id = author_name, ISBN = ISBN, quantity = quantity, category_id = category)
        new_book.save()
    #elif request.method=='GET':
    #    return render(request, 'addingbooks.html')
    #else:
    #    return HttpResponse("An Exception Occured! Employee Has Not Been Added")
        #return HttpResponse("A new book added successfully")
        
        
    return render(request,"libmanagement/addingbooks.html")

def actions(request):
    return render(request,"libmanagement/actions.html")


def deletingbook(request,book_id = 0):
    if book_id:
        try:
            book_removed=Books.objects.filter(id = book_id)
            book_removed.delete()
        except:
            return HttpResponse("Please Enter A Valid Book ID")
    books = Books.objects.all()
    context = {
        'books': books
    }
            
    return render(request,"libmanagement/deletingbook.html",context)


def searchbook(request):
    if request.method == 'POST':
        name = request.POST['name']
        #aname = request.POST['aname'] 
        code  = request.POST['code'] 
        books = Books.objects.all()
        if name:
            books = books.filter(book_name__icontains = name)
        # if aname :
        #     books.filter(author__name__icontains = aname)
        if code :
            books = books.filter(ISBN__name__icontains = code)
            
        context = {
            'books':books
        }    
        return render(request,"libmanagement/index.html",context)
            
    elif request.method == 'GET':
        return render(request, 'libmanagement/searchbook.html')
    else:
        return HttpResponse('An Exception Occurred')    
    # return render(request,"libmanagement/searchbook.html")
    
def updatebook(request):
    books = Books.objects.all()
    context = {
        'books': books
    }
    return render(request,"libmanagement/updatebook.html",context)
    # if request.method == 'POST':
    #     books = Books.objects.get(pk = id)
    #     fm = Books(request.POST,instance= books)
    #     fm.save()
    # else:
    #     books = Books.objects.get(pk = id)
    #     fm = Books(request.POST,instance= books)
        
        
    # return render(request,"libmanagement/updatebook.html",{
    #     'id':id
    # })
    
def updateaction(request,book_id):
    books = Books.objects.get(id = book_id)
    
    context= {
        "books":books
    }
  
  
    return render(request,"libmanagement/updateaction.html",context)
    
def updatebutton(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        author_name = request.POST['author_name']
        ISBN = request.POST['ISBN']
        quantity = request.POST['quantity']
        category = request.POST['category']
        location = request.POST['location']
        
    return render(request,"libmanagement/updatebook.html")