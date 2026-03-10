from flask import Blueprint, request                 
                                                    
                                                     

from controllers.A_controllers import create_vg 
                                                      

C_routes = Blueprint('vg_routes', __name__)  
                                                      

@C_routes.route('/video game', methods=['POST'])       
def vg_post():                                   
    vg_data = request.json                        
    return create_vg(request.json)                 


from controllers.A_controllers import create_bn 
                                                      

C_routes = Blueprint('bn_routes', __name__)   
                                                     

@C_routes.route('/Boneco', methods=['POST'])      
def bn_post():                                   
    bn_data = request.json                         
    return create_bn(request.json)


from controllers.A_controllers import create_pv
                                                      

C_routes = Blueprint('pv_routes', __name__)   
                                                     

@C_routes.route('/Placa de video', methods=['POST'])      
def pv_post():                                   
    pv_data = request.json                         
    return create_pv(request.json)


from controllers.A_controllers import create_fo 
                                                      

C_routes = Blueprint('fo_routes', __name__)   
                                                     

@C_routes.route('/fone de ouvido', methods=['POST'])      
def fo_post():                                   
    fo_data = request.json                         
    return create_fo(request.json)


from controllers.A_controllers import create_cr 
                                                      

C_routes = Blueprint('cr_routes', __name__)   
                                                     

@C_routes.route('/Carro', methods=['POST'])      
def cr_post():                                   
    cr_data = request.json                         
    return create_bn(request.json)