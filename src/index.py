from flask import Flask, render_template, request, redirect
import smtplib
from decouple import config

app = Flask(__name__)

@app.route('/') #Esta va a ser la página principal
def Home():
    return render_template('home.html')

@app.route('/contacto')
def Contacto():
    return render_template('contacto.html')

@app.route('/mensaje', methods=["POST"])
def Mensaje():
    if request.method == "POST":
        nombre = request.form['txtNombre']
        email = request.form['email']
        asunto = request.form['txtAsunto']
        comentario = request.form['txtComent']
    
    #Envío de email
    message='Hola {}.\nGracias por enviarnos tu mensaje.\n\nTu mensaje\n{}'.format(nombre,comentario)
    subject='Cretaceum- Contacto'

    message='Subject:{}\n\n{}'.format(subject,message)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('matias.pina@ifts18.edu.ar',config('PASS_EMAIL'))

    server.sendmail('matias.pina@ifts18.edu.ar',email,message)

    server.quit()
    
    return render_template("mensaje.html")

@app.route('/que_es')
def quEs():
    return render_template('queEs.html')

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

@app.route('/expo_yacimientos')
def ExpoYaci():
    return render_template('/Expos/expo_yaci.html')

@app.route('/info_chocon')
def InfoChocon():
    return render_template('/Yaci/info_chocon.html')

@app.route('/info_auca')
def InfoAuca():
    return render_template('/Yaci/info_auca.html')

@app.route('/info_barrales')
def InfoBarrales():
    return render_template('/Yaci/info_barrales.html')

@app.route('/info_carmen')
def InfoCarmen():
    return render_template('/Yaci/info_carmen.html')

@app.route('/info_toropi')
def InfoToropi():
    return render_template('/Yaci/info_toropi.html')

@app.route('/info_ischi')
def InfoIschi():
    return render_template('/Yaci/info_ischi.html')

@app.route('/info_mef')
def InfoMef():
    return render_template('/Yaci/info_mef.html')

@app.route('/info_valcheta')
def InfoValcheta():
    return render_template('/Yaci/info_valcheta.html')


if __name__ == '__main__':
    app.run(debug=True) #Ejecutar la aplicación, el debug es para reiniciar y no tener que ir cerrando todo el tiempo

