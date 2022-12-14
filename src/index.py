from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_DATABASE_HOST']     = 'localhost'
app.config['MYSQL_DATABASE_USER']     = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Matias8*00'
app.config['MYSQL_DATABASE_DB']       = 'usuarios_museo'

mysql.init_app(app)

@app.route('/') #Esta va a ser la página principal
def Home():
    return render_template('home.html')

#@app.route('/about')
#def about():
#    return render_template('about.html')
 
@app.route('/expo_dinos')
def ExpoDinos():
    return render_template('/Expos/expo_dinos.html')

@app.route('/info_gigano')
def InfoGigano():
    return render_template('/Dinos/info_gigano.html')

@app.route('/info_amarga')
def InfoAmarga():
    return render_template('/Dinos/info_amarga.html')

@app.route('/info_argen')
def InfoArgen():
    return render_template('/Dinos/info_argen.html')

@app.route('/info_buitre')
def InfoBuitre():
    return render_template('/Dinos/info_buitre.html')

@app.route('/info_carno')
def InfoCarno():
    return render_template('/Dinos/info_carno.html')

@app.route('/info_drusi')
def InfoDrusi():
    return render_template('/Dinos/info_drusi.html')

@app.route('/info_Eora')
def InfoEora():
    return render_template('/Dinos/info_eora.html')

@app.route('/info_futal')
def InfoFutal():
    return render_template('/Dinos/info_futal.html')

@app.route('/info_Huincul')
def InfoHuincul():
    return render_template('/Dinos/info_Hunicul.html')

@app.route('/info_Isable')
def InfoIsable():
    return render_template('/Dinos/info_Isable.html')

@app.route('/info_Jaka')
def InfoJaka():
    return render_template('/Dinos/info_Jaka.html')

@app.route('/info_ketep')
def InfoKetep():
    return render_template('/Dinos/info_ketep.html')

@app.route('/info_lampa')
def InfoLampa():
    return render_template('/Dinos/info_lampa.html')

@app.route('/info_mega')
def InfoMegar():
    return render_template('/Dinos/info_mega.html')

@app.route('/info_noasa')
def InfoNoasa():
    return render_template('/Dinos/info_noasa.html')

@app.route('/info_orkor')
def InfoOrkor():
    return render_template('/Dinos/info_orkor.html')

@app.route('/info_patag')
def InfoPatag():
    return render_template('/Dinos/info_patag.html')

@app.route('/info_unen')
def InfoUnen():
    return render_template('/Dinos/info_unen.html')

@app.route('/info_zupay')
def InfoZupay():
    return render_template('/Dinos/info_zupay.html')


#Expo yacimientos después
@app.route('/expo_yacimientos')
def ExpoYaci():
    return render_template('/Expos/expo_yaci.html')

@app.route('/info_chocon')
def InfoChocon():
    return render_template('/Yaci/info_chocon.html')

#Creamos Perfil
@app.route('/perfil')
def Perfil():
    return render_template('/Usuario/perfil.html')
#Esta es la parte de logueo de usuario. Después la vemos. 

@app.route('/login')
def Login():
    return render_template('/Usuario/login.html')

#Esta es la parte de creación de usuario.
@app.route('/create_user')
def create_user():
    conexion=mysql.connect()
    print(conexion)
    return render_template('/Usuario/create_user.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        email    = request.form['emailConf']
        password = request.form['txtPasswordConf']
        
        cur = mysql.connection.cursor()

        cur.execute('insert into usuario (email,password) values (%s,%s)',
        (email,password))

        mysql.connection.commit()

        cur.close()
        return 'Recibido, gracias!'

if __name__ == '__main__':
    app.run(debug=True) #Ejecutar la aplicación, el debug es para reiniciar y no tener que ir cerrando todo el tiempo

