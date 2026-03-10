from models.B_models import Carro   
from db import db                       
import json                              
from flask import make_response          

def video_game(vg_data):           
    novo_vg = video_game(                 
        modelo=vg_data['modelo'],    
        marca=vg_data['marca'],       
        ano=vg_data['ano'],           
        preço=vg_data['preço']
    )
    db.session.add(novo_vg)          
    db.session.commit()                 
    response = make_response(         
        json.dumps({                     
            'mensagem': 'Jogo cadastrado com sucesso.',  
            'carro': novo_vg.json()   
        }, sort_keys=False)               
    )
    response.headers['content-Type'] = 'application/json'  
    return response
                     
def boneco(bn_data):           
    novo_bn = boneco(               
        preço=bn_data['preço'],     
        marca=bn_data['marca'],      
        ano=bn_data['ano']            
    )
    db.session.add(novo_bn)           
    db.session.commit()                 
    response = make_response(            
        json.dumps({                     
            'mensagem': 'Boneco cadastrado com sucesso.',  
            'carro': novo_bn.json()  
        }, sort_keys=False)             
    )
    response.headers['content-Type'] = 'application/json' 
    return response  
          
def placa_de_video(pv_data):           
    novo_bn = placa_de_video(               
        preço=pv_data['preço'],     
        marca=pv_data['marca'],
        modelo=pv_data['modelo'],      
        ano=pv_data['ano']            
    )
    db.session.add(novo_pv)           
    db.session.commit()                 
    response = make_response(            
        json.dumps({                     
            'mensagem': 'Placa de Video cadastrada com sucesso.',  
            'carro': novo_pv.json()  
        }, sort_keys=False)             
    )
    response.headers['content-Type'] = 'application/json' 
    return response  

def fone_de_ouvido(fo_data):           
    novo_bn = fone_de_ouvido(               
        preço=fo_data['preço'],     
        marca=fo_data['marca'],
        modelo=fo_data['modelo'],      
        ano=fo_data['ano']              
    )
    db.session.add(novo_fo)           
    db.session.commit()                 
    response = make_response(            
        json.dumps({                     
            'mensagem': 'Placa de Video cadastrada com sucesso.',  
            'carro': novo_fo.json()  
        }, sort_keys=False)             
    )
    response.headers['content-Type'] = 'application/json' 
    return response

def carro(cr_data):           
    novo_bn = carro(               
        preço=cr_data['preço'],     
        marca=cr_data['marca'],
        modelo=cr_data['modelo'],     
        ano=cr_data['ano'],
        cor=cr_data['cor']              
    )
    db.session.add(novo_cr)           
    db.session.commit()                 
    response = make_response(            
        json.dumps({                     
            'mensagem': 'Placa de Video cadastrada com sucesso.',  
            'carro': novo_cr.json()  
        }, sort_keys=False)             
    )
    response.headers['content-Type'] = 'application/json' 
    return response                      