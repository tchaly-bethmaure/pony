from pony.orm import *
import hashlib

db = Database()
db.bind('mysql', host='127.0.0.1', user='root', passwd='', db='pony_test')

class Utilisateur(db.Entity):
	mail = PrimaryKey(str)
	nom = Required(str)
	prenom = Required(str)
	password = Required(str)
	autorise = Required(bool)
	hote = Required(bool)
	def obtenir_nom_entier(self):
		return "%s %s" % (self.nom, self.prenom)
db.generate_mapping(create_tables=True) 

@db_session
def ajouter_utilisateur(mail, nom, prenom, password, autorise,hote):
    Utilisateur(mail=mail, nom=nom, prenom=prenom, password=password, autorise=autorise,hote=hote)

m = hashlib.md5()
mail = raw_input("Mail : ")
m.update(raw_input("Password : "))
ajouter_utilisateur(mail, "test", "test", m.hexdigest(), True, False)