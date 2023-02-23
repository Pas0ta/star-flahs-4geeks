"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


# creacion de endpoints
# usuarios
@app.route('/user', methods=['GET'])
def handle_hello():

    users_query = User.query.all()
    results = list(map(lambda item: item.serialize(), users_query))

    response_body = {
        "msg": "ok",
        "results": results
    }
    response_body = {
        "msg": "aqui tu usuario "
    }

    return jsonify(response_body), 200


@app.route('/user/<int:user_id>/favoritos', methods=['GET'])
def user_fav(user_id):
    # query
    favoritos = Favoritos.query.filter_by(id_user=user_id).all()
    print(favoritos)
    response_body = {
        "msg": "tus favoritos ",
    }

    return jsonify(response_body), 200

# creacion personajes


@app.route('/personajes', methods=['GET'])
def todos_personajes():
    # query
    personajes_query = Personajes.query.all()

    results = list(map(lambda item: item.serialize(), personajes_query))
    print(results)
    response_body = {
        "msg": "planeta ok ",
        "result": results
    }

    return jsonify(response_body), 200

# creacion personajes individual


@app.route('/personajes/<int:personajes_id>', methods=['GET'])
def get_personajes(personajes_id):
    # query
    personaje = Personajes.query.filter_by(id=personajes_id).first()

    response_body = {
        "msg": "personajes ok ",
    }

    return jsonify(response_body), 200

    # creacion planetas


@app.route('/planetas', methods=['GET'])
def todos_planetas():
    # query
    planetas_query = Personajes.query.all()

    results = list(map(lambda item: item.serialize(), planetas_query))
    response_body = {
        "msg": "planetas ok ",
        "result": results
    }

    return jsonify(response_body), 200

# creacion personajes individual


@app.route('/planetas/<int:planetas_id>', methods=['GET'])
def planet_fav(planetas_id):
    # query
    planeta = Planetas.query.filter_by(id=planetas_id).first()

    response_body = {
        "msg": "personajes ok ",
    }

    return jsonify(response_body), 200

# post planetas


@app.route('/favoritos/<int:user_id>/planet/<int:planet_id>', methods=['POST'])
def añade_favoritos(planet_id, user_id):
    # query
    request_body = request.json

    planetas_query = Planetas.query.filter_by(id=planet_id,).first()
    favoritos_query = Favoritos.query.filter_by(id_user=user_id).first()

#  if planetas_query is None:
    planetas_id = Planetas(
        id=request_body["id"], nombre=request_body["nombre"])
    favoritos = Favoritos(id_user=user_id, id_planetas=planet_id)
    # db.session.add(planetas_id, favoritos)
    # db.session.commit()
    print(favoritos)
    response_body = {
        "msg": "añadido correctamente ",
    }

    return jsonify(response_body), 200
    # else:
    #     return jsonify({"msg": "Usuario ya existe"}), 400


@app.route("/login", methods=["POST"])
def login():

    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(email=email).first()
    print(user)
    if user is None:
        return jsonify({"msg": "Usuario no registrado"}), 404

    if email != user.email or password != user.password:
        return jsonify({"msg": "Bad email or password"}), 401
    

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

@app.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():

    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    user = User.query.filter_by(email = current_user).first()
    print(user)
    return jsonify(logged_in_as=current_user), 200




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
