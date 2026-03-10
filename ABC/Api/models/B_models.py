from db import db                     
class video_game(db.Model):                 
    __tablename__ = 'Video_game'            

    id = db.Column(db.Integer, primary_key=True)         
    marca = db.Column(db.String(80), nullable=False)     
    ano = db.Column(db.Integer, nullable=False)          
    preco = db.Column(db.Integer, nullable=False)
    modelo = db.Column(db.String(80), nullable=False)
    def json(self):                                       
        return {
            'id': self.id,            
            'marca': self.marca,      
            'ano': self.ano,           
            'preço': self.preco,
            'modelo': self.modelo

        }
class boneco (db.Model):                
    __tablename__ = 'Boneco'             

    id = db.Column(db.Integer, primary_key=True)         
    marca = db.Column(db.String(80), nullable=False)      
    ano = db.Column(db.Integer, nullable=False)          
    preco = db.Column(db.Integer, nullable=False)
    def json(self):                                       
        return {
            'id': self.id,           
            'marca': self.marca,     
            'ano': self.ano,          
            'preço': self.preco
        }
class placa_de_video (db.Model):                  
    __tablename__ = 'Placa_de_video'             

    id = db.Column(db.Integer, primary_key=True)         
    modelo = db.Column(db.String(80),db.Integer , nullable=False)         
    ano = db.Column(db.Integer, nullable=False)          
    preco = db.Column(db.Integer, nullable=False)
    marca = db.Column(db.String(80) , nullable=False)
    def json(self):                                        
        return {
            'id': self.id,            
            'modelo': self.modelo,    
            'ano': self.ano,           
            'preço': self.preco,
            'marca': self.marca,
        }
class fone_de_ouvido (db.Model):                 
    __tablename__ = 'Placa_de_video_Nvidia'              

    id = db.Column(db.Integer, primary_key=True)          
    modelo = db.Column(db.String(80),db.Integer , nullable=False)        
    ano = db.Column(db.Integer, nullable=False)           
    def json(self):                                        
        return {
            'id': self.id,            
            'modelo': self.modelo,   
            'marca': self.marca, 
            'ano': self.ano,          
            'preço': self.preco
        }
class carro (db.Model):                  
    __tablename__ = 'Carro'             

    id = db.Column(db.Integer, primary_key=True)         
    modelo = db.Column(db.String(80),db.Integer ,nullable=False)        
    ano = db.Column(db.Integer, nullable=False)          
    cor = db.Column(db.String(80),nullable=False)
    marca = db.Column(db.String(80), nullable=False)
    def json(self):                                      
        return {
            'id': self.id,            
            'modelo': self.modelo,   
            'ano': self.ano,          
            'preço': self.preco,
            'cor': self.cor,
            'marca': self.marca,
        }