from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template , redirect , request,url_for,flash,Response
from flask import render_template , redirect , request,url_for,flash,session ,Response
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
import os


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
class Notifica(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    
    quantite = db.Column(db.Integer,nullable = False)
    prix = db.Column(db.Integer,nullable = False)
    image = db.Column(db.String(100), unique = False , nullable = False)
    mail = db.Column(db.String(100), unique = False , nullable = False)
    

   
    def __init__(self,prix,quantite,image,mail):
        
        self.prix = prix
        self.quantite = quantite
        self.image = image
        self.mail = mail
        

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
            "mail": self.mail
            
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
class Panierz(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(100), unique = False , nullable = False)
    description = db.Column(db.String(100), unique = True , nullable = False)
    prix = db.Column(db.Integer,nullable = False)
    image = db.Column(db.String(100), unique = True , nullable = False)
   
    def __init__(self,nom,description,prix,image):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.image = image

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
            "image": self.image
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
class Boutiquez(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(100), unique = False , nullable = False)
    description = db.Column(db.String(100), unique = True , nullable = False)
    prix = db.Column(db.Integer,nullable = False)
    image = db.Column(db.String(100), unique = True , nullable = False)
    categorie = db.Column(db.String(100), unique = False , nullable = False)
   
    def __init__(self,nom,description,prix,image,categorie):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.image = image
        self.categorie = categorie


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
            "categorie": self.categorie
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





# PAYEMENT {}
@app.route('/Payement')
def Payement() :
    if 'utilisateur_id' in session:
        user = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    # user = Connecter.query.all()
    data = Userpaniere.query.all()
    # zee = Connecter.query.get(1)   
    frr = []
    ut = []
    etr = []
    
    for i in data : 
        if i.mail == user.last_name :
            frr.append(i)
            
            ut.append([i.nom,i.prix])
    pri = 0
    for i in frr :
        pri += i.prix
    
    az = len(frr)
    for i in frr :
        etr.append(i.image)
    po = 'a.jpeg'
    premier = [frr[0]]
    
    image = frr[0:4:1]
    
    er =[az,user,pri,ut,frr,premier,image]
 
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
#     data = Userpaniere.query.all()
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
@app.route('/panieruser')
def panieruserk():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    data = Userpaniere.query.all()
    Panier = Panierz.query.all()
    # zee = Connecter.query.get(1)
    user = Userpaniere.query.filter_by(mail = useru.last_name).first()
    
    frr = []
    imm = []
    
    for i in data : 
        if i.mail == useru.last_name :
            frr.append(i)
    
    
    pri = 0
    for i in frr :
        pri += i.prix
    az = len(frr)
    er =[az,user,pri]
    az = len(frr)
    er =[az,frr,pri]
    return render_template('panieruser.html',user = er)
    # return render_template('panieruser.html',user = [user])
# FIN PANIER {}


# PUBLICATION {}
@app.route('/achat')
def achl():
    if 'utilisateur_id' in session:
        user = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    aer = Boutiquez.query.all()
    # addsac = []
    # for i in aer :
    #     print(i.nom)
    #     for le in " ".join([i]) :

    #         if 'sac' or 'Sac' or 'SAC':
    #             addsac.append(i)
    # for i in addsac :
    #     print(i)
    data = Userpaniere.query.all()
    # zee = Connecter.query.get(1)   
    frr = []

    for i in data : 
        if i.mail == user.last_name :
            frr.append(i)
   
    sac = []
    for i in aer:
        if i.categorie == "Sac" :
            sac.append(i)
    az = len(frr)
    vetement = []
    for i in aer:
        if i.categorie == "Vetement" :
            vetement.append(i)
    az = len(frr)
    fourniture = []
    for i in aer:
        if i.categorie == "Fourniture" :
            fourniture.append(i)
    az = len(frr)
   
    er =[az,aer,sac,vetement,fourniture]
    
    return render_template('achat.html',ae = er)
# FIN PUBLICATION {}


# PROFIL USER {}
@app.route('/useprid')
def useprid():
    if 'utilisateur_id' in session:
        user = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    data = Userpaniere.query.all()
    
       
    frr = []

    
    for i in data : 
        if i.mail == user.last_name :
            frr.append(i)
   
    
    az = len(frr)

    frrno = Notifica.query.all()
    notif = []
    for i in frrno : 
        if i.mail == user.last_name :
            notif.append(i)

    er =[az,user,notif]
 

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
    profilp = Panierz.query.all()
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
    
 
        
        
    profil = Boutiquez.query.all()
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
@app.route('/envoyer_email', methods=['POST'])
def envoyer_email():
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

        return redirect("/home")
# FIN ENVOYER MAIL


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
        prix = request.form['prix']
        image = request.form['image']
        quantite = request.form['quantite']
        mail = oiuy.last_name
        notif = Notifica(prix = prix, quantite = quantite, image = image, mail = mail)
        
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
        
        # data = Userpaniere.query.all()
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
        
        # notif = Notifica(prix = prix, image = image, quantite = quantite, mail = mail)
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

    data = Userpaniere.query.all()
 
    
    frr = []
    imm = []
    pop = []
    calvo = 0
    for i in data : 
        if i.mail == user.last_name :
            frr.append(i)
            calvo += i.prix 
            imm.append([str(i.nom),str(i.prix)+" FCFA"])
    
    for i in imm :
        pop.append(" -#- ".join(i))
             

    mepo = " /---/ ".join(pop)
    contenu = f"COMMANDE DE {user.last_name} \n\n\n{mepo} \n\n\nCOUT TOTAL : {calvo} FCFA"
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

    data = Userpaniere.query.all()
 
    
    frr = []
    imm = []
    pop = []
    calvo = 0
    for i in data : 
        if i.mail == user.last_name :
            frr.append(i)
            calvo += i.prix 

            imm.append([str(i.nom),str(i.prix)+" FCFA"])
    
    for i in imm :
        pop.append(" -#- ".join(i))

    mepo = " /---/ ".join(pop)
    contenu = f"VOTRE COMMANDE SUR BLAY LIBRARY \n\n\n{mepo} \n\n\nCOUT TOTAL : {calvo} FCFA"
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
#         data = Userpaniere.query.all()
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


# PARTIE AJOUTER DES ARTICLES{}
@app.route('/objet',methods = ["POST"])
def objet(): 
    
    try :
        nom = request.form.get("nom")
        description = request.form.get("description")
        prix = request.form.get("prix")
        image = request.form.get("image") 
        print('recu1')      
        categorie = request.form.get('selectOptione')
        print('recu2',categorie)      

        pani = Boutiquez(nom = nom, description = description , prix = prix, image = image, categorie = categorie)
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


# AJOUTER DES PANIER{}
@app.route('/new',methods = ["POST"])
def new():
    zee = Connecter.query.get(1)
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    user = Profil.query.filter_by(last_name = useru.last_name).first()
    nom = request.form.get("nom")
    desc = request.form.get("desc")
    image = request.form.get("image")
    prix = request.form.get("prix")
    mail = user.last_name
    user = Userpaniere.query.filter_by(nom = nom, description = desc , prix = prix, mail = mail).first()
    if user:
        
        return redirect("/achat")
    prix = Userpaniere(nom = nom, description = desc , prix = prix, mail = mail,image=image)
    db.session.add(prix)
    db.session.commit()
    return redirect("/achat")
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
    zerr = Userpaniere.query.all()
    
    print(mail,nom,description,prix)
    recy =[]
    for i in zerr :
        
        if i.mail == mail :
            if i.nom == nom and i.description == description :
                user = Userpaniere.query.filter_by(nom = nom, description = description , prix = prix, mail = mail).first()

                print(i.description,i.id,i.mail,i.nom,i.prix)
                zerre = Userpaniere.query.get(i.id)
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

# SUPPRIMER TOUTES LES  NOTIFICATIONS{} 
@app.route('/toutsu')
def toutsu() :

    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    data = Notifica.query.all()
    for i in range(len(data)):
        if data[i].mail == useru.last_name :
            db.session.delete(data[i])
            db.session.commit()
        
    
            
    return redirect("/useprid")
# FIN SUPPRIMER NotificaATION{} 
# SUPPRIMER NotificaATION{} 
@app.route('/deletenotif/<int:id>')
def deletenotif(id) :


    data = Notifica.query.get(id)
    db.session.delete(data)
    db.session.commit()
    


    # nom = request.form.get("nom")
    # description = request.form.get("description")
    # mail = request.form.get("mail")
    # prix = request.form.get("prix")
    # zerr = Notifica.query.all()
    
    # print(mail,nom,description,prix)
    # recy =[]
    # for i in zerr :
        
    #     if i.mail == mail :
    #         if i.nom == nom and i.description == description :
    #             user = Userpaniere.query.filter_by(nom = nom, description = description , prix = prix, mail = mail).first()

    #             print(i.description,i.id,i.mail,i.nom,i.prix)
    #             zerre = Userpaniere.query.get(i.id)
    #             db.session.delete(zerre)
    #             db.session.commit()
    #             return redirect("/useprid")

            
    return redirect("/useprid")
# FIN SUPPRIMER NotificaATION{} 

# SUPPRIMER ARTICLES{} 
@app.route('/deletearticles/<int:id>')
def ecraseart(id) :


    data = Panierz.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect("/admining")
# FIN SUPPRIMER ARTICLES{} 

if __name__ == '__main__' :
    app.run(debug=True,port=5000)
