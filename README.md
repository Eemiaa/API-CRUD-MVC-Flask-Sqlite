# API-CRUD-MVC-Flask-Sqlite

<img height="200em" style="border-radius:50px;" align="right" src="https://remimercier.com/media/2017/what-is-an-api-remi-mercier.gif" >

> Status: Develooping ⏳</br>

### What's it?

It is an MVC API developed in Python, using the Flask framework, SqlAlchemy (SQL object-relational mapping library) and the Sqlite database. The API performs basic Create, Read, Update, and Remove (CRUD) functions.

</br></br>
<hr>

## How to use this api?

### Environment preparation

I suggest that you create your own [virtual environment](https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv) for the project.

After activating the environment, run [requirements.txt](https://medium.com/pyladiesbh/requirements-em-python-ec88b42058a6) to install the dependencies, as follows:
```sh
$ pip install -r requirements.txt
```
### Run the API

In the terminal and with virtualenv activated, run the following command:
```sh
$ FLASK_APP=run.py flask run
```
Or same:
```sh
$ python3 run.py
```
Thus, you will receive in the terminal the address where the API is running and its status.

### Test the API

Here I am using Postman to test the requests. The collection file is the **CRUC-MVC-Flask-Sqlite.postman_collections.json**, have fun!
