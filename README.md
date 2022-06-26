### An Online Tutorial Platform API

##### How to Run

``` sh
# create and setup a virtual environment
$ python3 -m venv DPhi
# Move Into the folder
$ cd DPhi/
# activate the environment
$ source bin/activate
# clone the project
$ git clone git@github.com:adewolejosh/DPhi.git
# move into dir
$ cd DPhi/
# install all dependencies
$ pip install -r requirements.txt
# You're done with the installation!

# make migrations
> python manage.py makemigrations accounts
> python manage.py makemigrations courses
# migrate
> python manage.py migrate
# run server
> python manage.py runserver
```

##### Endpoints

<details>
    <summary> - POST: 'accounts/new/'  create new user</summary>
    
    fields required are unique username, password, 
    category( E for educators, NE for Non-Educators )
    unique email

</details>

<details>
    <summary> - POST: 'accounts/api-token-auth/' login user/</summary>
    
    get user token that would be used in every endpoint
    how to use:
    in your headers add; "Authorization: Token {token}

</details>

<details>
    <summary> - POST 'courses/new/' make a new course as an educator</summary>

    fields include name, image, description    

</details>

<details>
    <summary> - GET: 'courses/list/' get a list of all courses</summary>

</details>

<details>
    <summary> - GET: 'courses/list/:id/' get details on a course </summary>

</details>

<details>
    <summary> - POST: 'courses/enrol/new/:id/ enrol into a new course as
    a Non-Educator </summary>

</details>

<details>
    <summary> - GET: 'courses/enrol/view/:id/' get users who enrolled into your
    course as an owner/educator</summary>

</details>

