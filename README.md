# Blog
<ul>
    <li>After cloning this project</li>
    <li>Create a virtual environment within the parent folder
    of this project. you can give it a name such as <code>venv</code>.
    </li>
    <li>Run the following command in the parent directory of this project on your
    terminal. <code>pip install -r requirements.txt</code> to install 
    all the required libraries for this project into the virtual environment you created.</li>
    <li>Set up a postgres database for this project</li>
    <li>
    Run the following command in your terminal afterwards
    <code>python manage.py makemigrations</code> to create the database
    migrations in the postgres database you created.
    </li>
    <li>
    Run the following command in your terminal afterwards
    <code>python manage.py migrate</code> to create the database
    tables in the postgres database you created.
    </li>
    <li>
    Run the following command in your terminal afterwards
    <code>python manage.py runserver localhost:8000</code> to startup the web server.
    </li>
</ul>
