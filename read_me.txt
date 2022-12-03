1. Register new user

path: http://127.0.0.1:5000/api/v1/auth/register

payload:
{
    "email":"testemail@gmail",
    "password":"password"
}

2. Login User

path: http://127.0.0.1:5000/api/v1/auth/login

payload:
{
    "email":"testemail1@gmail",
    "password":"pasfsword"
}

3. Logout user ( Not completed )

path: http://127.0.0.1:5000/api/v1/auth/logout

3.  Create a new post

path: http://127.0.0.1:5000/api/v1/posts

payload:
{
    "title": "Post 3 title",
    "description": "Post 3 description",
    "postUrl": "Post 3 postUrl"
}
4. Get all posts  ( not completed )
 
 path http://127.0.0.1:5000/api/v1/posts