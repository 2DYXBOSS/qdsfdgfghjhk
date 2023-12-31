from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template , redirect , request,url_for,flash,Response
from flask import render_template , redirect , request,url_for,flash,session ,Response
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
import os
import datetime

data = datetime.date.today()
dataheure = datetime.datetime.now()

print(dataheure)

from flask import Flask, request, render_template, redirect, url_for,send_file
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



# Configurations pour le serveur SMTP


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'BONJOUR'


app.config['SECRET_KEY'] = 'sdfgghjklhkj'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '0streamblay@gmail.com'
app.config['MAIL_PASSWORD'] = 'vgux fpjq qyqr nxem'
app.config['MAIL_DEFAULT_SENDER'] = '0streamblay@gmail.com'



SMTP_SERVER = 'smtp.googlemail.com'  # Remplacez par l'adresse de votre serveur SMTP
SMTP_PORT = 587  # Port SMTP (généralement 587 pour TLS)
SMTP_USERNAME = 'pythonanywhere225@gmail.com'
SMTP_PASSWORD = 'tdqn cklm uvjd aonn'
# Clé secrète pour sécuriser l'application
app.secret_key = os.urandom(24)
mail = Mail(app)
# fin

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


db = SQLAlchemy(app)



debug = True
# login_manager = LoginManager()
# login_manager.init_app(app)

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")


with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
class Notificap(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    
    quantite = db.Column(db.Integer,nullable = False)
    prix = db.Column(db.Integer,nullable = False)
    image = db.Column(db.String(100), unique = False , nullable = False)
    mail = db.Column(db.String(100), unique = False , nullable = False)
    dataheure = db.Column(db.String(100), unique = False , nullable = False)
    

   
    def __init__(self,prix,quantite,image,mail,dataheure):
        
        self.prix = prix
        self.quantite = quantite
        self.image = image
        self.mail = mail
        self.dataheure = dataheure
        

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(prix: {self.prix}, quantite: {self.quantite}, image: {self.image}, mail: {self.mail})"
    def __repr__(self):
        
        return {
            
            "prix": self.prix,
            "quantite": self.quantite,
            "image": self.image,
            "mail": self.mail,
            "dataheure": self.dataheure
            
        }
# creation de ma table dans la base de donnée 

class Profil(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), unique = False , nullable = False)
    last_name = db.Column(db.String(20), unique = True , nullable = False)
    age = db.Column(db.String(8),nullable = False)

    # achat = db.relationship('Panier',back_populates='prendre')
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(first_name: {self.first_name}, last_name: {self.last_name}, age: {self.age})"
    def __repr__(self):
        
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
class Connecter(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), unique = False , nullable = False)
    last_name = db.Column(db.String(20), unique = True , nullable = False)
    age = db.Column(db.String(8),nullable = False)

    # achat = db.relationship('Panier',back_populates='prendre')
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()

    def __repr__(self):
        
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }


with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")


with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")

class Maboutik(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(100), unique = False , nullable = False)
    description = db.Column(db.String(100), unique = True , nullable = False)
    prix = db.Column(db.Integer,nullable = False)
    image = db.Column(db.String(100), unique = True , nullable = False)
    categorie = db.Column(db.String(100), unique = False , nullable = False)
    like = db.Column(db.Integer, unique = False , nullable = False)
   
    def __init__(self,nom,description,prix,image,categorie,like):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.image = image
        self.categorie = categorie
        self.like = like


    # db.init_app(app)
    # with app.app_context() :
    # #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(nom: {self.nom}, description: {self.description}, age: {self.age})"
    def __repr__(self):
        
        return {
            "nom": self.nom,
            "description": self.description,
            "prix": self.prix,
            "image": self.image,
            "categorie": self.categorie,
            "like": self.like
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
class Userpanierezeze(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(100), unique = False , nullable = False)
    description = db.Column(db.String(100), unique = False , nullable = False)
    prix = db.Column(db.Integer,nullable = False)
    mail = db.Column(db.String(100), unique = False , nullable = False)
    image = db.Column(db.String(100), unique = False , nullable = False)
    qutite = db.Column(db.Integer,nullable = False)
    

    
    def __init__(self,nom,description,prix,mail,image,qutite):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.mail = mail
        self.image = image
        self.qutite = qutite 
        

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(nom: {self.nom}, description: {self.description}, prix: {self.prix}, mail: {self.mail}, image: {self.image})"
    def __repr__(self):
        
        return {
            "nom": self.nom,
            "description": self.description,
            "prix": self.prix,
            "mail": self.mail,
            "image": self.image,
            "qutite": self.qutite,
            
        }
with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
class Userpaniere(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(100), unique = False , nullable = False)
    description = db.Column(db.String(100), unique = False , nullable = False)
    prix = db.Column(db.Integer,nullable = False)
    mail = db.Column(db.String(100), unique = False , nullable = False)
    image = db.Column(db.String(100), unique = False , nullable = False)
    

    
    def __init__(self,nom,description,prix,mail,image):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.mail = mail
        self.image = image
        

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(nom: {self.nom}, description: {self.description}, prix: {self.prix}, mail: {self.mail}, image: {self.image})"
    def __repr__(self):
        
        return {
            "nom": self.nom,
            "description": self.description,
            "prix": self.prix,
            "mail": self.mail,
            "image": self.image,
            
        }


with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
class Img(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    img = db.Column(db.Text, unique = False , nullable = False)
    name = db.Column(db.Text, nullable = False)
    mimetype = db.Column(db.Text,nullable = False)
with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")






@app.route('/panieruser')
def detail():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    data = Userpanierezeze.query.all()
    Panier = Maboutik.query.all()
    # zee = Connecter.query.get(1)
    user = Userpanierezeze.query.filter_by(mail = useru.last_name).first()
    
    frr = []
    imm = []
    mop = []
    for i in data : 
        if i.mail == useru.last_name :
            frr.append(i.qutite)
            mop.append(i)
    
    tableau_trié = sorted(mop, key=lambda x: x.nom)


    pri = 0
    for i in mop :
        pri += i.prix*int(i.qutite)
    tva = int(pri * 0.0002)
    eta = int(pri * 0.0001)
    mon = int(pri * 0.00005)
    pri = int(pri) + int(tva) + int(eta) + int(mon)
    az = len(frr)
    er =[az,user,pri]
    az = len(frr)
    er =[sum(frr),tableau_trié,pri,tva,eta,mon]
    return render_template('panieruser.html',user = er)

# RECHERCHE DANS LA BASE DE DONNEE {}
@app.route('/recherche',methods = ["POST"])
def recherche() :
    if 'utilisateur_id' in session:
        user = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    
    if request.method == 'POST':
        mots = request.form['textenter']
    mot = (mots.strip()).lower()
    aer = Maboutik.query.all()
    data = Userpanierezeze.query.all()
    frr = []

    for i in data : 
        if i.mail == user.last_name :
            frr.append(i.qutite)
   
    
    az = len(frr)
    
    sac = []
    for i in aer:
        if i.categorie == "Sac" :
            sac.append(i)
    vetement = []
    for i in aer:
        if i.categorie == "Vetement" :
            vetement.append(i)
    fourniture = []
    for i in aer:
        if i.categorie == "Fourniture" :
            fourniture.append(i)

    recherche = []
    
    if mot == 'sacs' or mot == 'sac' or mot == 'sacs à mains' or mot == 'sac à mains' or mot == 'sacs à dos' or mot == 'sac à dos' :
        recherche=sac

    if mot == 'vêtement' or mot == 'vêtements' or mot == 'vetement' or mot == 'vetements' or mot == 'habits' or mot == 'habit' :
        recherche=vetement

    if mot == 'fourniture' or mot == 'fournitures' or mot == 'livre' or mot == 'livres' :
        recherche=fourniture


    er =[sum(frr),recherche,mot]
    if len(recherche) <= 0 :
        flash("CET ARTICLE N'EST PAS DISPONIBLE POUR LE MOMENT !")
    return render_template('recherc.html',ae = er)
# PAYEMENT {}
@app.route('/payeffectue')
def payeffectue() :
    return render_template('afipay.html')
@app.route('/Payement')
def Payement() :
    if 'utilisateur_id' in session:
        user = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    # user = Connecter.query.all()
    data = Userpanierezeze.query.all()
    # zee = Connecter.query.get(1)   
    frr = []
    ut = []
    etr = []
    mop = []
    for i in data : 
        if i.mail == user.last_name :
            frr.append(i.qutite)
            mop.append(i)
            
            ut.append([i.nom,int(i.prix)*int(i.qutite)])
    pri = 0
    for i in mop :
        pri += int(i.prix)*int(i.qutite)
    
    az = len(frr)
    for i in mop :
        etr.append(i.image)
    po = 'a.jpeg'
    premier = [mop[0]]
    
    image = mop[0:4:1]
    
    er =[sum(frr),user,pri,ut,mop,premier,image]
 
    print(f"{etr[0]}")
    return render_template('payement.html',ae = er)


# FIN PAYEMENT {}
# # QRPAYEMENT {}
# @app.route('/QrPayement')
# def QrPayement() :
#     if 'utilisateur_id' in session:
#         user = Profil.query.get(session['utilisateur_id'])
#     else:
#         return redirect('/pre')
#     # user = Connecter.query.all()
#     data = Userpanierezeze.query.all()
#     # zee = Connecter.query.get(1)   
#     frr = []
    
    
#     for i in data : 
#         if i.mail == user.last_name :
#             frr.append(i)
            
    
    
#     az = len(frr)
    
#     er =[az]
 
#     return render_template('codeqr.html',ae = er)
# # FIN QRPAYEMENT {}

   

# PANIER {}
# @app.route('/panieruser')
# def panieruserk():
#     if 'utilisateur_id' in session:
#         useru = Profil.query.get(session['utilisateur_id'])
#     else:
#         return redirect('/pre')
#     data = Userpanierezeze.query.all()
#     Panier = Maboutik.query.all()
#     # zee = Connecter.query.get(1)
#     user = Userpanierezeze.query.filter_by(mail = useru.last_name).first()
    
#     frr = []
#     imm = []
    
#     for i in data : 
#         if i.mail == useru.last_name :
#             frr.append(i)
    
    
#     pri = 0
#     for i in frr :
#         pri += i.prix
#     az = len(frr)
#     er =[az,user,pri]
#     az = len(frr)
#     er =[az,frr,pri]
#     return render_template('panieruser.html',user = er)
    # return render_template('panieruser.html',user = [user])
# FIN PANIER {}


# PUBLICATION {}
@app.route('/achat')
def achl():
    if 'utilisateur_id' in session:
        user = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    aer = Maboutik.query.all()
   
    # addsac = []
    # for i in aer :
    #     print(i.nom)
    #     for le in " ".join([i]) :

    #         if 'sac' or 'Sac' or 'SAC':
    #             addsac.append(i)
    # for i in addsac :
    #     print(i)
    data = Userpanierezeze.query.all()
    # zee = Connecter.query.get(1)   
    frr = []

    for i in data : 
        if i.mail == user.last_name :
            frr.append(i.qutite)
   
   
    sac = []
    for i in aer:
        if i.categorie == "Sac" :
            sac.append(i)
    
    vetement = []
    for i in aer:
        if i.categorie == "Vetement" :
            vetement.append(i)
    
    
    fourniture = []
    for i in aer:
        if i.categorie == "Fourniture" :
            fourniture.append(i)
    az = sum(frr)
    print(az)
    frrnoz = Notificap.query.all()
    notifm = []
    for i in frrnoz : 
        if i.mail == user.last_name :
            notifm.append(i)
    tail = len(notifm)
   
    er =[sum(frr),aer,sac,vetement,fourniture,tail]
    
    return render_template('achat.html',ae = er)
# FIN PUBLICATION {}


# PROFIL USER {}
@app.route('/useprid')
def useprid():
    if 'utilisateur_id' in session:
        user = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    data = Userpanierezeze.query.all()
    
       
    frr = []
    mop = []

    
    for i in data : 
        if i.mail == user.last_name :
            frr.append(i.qutite)
            mop.append(i)
   
    
    az = sum(frr)

    frrno = Notificap.query.all()
    notif = []
    for i in frrno : 
        if i.mail == user.last_name :
            notif.append(i)

    er =[az,user,notif,mop]
 

    return render_template('useprid.html',ae = er)
# FIN PROFIL USER {}

# PAGE ACCEUIL AVANT CONNEXION {}
@app.route('/')
def page():
    return render_template("page.html")
# FIN PAGE ACCEUIL AVANT CONNEXION {}


# PAGE ACCEUIL APRES CONNEXION {}
@app.route('/home')
def home():
    if 'utilisateur_id' in session:
        user = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    # user = Connecter.query.all()
    return render_template('home.html')
@app.route('/autre/<int:id>')
def join(id):
    user = Profil.query.filter_by(id=id).first()
    return render_template('miseajour.html')
# FIN PAGE ACCEUIL APRES CONNEXION {}


# DECONNEXION ADMIN {}
@app.route('/deconnexionad')
def deconnexionad():
    session.pop('admining_id', None)
    return redirect('/pre')
# FIN DECONNEXION ADMIN{}


# DECONNEXION {}
@app.route('/deconnexion')
def deconnexion():
    session.pop('utilisateur_id', None)
    return redirect('/pre')
# FIN DECONNEXION {}


# CONNEXION {}
@app.route('/pre')
def pree():
    return render_template('connexion.html')
@app.route('/sprome',methods = ["GET","POST"])
def sprome() :
    compte = 0
    eudeu = Profil.query.all()
    profilp = Maboutik.query.all()
    eude = [eudeu,profilp]
    user = Profil.query.filter_by(last_name = request.form.get("last_name"),age = request.form.get("age")).first()
    userr = Connecter.query.filter_by(last_name = request.form.get("last_name"),age = request.form.get("age")).first()

    if user :
        
        datae = Profil.query.get(user.id)
        
        print(f"vous etes connecter{user.first_name}{user.id}")
        

        session['utilisateur_id'] = user.id
        return redirect('/home')

    elif userr :
        session['admining_id'] = userr.id
        return redirect('/admining')
    else :

        flash("Email ou Mot de passe invalide")
        return redirect("/pre")
# FIN CONNEXION {}




# ADMIN{}
@app.route('/admining')
# @login_requiered
def index() :
    if 'admining_id' in session:
        userr = Connecter.query.get(session['admining_id'])
    else:
        return redirect('/pre')
    
 
        
        
    profil = Maboutik.query.all()
    profile = Profil.query.all()
    
    profiles = [profil , profile]
    return render_template('index.html', profiles = profiles)
   
# FIN ADMIN{}




# AJOUTER DES IMAGES PAR UN KV
@app.route('/upload',methods = ["POST"])
def upload():
    pic = request.files['pic']
    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    img = Img(img = pic.read(),name = filename,mimetype = mimetype)
    print(img)
    db.session.add(img)
    db.session.commit()
    return redirect("/recup")

@app.route('/recup')
def recup():
    data = Img.query.get(Img.id)
    return redirect('recu.html',Response(data.name, mimetype=data.mimetype))

# @app.route('/ee/<int:id>')
# def ee(id):
#     data = Img.query.get(id)
#     return redirect(url_for('ee', id=id),Response(data.img, mimetype=data.mimetype))


# def conver_image_into_binary(filename):
#     with open(filename, 'rb') as file:
#         photo_image = file.read()
#     return photo_image


# comment recuperer une image de la base de donnée
# @app.route('/img/<int:id>')
# def img(id):
#     data = Img.query.get(id)
#     return Response(data.img, mimetype=data.mimetype)

# FIN AJOUTER DES IMAGES PAR UN KV






# ENVOYER MAIL
@app.route('/envoyer_emailhom', methods=['POST'])
def envoyer_emailhom():
    if 'utilisateur_id' in session:
        user = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    if request.method == 'POST':
        # destinataire = request.form['destinataire']
        destinataire = "0streamblay@gmail.com"
        # sujet = request.form['sujet']
        # tre = Connecter.query.get(1)
        if 'utilisateur_id' in session:
            user = Profil.query.get(session['utilisateur_id'])
        else:
            return redirect('/pre')
        dfggh = user.last_name
        sujet = dfggh
        contenu = request.form['contenu']

        msg = Message(sujet, recipients=[destinataire])
        msg.body = contenu
       
        try:
            mail.send(msg)
            
        except Exception as e:
            flash("Une erreur s'est produite lors de l'envoi de l'e-mail", 'danger')

        return redirect("/useprid")
# FIN ENVOYER MAIL
# ENVOYER MAIL
@app.route('/envoyer_emailcom', methods=['POST'])
def envoyer_emailcom():
    if 'utilisateur_id' in session:
        user = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    if request.method == 'POST':
        # destinataire = request.form['destinataire']
        destinataire = "0streamblay@gmail.com"
        # sujet = request.form['sujet']
        # tre = Connecter.query.get(1)
        if 'utilisateur_id' in session:
            user = Profil.query.get(session['utilisateur_id'])
        else:
            return redirect('/pre')
        dfggh = user.last_name
        sujet = dfggh
        contenu = request.form['contenu']

        msg = Message(sujet, recipients=[destinataire])
        msg.body = contenu
       
        try:
            mail.send(msg)
            
        except Exception as e:
            flash("Une erreur s'est produite lors de l'envoi de l'e-mail", 'danger')

        return redirect("/achat")
# FIN ENVOYER MAIL
# ENVOYER MAIL
# @app.route('/envoyer_email', methods=['POST'])
# def envoyer_email():
#     if 'utilisateur_id' in session:
#         user = Profil.query.get(session['utilisateur_id'])
#     else:
#         return redirect('/pre')
#     if request.method == 'POST':
#         # destinataire = request.form['destinataire']
#         destinataire = "0streamblay@gmail.com"
#         # sujet = request.form['sujet']
#         # tre = Connecter.query.get(1)
#         if 'utilisateur_id' in session:
#             user = Profil.query.get(session['utilisateur_id'])
#         else:
#             return redirect('/pre')
#         dfggh = user.last_name
#         sujet = dfggh
#         contenu = request.form['contenu']

#         msg = Message(sujet, recipients=[destinataire])
#         msg.body = contenu
       
#         try:
#             mail.send(msg)
            
#         except Exception as e:
#             flash("Une erreur s'est produite lors de l'envoi de l'e-mail", 'danger')

#         return redirect("/home")
# FIN ENVOYER MAIL




# app.config['SECRET_KEY'] = 'sdfgghjklhkj'
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'pythonanywhere225@gmail.com'
# app.config['MAIL_PASSWORD'] = 'tdqn cklm uvjd aonn'
# app.config['MAIL_DEFAULT_SENDER'] = 'pythonanywhere225@gmail.com'

# Clé secrète pour sécuriser l'application


@app.route('/image/<nom_fichier>')
def recuperer_image(nom_fichier):
    try:
        # Spécifiez le chemin complet vers le fichier image
        chemin_image = f'static\image\{nom_fichier}'
        az = send_file(chemin_image, mimetype='image/jpeg')
        # Récupérez l'image à partir du fichier
        return az  # Spécifiez le type MIME approprié pour votre image

    except Exception as e:
        return str(e), 404  # Gérez les erreurs appropriées


@app.route('/envoyer_email', methods=['POST'])
def envoyer_email():
    if 'utilisateur_id' in session:
        user = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    if 'photo' not in request.files:
        return "Aucun fichier n'a été téléchargé."

    fichier = request.files['photo']
    # image = MIMEImage(fichier.read(), name=fichier.filename)
    # print(image)
    # if fichier.filename == '':
    #     return "Aucun fichier n'a été sélectionné."
    
    # return render_template('connexion.html')
    if fichier:
        # Construire le message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = "0streamblay@gmail.com"
        msg['Subject'] = request.form['sujet']
        masz = user.last_name + "    " + request.form['contenu']
        message_texte = MIMEText(masz)
        msg.attach(message_texte)

        # Ajouter l'image au message
        image = MIMEImage(fichier.read(), name=fichier.filename)
        msg.attach(image)

        # Connexion au serveur SMTP et envoi du courrier électronique
        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, "0streamblay@gmail.com", msg.as_string())
            server.quit()
            return redirect('/home')
        except Exception as e:
            return "Erreur lors de l'envoi de l'e-mail : " + str(e)

# COMMANDER
@app.route('/commande', methods=['POST'])
def commande():
    # utilisateur_id = Profil.query.get(session['utilisateur_id'])
    
    # oiuy = utilisateur_id.first_name
    if 'utilisateur_id' in session:
        oiuy = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    if request.method == 'POST':
        data = Userpanierezeze.query.all()
        
        frr = []
        imm = []
        mop = []
        img = []
        for i in data : 
            if i.mail == oiuy.last_name :
                frr.append(i.qutite)
                mop.append(i)
                img.append(i.image)
        
        tableau_trié = sorted(mop, key=lambda x: x.nom)
        prix = request.form['prix']
        print(img)
        image = ",".join(img)
        quantite = sum(frr)
        mail = oiuy.last_name
        a = dataheure
        notif = Notificap(prix = prix, quantite = quantite, image = image, mail = mail , dataheure=dataheure )
        
        db.session.add(notif)
        db.session.commit()
        # flash('Commande effectuée avec succes', 'success')

        # destinataire = "0streamblay@gmail.com"
        # # sujet = request.form['sujet']
        # # tre = Connecter.query.get(1)
        
        # sujet = mail
        # contenu = "quantite"

        # msg = Message(sujet, recipients=[destinataire])
        # msg.body = contenu
       
        # try:
        #     mail.send(msg)
            
        # except Exception as e:
        #     flash("Une erreur s'est produite lors de l'envoi de l'e-mail", 'danger')
        
        # destinataire = "0streamblay@gmail.com"
        
        # data = Userpanierezeze.query.all()
        # frr = []
        # ut = []
        
        # for i in data : 
        #     if i.mail == oiuy.last_name :
        #         frr.append(i)
        #         ut.append([str(i.nom) ,str(i.prix) + " FCFA"])
        # pri = 0
        # for i in frr :
        #     pri += i.prix
        
        # az = len(frr)
        # er =[az,oiuy,pri,ut]
    
        # dfggh = oiuy.last_name
        # sujet = 'dfggh'
        # numero = request.form['numero']
        # lieux = request.form['lieux']
        # recu = []
        # lo = "\n"
        # for i in ut :
        #     recu.append(" : ".join(i))
        # contenu = f"COMMANDE DE MR/MME \n{oiuy} \n{dfggh} \n\n\nNOMBRE D'ARTICLES : {az} \n\n{lo.join(recu)} \n\nPRIX : {pri} FCFA \n\nNUMERO : {numero} \n\nLOCALISATION : {lieux} "
        # # contenu = 250
        
        # msg = Message(sujet, recipients=[destinataire])
        # msg.body = contenu

        # try:
        #     mail.send(msg)
        #     flash("COMMANDE VALIDEE AVEC SUCCES")
            
        # except Exception as e:
        #     flash("Une erreur s'est produite lors de l'envoi de l'e-mail", 'danger')

        
    # ertp = 5

    # if 'utilisateur_id' in session:
    #     user = Profil.query.get(session['utilisateur_id'])
    # else:
    #     return redirect('/pre')
    # if request.method == 'POST':
    #     # numero = request.form['numero']
    #     # lieux = request.form['lieux']
    #     # destinataire = request.form['destinataire']
    #     destinataire = "0streamblay@gmail.com"
    #     # sujet = request.form['sujet']
    #     # tre = Connecter.query.get(1)
    #     if 'utilisateur_id' in session:
    #         user = Profil.query.get(session['utilisateur_id'])
    #     else:
    #         return redirect('/pre')
    #     dfggh = user.last_name
    #     sujet = dfggh
    #     contenu = f"request.form['contenu'{sujet}"
    #     # contenu = f"request.form['contenu'{sujet} \n{numero} \n{lieux}"

    #     msg = Message(sujet, recipients=[destinataire])
    #     msg.body = contenu
       
    #     try:
    #         mail.send(msg)
            
    #     except Exception as e:
    #         flash("Une erreur s'est produite lors de l'envoi de l'e-mail", 'danger')


        # prix = request.form['prix']
        # image = request.form['image']
        # quantite = request.form['quantite']
        # mail = request.form['maill']
        
        # notif = Notificap(prix = prix, image = image, quantite = quantite, mail = mail)
        # db.session.add(notif)
        # db.session.commit()
        # return redirect("/home")


    # if request.method == 'POST':

    #     destinataire = dfggh
      
        
    #     sujet = "Votre commande sur BLAY LIBRARY"
    #     # contenu = f"NOMBRE D'ARTICLES : {az} \n\n{lo.join(recu)} \n\nPRIX : {pri} FCFA \n\nNUMERO : {numero} \n\nLOCALISATION : {lieux} "

    #     contenu = 'bonjour'
    #     msg = Message(sujet, recipients=[destinataire])
    #     msg.body = contenu
       
    #     try:
    #         mail.send(msg)
          
    #     except Exception as e:
    #         flash("Une erreur s'est produite lors de l'envoi de l'e-mail", 'danger')

    #     return redirect("/Payement")
    
        # destinataire = request.form['destinataire']
    # destinataire = "0streamblay@gmail.com"
    # # sujet = request.form['sujet']
    # # tre = Connecter.query.get(1)
    # if 'utilisateur_id' in session:
    #     user = Profil.query.get(session['utilisateur_id'])
    # else:
    #     return redirect('/pre')
    # dfggh = user.last_name
    # sujet = dfggh
    # contenu = 'request.form['']'

    # msg = Message(sujet, recipients=[destinataire])
    # msg.body = contenu
    
    # try:

    #     mail.send(msg)
    #     flash("Commande validee avec succes", 'success')

        
    # except Exception as e:
    #     flash("Une erreur s'est produite lors de l'envoi de l'e-mail", 'danger')

    return redirect("/valcommande")

@app.route('/valcommande')
def valcommande():
    destinataire = "0streamblay@gmail.com"
    # sujet = request.form['sujet']
    # tre = Connecter.query.get(1)
    if 'utilisateur_id' in session:
        user = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    dfggh = user.last_name
    sujet = dfggh

    data = Userpanierezeze.query.all()
 
    
    frr = []
    imm = []
    pop = []
    calvo = 0
    for i in data : 
        if i.mail == user.last_name :
            frr.append(i.qutite)
            calvo += int(i.prix)*int(i.qutite)
            imm.append([str(i.nom),str(i.qutite),str(i.prix*i.qutite)+" FCFA"])
    
    for i in imm :
        pop.append(" -#- ".join(i))
    data = datetime.date.today()
    dataheure = datetime.datetime.now()

    print(dataheure)         

    mepo = " /---/ ".join(pop)
    contenu = f"Aujourd'hui {dataheure} \n\nNouvelle Commande de {user.last_name} \n\n\n{mepo} \n\n\nCOUT TOTAL : {calvo} FCFA "
    # contenu = f"bonjour , {user.last_name} \Commnde {envo}"

    msg = Message(sujet, recipients=[destinataire])
    msg.body = contenu
    
    try:

        mail.send(msg)

        
    except Exception as e:
        flash("Une erreur s'est produite lors de l'envoi de l'e-mail", 'danger')

    return redirect("/procomm")
@app.route('/procomm')
def procomm():
    # sujet = request.form['sujet']
    # tre = Connecter.query.get(1)
    if 'utilisateur_id' in session:
        user = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    
    destinataire = str(user.last_name)

    sujet = "NOUVELLE COMMANDE SUR BLAY LIBRARY"

    data = Userpanierezeze.query.all()
 
    
    frr = []
    imm = []
    pop = []
    calvo = 0
    for i in data : 
        if i.mail == user.last_name :
            frr.append(i.qutite)
            calvo += int(i.prix)*int(i.qutite)

            imm.append([str(i.nom),str(i.qutite),str(i.prix*i.qutite)+" FCFA"])
    
    for i in imm :
        pop.append(" -#- ".join(i))
    data = datetime.date.today()
    dataheure = datetime.datetime.now()

    print(dataheure) 
    mepo = " /---/ ".join(pop)
    contenu = f"Aujourd'hui {dataheure} \n\nVous avez valider une nouvelle Commande sur BLAY LIBRARY \n\n\n{mepo} \n\n\nCOUT TOTAL : {calvo} FCFA \n\n\nJOUR/HEURES{dataheure}"
    # contenu = f"bonjour , {user.last_name} \Commnde {envo}"

    msg = Message(sujet, recipients=[destinataire])
    msg.body = contenu
    
    try:

        mail.send(msg)
        flash("Commande validee avec succes", 'success')

        
    except Exception as e:
        flash("Une erreur s'est produite lors de l'envoi de l'e-mail", 'danger')

    return redirect("/Payement")

@app.route('/usercommande')
def usercommande():
    
    # sujet = request.form['sujet']
    # tre = Connecter.query.get(1)
    if 'utilisateur_id' in session:
        user = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    destinataire = "0streamblay@gmail.com"
    dfggh = "0streamblay@gmail.com"
    sujet = dfggh
    contenu = f"bonjour , {user.last_name}"

    msg = Message(sujet, recipients=[destinataire])
    msg.body = contenu
    
    try:

        mail.send(msg)
        flash("Commande validee avec succes", 'success')

        
    except Exception as e:
        flash("Une erreur s'est produite lors de l'envoi de l'e-mail", 'danger')

    return redirect("/Payement")
    # return render_template("payement.html")
# FIN COMMANDER


# # COMMANDER
# @app.route('/commande', methods=['POST'])
# def commande():
#     utilisateur_id = Profil.query.get(session['utilisateur_id'])
#     oiuy = utilisateur_id.first_name
#     if request.method == 'POST':
#         prix = request.form['prix']
#         image = request.form['image']
#         quantite = request.form['quantite']
#         notif = Notife(prix = prix, image = image, quantite = quantite)
#         # pani = Panier(nom = nom, description = description , prix = prix)
        
#         db.session.add(notif)
#         db.session.commit()
#         # return redirect("/admining")
        
#         # destinataire = request.form['destinataire']
#         destinataire = "0streamblay@gmail.com"
#         # sujet = request.form['sujet']
#         # user = Connecter.query.all()
#         if 'utilisateur_id' in session:
#             user = Profil.query.get(session['utilisateur_id'])
#         else:
#             return redirect('/pre')
#         data = Userpanierezeze.query.all()
#         # zee = Connecter.query.get(1)   
#         frr = []
#         ut = []
        
#         for i in data : 
#             if i.mail == user.last_name :
#                 frr.append(i)
#                 ut.append([str(i.nom) ,str(i.prix) + " FCFA"])
#         pri = 0
#         for i in frr :
#             pri += i.prix
        
#         az = len(frr)
#         er =[az,user,pri,ut]
    

#         # return render_template('payement.html',ae = er)
#         # tre = Connecter.query.get(1)
#         dfggh = user.last_name
#         sujet = dfggh
#         numero = request.form['numero']
#         lieux = request.form['lieux']
#         recu = []
#         lo = "\n"
#         for i in ut :
#             recu.append(" : ".join(i))
#         contenu = f"COMMANDE DE MR/MME \n{oiuy} \n{dfggh} \n\n\nNOMBRE D'ARTICLES : {az} \n\n{lo.join(recu)} \n\nPRIX : {pri} FCFA \n\nNUMERO : {numero} \n\nLOCALISATION : {lieux} "
        
        
#         # names = [['Adam',str(25)], ['Bob',str(58)], ['Cyril',str(32)]]
#         # recu = []
#         # # nl = '\n'
#         # # text = f"Winners are:{nl}{''.join(names)}"
#         # for i in names :
#         #     recu.append(",".join(i))
#         # print( '\n'.join(recu))
        
        
#         # names = ['Adam', 'Bob', 'Cyril']
#         # text = f"Winners are:\n{'\n'.join(names)}"
#         # print(text)
        
#         # names = ['Adam', 'Bob', 'Cyril']
#         # nl = '\n'
#         # text = f"Winners are:{nl}{nl.join(names)}"
#         # print(text)
#         msg = Message(sujet, recipients=[destinataire])
#         msg.body = contenu

#         try:
#             mail.send(msg)
#             flash("COMMANDE VALIDEE AVEC SUCCES")
            
#         except Exception as e:
#             flash("Une erreur s'est produite lors de l'envoi de l'e-mail", 'danger')

        
    
#     if request.method == 'POST':
#         # destinataire = request.form['destinataire']
#         destinataire = dfggh
#         # sujet = request.form['sujet']
#         # tre = Connecter.query.get(1)
        
#         sujet = "Votre commande sur BLAY LIBRARY"
#         contenu = f"NOMBRE D'ARTICLES : {az} \n\n{lo.join(recu)} \n\nPRIX : {pri} FCFA \n\nNUMERO : {numero} \n\nLOCALISATION : {lieux} "


#         msg = Message(sujet, recipients=[destinataire])
#         msg.body = contenu
       
#         try:
#             mail.send(msg)
          
#         except Exception as e:
#             flash("Une erreur s'est produite lors de l'envoi de l'e-mail", 'danger')

#         return redirect("/Payement")
# # FIN COMMANDER




















# PARTIE AJOUTER
# @app.route('/like',methods = ["POST"])
# def like():
#     if 'utilisateur_id' in session:
#         useru = Profil.query.get(session['utilisateur_id'])
#     else:
#         return redirect('/pre')
    
#     if request.method == 'POST' :
#         likere = Maboutik.query.all()
#         nom = request.form.get("nom")
#         description = request.form.get("description")
#         prix = request.form.get("prix")
#         image = request.form.get("image")
        
        
#         recpo = Maboutik.query.filter_by(nom = nom,description = description, prix = prix,image=image )
        
#         recpo.like += 1
#         db.session.commit()
#         return redirect("/achat")

# @app.route('/like/<int:post_id>', methods=['GET', 'POST'])
# def like(post_id):
    
#     post = Maboutik.query.get(post_id)  # Load the post object

#     if post:
#         post.like += 1
#         db.session.commit()
#         return redirect("/achat#{post_id}")  # Redirect to the index or wherever you want
#     else:
#         print("Post not found.")
#         return redirect("/achat")
# from flask import redirect, url_for

# @app.route('/like/<int:article_id>', methods=['POST'])
# def like_article(article_id):
#     article = Article.query.get_or_404(article_id)
#     article.likes += 1
#     db.session.commit()
#     return redirect(url_for('article_detail', article_id=article.id))

@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    try:
        post = Maboutik.query.get(post_id)  # Load the post object

        if post:
            post.like += 1
            db.session.commit()
           
            return redirect(url_for("achl", _anchor=f"{post_id}"))  # Redirect to the index or wherever you want
        else:
            print("Post not found.")
            return redirect(url_for("achl"))
    except Exception as e:
        print(f"Error liking post: {e}")
        db.session.rollback()  # Rollback changes in case of an error
        return redirect(url_for("achl"))

# PARTIE AJOUTER DES ARTICLES{}
@app.route('/objet',methods = ["POST"])
def objet(): 
    
    try :
        nom = request.form.get("nom")
        description = request.form.get("description")
        prix = request.form.get("prix")
        image = request.form.get("image") 
        like = 0 
        
        print('recu1')      
        categorie = request.form.get('selectOptione')
        print('recu2',categorie)      

        pani = Maboutik(nom = nom, description = description , prix = prix, image = image, categorie = categorie ,like=like)
        # pani = Panier(nom = nom, description = description , prix = prix)
        
        db.session.add(pani)
        db.session.commit()
             

        return redirect("/admining")
    except :
        return render_template("/boutique.html")
    

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/add_objet')
def add_objet():
    if 'admining_id' in session:
        useru = Profil.query.get(session['admining_id'])
    else:
        return redirect('/pre')
    return render_template("boutique.html")

@app.route('/add_objet', methods=['POST'])
def upload_image():
    try :
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print(file.filename)
        if file.filename == '':
            flash('Aucune image sélectionnée pour le téléchargement')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #print('upload_image filename: ' + filename)
            flash('Image téléchargée avec succès et affichée ci-dessous')
            return render_template('boutique.html', filename=file.filename)
            # return render_template('boutique.html', filename=filename)
    except:
        flash('Les types dimages autorisés sont - png, jpg, jpeg, gif')
        return redirect(request.url)

        # uploads.image
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename = 'uploads/' + filename), code=301)
# FIN AJOUTER DES ARTICLES{}


# AJOUTER DES USER{}
@app.route('/add_data')
def add_data():
    
    return render_template("add_profile.html")

@app.route('/add',methods = ["POST"])
def profile() :
    
    
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    age = request.form.get("age")
    conf = request.form.get("conf")
    

    if conf != age :
        flash("Entrez le meme mot de passe")
        return redirect("/add_data")
    
    for i in range (len(last_name)) :
        if last_name[i] == "@" :

            if "moc.liamg" == last_name[:i:-1]:

                pass
            else :
                flash("Email ou Mot de passe invalide")
                return redirect("/add_data")
            



    user = Profil.query.filter_by(last_name = request.form.get("last_name")).first()
    if user :
        flash("Ce compte existe deja") 
        return redirect(url_for("add_data"))
    else :
        if first_name != " " and last_name != " " and age is not None and len(age)== 8 :
            p = Profil(first_name = first_name, last_name = last_name , age = age)

            db.session.add(p)
            db.session.commit()
            return redirect("/pre")
        else :
            return redirect("/add_data")
        
# FIN AJOUTER DES USER{} 


# # AJOUTER DES PANIER DEPUIS RECHERC{}
# @app.route('/newrec',methods = ["POST"])
# def newrec():
#     zee = Connecter.query.get(1)
#     if 'utilisateur_id' in session:
#         useru = Profil.query.get(session['utilisateur_id'])
#     else:
#         return redirect('/pre')
#     user = Profil.query.filter_by(last_name = useru.last_name).first()
#     nom = request.form.get("nom")
#     desc = request.form.get("desc")
#     image = request.form.get("image")
#     prix = request.form.get("prix")
#     id = request.form.get("id")
#     mail = user.last_name
#     user = Userpanierezeze.query.filter_by(nom = nom, description = desc , prix = prix, mail = mail).first()
#     if user:
#         bou = Userpanierezeze.query.get(user.id)
#         bou.qutite = bou.qutite+1
#         db.session.commit()
#         return redirect("/recherche")
#     prix = Userpanierezeze(nom = nom, description = desc , prix = prix, mail = mail,image=image,qutite=1)
#     db.session.add(prix)
#     db.session.commit()
#     return redirect("/recherche")
# # FIN AJOUTER DES PANIER{} 
# AJOUTER DES PANIER{}


@app.route('/new',methods = ["POST"])
def new():
    try :
        zee = Connecter.query.get(1)
        if 'utilisateur_id' in session:
            useru = Profil.query.get(session['utilisateur_id'])
        else:
            return redirect('/pre')
        zert = Userpanierezeze.query.all()
        user = Profil.query.filter_by(last_name = useru.last_name).first()
        nom = (request.form.get("nom").upper()).strip()
        desc = request.form.get("desc").strip()
        image = request.form.get("image").strip()
        prix = request.form.get("prix").strip()
        id = request.form.get("id")
        aid = request.form.get("aid")
        mail = user.last_name
        print(f"{nom},{desc},{image},{prix},{id},{mail}")
        user = Userpanierezeze.query.filter_by(nom=nom,description = desc , prix = prix, mail = mail).first()
        
        if user:
            bou = Userpanierezeze.query.get(user.id)
            
            bou.qutite = bou.qutite+1
            db.session.commit()
            return redirect(url_for("achl", _anchor=f"{aid}"))

            # return redirect(url_for("achl", _anchor=f"{ze}")) 
        prix = Userpanierezeze(nom = nom, description = desc , prix = prix, mail = mail,image=image,qutite=1)
        db.session.add(prix)
        db.session.commit()
        return redirect(url_for("achl", _anchor=f"{aid}")) 
    
    except :
        return redirect("achat")
    # return redirect(url_for("achl", _anchor=f"{ze}")) 
# FIN AJOUTER DES PANIER{} 


# PARTIE MODIFIER


# MODIFIER USER{}
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = Profil.query.get(id)
    eude = Profil.query.all()
    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.age = request.form['age']
        for i in eude :
            if i == user :
                continue
            if i.last_name == user.last_name :
                flash("Email ou Mot de passe invalide")
                return redirect(url_for('update', id=id))
            else :
            
                for i in range (len(user.last_name)) :

                    if user.last_name[i] == "@" :
                        
                        if "moc.liamg" == user.last_name[:i:-1] and len(user.age)== 8 :

                            db.session.commit()
                            return redirect(url_for('index',id=id))
                        
                        else :

                            flash("Email ou Mot de passe invalide")
                            return redirect(url_for('update', id=id))
                   
                        
 
            
           
    flash("Email ou Mot de passe invalide")
    return render_template('miseajour.html', user=user)
# FIN MODIFIER USER{}



# MODIFIER MOIMEN{}
@app.route('/updater/<int:id>', methods=['GET', 'POST'])
def updater(id):
    user = Profil.query.get(id)
    eude = Profil.query.all()
    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name = user.last_name
        user.age = request.form['age']
        for i in eude :
            if i == user :
                continue
            if i.last_name == user.last_name :
                
                return redirect(url_for('update', id=id))
            else :
            
                for i in range (len(user.last_name)) :

                    if user.last_name[i] == "@" :
                        
                        if "moc.liamg" == user.last_name[:i:-1] and len(user.age)== 8 :

                            db.session.commit()
                            return redirect(url_for('useprid',id=id))
                        
                        else :

                            return redirect(url_for('updater', id=id))
                   
                        
 
            
           
   
    return render_template('updatpro.html', user=user)
# FIN MODIFIER MOIMEN{}


# PARTIE SUPPRIMER


# SUPPRIMER DU PANIER{} 
@app.route('/suppanier',methods = ["POST"])
def suppanier() :

    nom = request.form.get("nom")
    description = request.form.get("description")
    mail = request.form.get("mail")
    prix = request.form.get("prix")
    zerr = Userpanierezeze.query.all()
    
    print(mail,nom,description,prix)
    recy =[]
    for i in zerr :
        
        if i.mail == mail :
            if i.nom == nom and i.description == description :
                user = Userpanierezeze.query.filter_by(nom = nom, description = description , prix = prix, mail = mail).first()

                print(i.description,i.id,i.mail,i.nom,i.prix)
                zerre = Userpanierezeze.query.get(i.id)
                db.session.delete(zerre)
                db.session.commit()
                return redirect("/panieruser")

        
    return redirect("/panieruser")
# FIN SUPPRIMER DU PANIER{} 


# SUPPRIMER USER{} 
@app.route('/delete/<int:id>')
def erase(id) :

    data = Profil.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/admining')

# FIN SUPPRIMER USER{} 

# SUPPRIMER TOUTES LES  NotificapTIONS{} 
@app.route('/toutsu')
def toutsu() :

    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    data = Notificap.query.all()
    for i in range(len(data)):
        if data[i].mail == useru.last_name :
            db.session.delete(data[i])
            db.session.commit()
        
    
            
    return redirect("/useprid")
# FIN SUPPRIMER NotificapATION{} 
# SUPPRIMER NotificapATION{} 
@app.route('/deletenotif/<int:id>')
def deletenotif(id) :


    data = Notificap.query.get(id)
    db.session.delete(data)
    db.session.commit()
    


    # nom = request.form.get("nom")
    # description = request.form.get("description")
    # mail = request.form.get("mail")
    # prix = request.form.get("prix")
    # zerr = Notificap.query.all()
    
    # print(mail,nom,description,prix)
    # recy =[]
    # for i in zerr :
        
    #     if i.mail == mail :
    #         if i.nom == nom and i.description == description :
    #             user = Userpanierezeze.query.filter_by(nom = nom, description = description , prix = prix, mail = mail).first()

    #             print(i.description,i.id,i.mail,i.nom,i.prix)
    #             zerre = Userpanierezeze.query.get(i.id)
    #             db.session.delete(zerre)
    #             db.session.commit()
    #             return redirect("/useprid")

            
    return redirect("/useprid")
# FIN SUPPRIMER NotificapATION{} 

# SUPPRIMER ARTICLES{} 
@app.route('/deletearticles/<int:id>')
def ecraseart(id) :


    data = Maboutik.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect("/admining")
# FIN SUPPRIMER ARTICLES{} 















# import subprocess
# import phonenumbers

# def make_phone_call(phone_number):
#     # Vérifier si le numéro de téléphone est valide
#     if not phonenumbers.is_valid_number(phonenumbers.parse(phone_number, "FR")):
#         print("Numéro de téléphone invalide.")
#         return

#     # Former la commande d'appel téléphonique (exemple avec la commande 'echo')
#     command = f'echo "Appel à {phone_number}"'

#     # Exécuter la commande système
#     try:
#         subprocess.run(command, shell=True, check=True)
#         print(f"Appel réussi vers {phone_number}")
#     except subprocess.CalledProcessError as e:
#         print(f"Erreur lors de l'appel : {e}")

# # Remplacez le numéro de téléphone par celui que vous souhaitez appeler
# phone_number_to_call = '+223XXXXXXXX'  # Remplacez par le numéro Moov

# # Appeler la fonction pour lancer l'appel téléphonique
# make_phone_call(phone_number_to_call)


if __name__ == '__main__' :
    app.run(debug=True,port=5005)
