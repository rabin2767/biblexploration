# BIBLExploration.com

This section is to load the data to your MySQL DB.

## PREREQUISITE
Install MySQL
Python 3.7 above


### Create Virtual Env
```bash
virtualenv env_<ANY-NAME>
```

### Activate Virtual Env
```bash
.\<PATH To your env_<ANY-NAME>>\Scripts\activate
```

### Deactivate Env
```bash
deactivate
```


### TO RUN
Activate your virtual environment and install the below
```bash
pip install mysql-connector-python-rf
pip install requests
```

Before running data to db, edit dbConnect.py with appropriate details, EDIT everything with <>

```bash
python .<GOTO WHERE YOU CLONED>\InitialSetup-DbSetup\loadBooks.py
```

