from flask import Flask, jsonify, request
from models import db, User, Character, Favorite_character, Planet, Favorite_planet
from flask_migrate import Migrate

app = Flask(__name__)
db.init_app(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
Migrate(app, db)

@app.route('/people', methods=['GET'])
def home():
    return '<h1>Holi </h1>'

@app.route('/people/<int:people_id>', methods=['GET'])
def get_people_id():
    return '<h1>Holi </h1>'

@app.route('/planets', methods=['GET', 'POST'])
def get_planets():
 if request.method == "POST":
        data = request.get_json()
        planet = Planet()

        if data:
            name = data["name"]
            description = data["description"]
            lenght = data["lenght"]
            diameter = data["diameter"]
            rotation_period = data["rotation_period"]
            orbital_period = data["orbital_period"]
            gravity = data["gravity"]
            population = data["population"]
            climate = data["climate"]
            terrain = data["terrain"]
            surface_water = data["surface_water"]

            planet = Planet(
                name=name,
                description=description,
                lenght=lenght,
                diameter=diameter,
                rotation_period=rotation_period,
                orbital_period=orbital_period,
                gravity=gravity,
                population=population,
                climate=climate,
                terrain=terrain,
                surface_water=surface_water
            )

            db.session.add(planet)
            db.session.commit()

            return jsonify({
               "message": "Planet added successfully",
                "planet":planet.serialize()     
            }), 201
        if request.method == "GET":
            planets = Planet.query.all()
            planets = list(map(lambda planet: planet.serialize(), planets))
            
            return jsonify(planets), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planets_id():
    planet = Planet.query.filter_by(id=id).first()
    if not planet:
        return jsonify({"msg": "Planet not found"}), 404
    planet = list(map(lambda planet: planet.serialize(), planet))
    
    return (planet), 200

@app.route('/users', methods=['GET'])
def get_users():
    data = request.get_json()
    user = User()

    if request.method == "POST":
        if data:
            email = data["email"]
            existing_user = User.query.filter_by(email=email).first()
           
            if existing_user:
               return jsonify({"msg": "Email already registered"}), 400

            if email is not None:
               user.email = email
            else:
               return jsonify({"msg": "Email cannot be empty"}), 400
            
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]

            db.session.add(user)
            db.session.commit()

            return jsonify({
                    "user_id": user.id,
                    "user_first_name": user.first_name,
                    "user_last_name": user.last_name
            }), 201

    if request.method == "GET":
        users = User.query.all()
        users = list(map(lambda user: user.serialize(), users))

        return jsonify(users)

@app.route('/users/favorites', methods=['GET'])
def get_favorites():
     if request.method == "GET":
        favorite_character = Favorite_character.query.filter_by(user_id=user_id).all()
        favorite_character = list(map(lambda favorite_character:favorite_character.serialize(), favorite_character))
        favorite_planet = Favorite_planet.query.filter_by(user_id=user_id).all()
        favorite_planet = list(map(lambda favorite_planet:favorite_planet.serialize(), favorite_planet))
       
        return jsonify({"favorite_character": favorite_character, 
                        "favorite_planet": favorite_planet}), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['POST', 'DELETE'])
def post_favorite_planet_id():
    data = request.get_json()

    user_id = data.get("user_id")
    if not user_id:
        return jsonify({"msg": "user_id is required"}), 400

    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"msg": "User not found"}), 403
    
    planet_id = data.get("planet_id")
    if not planet_id:
        return jsonify({"msg": "character_id is required"}), 400

    planet = Planet.query.filter_by(id=planet_id).first()
    if not planet:
        return jsonify({"msg": "Character not found"}), 403


    favorite_planet = Favorite_planet()
    favorite_planet.user_id = data.get("user_id")
    favorite_planet.character_id = data.get("planet_id")
    favorite_planet.name = data.get("name")
    favorite_planet.type = data.get("type")
    
    db.session.add(favorite_planet)
    db.session.commit()

    return jsonify(
            {"Msg": "Favorite planet created successfully", }
        ), 201

@app.route('/favorite/planet/<int:planet_id>')
def delete_favorite_planet_id():
    favorite_planet = Favorite_planet.query.filter_by(id=id).first()
    if not favorite_planet:
        return jsonify({"msg": "Favorite planet not exist"}), 404
    
    db.session.delete(favorite_planet)
    db.session.commit()
    return jsonify(f"Favorite planet {id} deleted"), 200

@app.route('/favorite/people/<int:people_id>', methods=['POST', 'DELETE'])
def post_favorite_people_id():
    return '<h1>Holi </h1>'

if __name__ == '__main__':
    app.run(host='localhost', port=5050, debug=True)