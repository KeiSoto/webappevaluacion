import web, datetime

db = web.database(host="us-cdbr-iron-east-04.cleardb.net", dbn='mysql', db='heroku_15d60b6521417a0', user='b2adee8445e8b1', pw='bcc5c26d')

def get_posts():
    return db.select('peliculas')

def get_users():
    return db.select('users')

def get_post(id):
    try:
        return db.select('peliculas', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_post(title, original, genero, nac, year, director, guion, fecha):
    db.insert('peliculas', titulo=title, titulo_original=original, genero=genero,
             nacionalidad=nac, anio=year, director=director,
             guion=guion, fecha_estreno=fecha)

def del_post(id):
    db.delete('peliculas', where="id=$id", vars=locals())

def update_post(id, title, original, genero, nac, year, director, guion, fecha):
    db.update('peliculas', where="id=$id", vars=locals(),
        titulo=title, titulo_original=original, genero=genero,
             nacionalidad=nac, anio=year, director=director,
             guion=guion, fecha_estreno=fecha)
