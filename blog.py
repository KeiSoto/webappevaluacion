# -*- coding: utf-8 -*-
import web
import model
import csv
from web import form

data_list = []
data_list1 = []
categorias = ["Inmunizaciones","Detecciones"]
anios = ["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"]

### Url mappings

urls = (
    '/', 'Index',
    '/view/(\d+)', 'View',
    '/new', 'New',
    '/delete/(\d+)', 'Delete',
    '/edit/(\d+)', 'Edit',
    '/viewdata', 'Viewdata',
    '/login', 'Login',
)


### Templates
t_globals = {
    'datestr': web.datestr
}

render = web.template.render('templates', base='base', globals=t_globals)


with open("data/inmunizaciones.csv","r") as filename:
    data = csv.reader(filename, delimiter = ",")
    for row in data:
        data_list.append(row)
        
with open("data/detecciones.csv","r") as filename:
    data = csv.reader(filename, delimiter = ",")
    for row in data:
        data_list1.append(row)
        
myform = form.Form(form.Dropdown('Categoria', categorias),
                  form.Dropdown('Anio', anios))

class Index:
    casos = {}
    def GET(self): 
        form = myform()
        return render.index(form,self.casos)

    def POST(self):
        self.casos = {}
        form = myform()
        if not form.validates():
            return render.index(form,self.casos)
        elif form['Categoria'].value == "Inmunizaciones":
            if form['Anio'].value == "2000":
                for row in data_list:
                    self.casos[row[0]] = row[1]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2001":
                for row in data_list:
                    self.casos[row[0]] = row[2]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2002":
                for row in data_list:
                    self.casos[row[0]] = row[3]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2003":
                for row in data_list:
                    self.casos[row[0]] = row[4]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2004":
                for row in data_list:
                    self.casos[row[0]] = row[5]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2005":
                for row in data_list:
                    self.casos[row[0]] = row[6]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2006":
                for row in data_list:
                    self.casos[row[0]] = row[7]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2007":
                for row in data_list:
                    self.casos[row[0]] = row[8]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2008":
                for row in data_list:
                    self.casos[row[0]] = row[9]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2009":
                for row in data_list:
                    self.casos[row[0]] = row[10]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2010":
                for row in data_list:
                    self.casos[row[0]] = row[11]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2011":
                for row in data_list:
                    self.casos[row[0]] = row[12]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2012":
                for row in data_list:
                    self.casos[row[0]] = row[13]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2013":
                for row in data_list:
                    self.casos[row[0]] = row[14]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2014":
                for row in data_list:
                    self.casos[row[0]] = row[15]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2015":
                for row in data_list:
                    self.casos[row[0]] = row[16]
                return render.index(form,self.casos)
        elif form['Categoria'].value == "Detecciones":
            if form['Anio'].value == "2000":
                for row in data_list1:
                    self.casos[row[0]] = row[1]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2001":
                for row in data_list1:
                    self.casos[row[0]] = row[2]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2002":
                for row in data_list1:
                    self.casos[row[0]] = row[3]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2003":
                for row in data_list1:
                    self.casos[row[0]] = row[4]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2004":
                for row in data_list1:
                    self.casos[row[0]] = row[5]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2005":
                for row in data_list1:
                    self.casos[row[0]] = row[6]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2006":
                for row in data_list1:
                    self.casos[row[0]] = row[7]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2007":
                for row in data_list1:
                    self.casos[row[0]] = row[8]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2008":
                for row in data_list1:
                    self.casos[row[0]] = row[9]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2009":
                for row in data_list1:
                    self.casos[row[0]] = row[10]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2010":
                for row in data_list1:
                    self.casos[row[0]] = row[11]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2011":
                for row in data_list1:
                    self.casos[row[0]] = row[12]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2012":
                for row in data_list1:
                    self.casos[row[0]] = row[13]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2013":
                for row in data_list1:
                    self.casos[row[0]] = row[14]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2014":
                for row in data_list1:
                    self.casos[row[0]] = row[15]
                return render.index(form,self.casos)
            elif form['Anio'].value == "2015":
                for row in data_list1:
                    self.casos[row[0]] = row[16]
                return render.index(form,self.casos)

class View:

    def GET(self, id):
        """ View single post """
        post = model.get_post(int(id))
        return render.view(post)

class Viewdata:
    def GET(self):
        """ View single post """
        posts = model.get_posts()
        return render.viewdata(posts)
    

class New:
    def GET(self):
        return render.new()

    def POST(self):
        i = web.input()
        model.new_post(i.title, i.original, i.genero, i.nac, i.year, i.dir,
                      i.guion, i.fecha)
        raise web.seeother('/viewdata')


class Delete:

    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother('/viewdata')


class Edit:
    def GET(self, id):
        post = model.get_post(int(id))
        return render.edit(post)


    def POST(self, id):
        i = web.input()
        model.update_post(int(id), i.title, i.original, i.genero, i.nac, i.year, i.dir,
                      i.guion, i.fecha)
        raise web.seeother('/viewdata')
        
class Login:

    def GET(self):
        return render.login()


    def POST(self):
        i = web.input()
        post = model.get_users()
        if len(i) == 0:
            return render.login()
        else:
            for row in post:
                if row.username == i.user and row.pw == i.pw:
                    raise web.seeother('/viewdata')
                else:
                    raise web.seeother('/login')
        


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()