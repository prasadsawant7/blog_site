import pyodbc
import datetime
import random
import hashlib

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

firstName = "Andre"
lastName = "Gomes"
email = "andre.gomes@gmail.com"
username = "andre7"
passwd = "andre$123"
bio = "Hello I am Andre, Front End Developer"
country = "Portugal"

def saltGenerator(stringLength=15):
        salt_characters = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        return ''.join(random.choice(salt_characters) for i in range(stringLength))

salt = saltGenerator()

saltedPasswd = passwd + salt

passwdHash = hashlib.sha256(saltedPasswd.encode('utf-8')).hexdigest()

registered_at = str(datetime.datetime.now())[:19+4]
last_login = str(datetime.datetime.now())[:19+4]

sql = f"""insert into bs_user(
firstName,
lastName,
email,
username,
salt,
passwdHash,
registered_at,
last_login,
bio,
country
) 
values
(
'{firstName}',
'{lastName}',
'{email}',
'{username}',
'{salt}',
'{passwdHash}',
'{registered_at}',
'{last_login}',
'{bio}',
'{country}'
);"""

cur.execute(sql)

conn.commit()
conn.close()
