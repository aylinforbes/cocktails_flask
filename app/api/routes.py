from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Cocktail, cocktail_schema, cocktails_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee': 'haw'}

# Insert cocktail into database
@api.route('/cocktails', methods = ['POST'])
@token_required
def create_cocktail_data(current_user_token):
    name = request.json['name']
    liquor = request.json['liquor']
    ingredients = request.json['ingredients']
    time = request.json['time']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    cocktail = Cocktail(name, liquor, ingredients, time, user_token = user_token )

    db.session.add(cocktail)
    db.session.commit()

    response = cocktail_schema.dump(cocktail)
    return jsonify(response)

# Retrieve all cocktails
@api.route('/cocktails', methods = ['GET'])
@token_required
def get_cocktails(current_user_token):
    a_user = current_user_token.token
    cocktails = Cocktail.query.filter_by(user_token = a_user).all()
    response = cocktails_schema.dump(cocktails)
    return jsonify(response)

# Retrieve a single cocktail
@api.route('/cocktails/<id>', methods = ['GET'])
@token_required
def get_single_cocktail(current_user_token, id):
    cocktail = Cocktail.query.get(id)
    response = cocktail_schema.dump(cocktail)
    return jsonify(response)

# Update cocktail info
# 'PUT' is the replace command
@api.route('/cocktails/<id>', methods = ['POST','PUT'])
@token_required
def update_cocktail(current_user_token,id):
    cocktail = Cocktail.query.get(id) 
    cocktail.name = request.json['name']
    cocktail.liquor = request.json['liquor']
    cocktail.ingredients = request.json['ingredients']
    cocktail.time = request.json['time']
    cocktail.user_token = current_user_token.token

    db.session.commit()
    response = cocktail_schema.dump(cocktail)
    return jsonify(response)

#Delete cocktail
@api.route('/cocktails/<id>', methods = ['DELETE'])
@token_required
def delete_cocktail(current_user_token, id):
    cocktail = Cocktail.query.get(id)
    db.session.delete(cocktail)
    db.session.commit()
    response = cocktail_schema.dump(cocktail)
    return jsonify(response)