import mysql.connector
from datetime import date
class Database:
    def __init__(self,mabase):
        
        try:
            self.con = mysql.connector.connect(user='root', 
                                               password='123456',
                                                host='localhost',
                                                database='stock')
        except mysql.connector.Error :
            print("Erreur base")

        self.cursor = self.con.cursor()
        
    def Nbrenr(self):
        self.cursor.execute("SELECT COUNT(*) FROM produit")
        num_rows = self.cursor.fetchone()[0]
        return num_rows
    
    def SelectImage(self) :
        self.cursor.execute("SELECT nom,prix,Image FROM produit")
        tout = self.cursor.fetchall()
        return tout
    def Ajouter(self,nom,description,Image,prix,quantite,seuil,id_ut,catProduit):
        dateE= date.today().strftime("%Y-%m-%d")
        dateS=""
        id=0
        self.cursor.execute("INSERT INTO produit(id,nom,description,Image,prix,quantite,seuil,dateE,dateS,id_ut,catProduit) VALUES({}, '{}','{}', '{}', {},{}, {}, '{}',NULL,2,'{}')".format(id,nom,description,Image,prix,quantite,seuil,dateE,catProduit))
        self.con.commit()
        
    def Supprimer(self,id):
        self.cursor.execute("DELETE FROM produit where id={}".format(id))
        self.con.commit()
    def Modifier(self,nom,description,Image,prix,quantite,seuil,catProduit,id):
        dateE= date.today().strftime("%Y-%m-%d")
        id_ut=1
        self.cursor.execute("UPDATE produit SET nom = '{}', description = '{}', Image = '{}', prix = {}, quantite = {}, seuil = {}, dateE = '{}', id_ut = {}, catProduit = '{}' WHERE id = {}".format(nom,description,Image,prix,quantite,seuil,dateE,id_ut,catProduit,id))
        self.con.commit()
    def Entree(self,quantite,id,prix):
        dateE= date.today().strftime("%Y-%m-%d")
        print ("UPDATE produit SET  dateE = '{}' , prix= ((prix*quantite)+{}*{})/({}+quantite) ,quantite = quantite+{} WHERE id = {}".format(dateE,quantite,prix,quantite,quantite,id))
        
        self.cursor.execute("UPDATE produit SET  dateE = '{}' , prix= ((prix*quantite)+{}*{})/({}+quantite) ,quantite = quantite+{} WHERE id = {}".format(dateE,quantite,prix,quantite,quantite,id))
        self.con.commit()
    def Sortie(self,quantite,id):
        dateS= date.today().strftime("%Y-%m-%d")
        self.cursor.execute("UPDATE produit SET quantite = quantite-{}, dateS = '{}' WHERE id = {}".format(quantite,dateS,id))
        self.con.commit()
    def Selectionnerid(self,id):
        self.cursor.execute("SELECT * FROM produit where id={}".format(id))
        Sid=self.cursor.fetchall()
        return Sid
    def Selectionnertout(self):
        self.cursor.execute("SELECT * FROM produit ")
        Tout=self.cursor.fetchall()
        return Tout
 