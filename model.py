import web, datetime

#db = web.database(host="us-cdbr-iron-east-04.cleardb.net", dbn='mysql', db='heroku_1badb4b9ac7e6f9', user='b9d8d242aa29ad', pw='a96424d8')

db = web.database(dbn='mysql', db='estrenos', user='root', pw='mikei')

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
