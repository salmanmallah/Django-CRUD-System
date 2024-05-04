from django.shortcuts import render, redirect
from django.contrib import messages
from setup.models import user_login
from sys import exc_info

# Create your views here.
def index(request):
    # getting data from form
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if (name == "") or (email == "") or (username == "") or (password == ""):
            messages.warning(request, 'All fields are required*')
        else:
            data = user_login.objects.create(name=name, email=email, username=username, password=password)
            data.save()
            messages.success(request, f'User : {name} is Added Successfully')

    # fetching all rows from database table (user_long)
    row = user_login.objects.all()
    user_data = {
        'user_data': row
    }
    return render(request, 'index.html', user_data)


# function to delete row
def delete(request, user_id):
    try:
        row = user_login.objects.get(id=user_id)
        row.delete()
        messages.warning(request, f'User : {row.name} is Deleted Successfully')
    except:
        print(f'{exc_info()[1]}')
    return redirect("/")  # / means redirect the user to home page


# function to update data
def update(request, user_id):
    # fetching all data
    all_row = user_login.objects.all()

    # fetching row by user id
    row = user_login.objects.get(id=user_id)
    user = {
        'user': row,
        'user_data': all_row,
        'text': True
    }


    # updating data
    if request.method == 'POST':
        # getting form data
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        # updating data
        if (name == '') or (email == '') or (username == '') or (password == ''):
            messages.warning(request, 'All Fields are required**')
        else:
            row.name = name
            row.email = email
            row.username = username
            row.password = password
            # saving data
            row.save()
            messages.success(request, 'Row updated successfully')
            return redirect('/index.html/')

    return render(request, 'update.html/', user)