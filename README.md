To start the project: 
*for Windows
1. Select a folder you need to clone the project and get in -> empty space right mouse button -> Git Bash Here (Git must be installed)
2. Enter:
git clone https://github.com/ip-kovylin/IPNewsPortal
3. Open project in PyCharm then open its terminal
4. Make sure you're in IPNewsPortal folder (otherwise move there by 'cd C:\Users\...' command) and enter:  
python -m venv venv  
venv\scripts\activate  
pip install django  
cd IPNP  
python manage.py runserver  
5. Congrats, you started development server at http://127.0.0.1:8000/
6. To quit the server use CTRL+C in terminal


SUPERUSER is created, link: 
http://127.0.0.1:8000/admin/
Username: admin
Password: 0000
