from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

class ShkoloTweaksAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(self.app)
        self.create_tables()
        self.setup_routes()

    def create_tables(self):
        class Leaderboard(self.db.Model):
            id = self.db.Column(self.db.Integer, primary_key=True)
            name = self.db.Column(self.db.String(100), nullable=False)
            score = self.db.Column(self.db.Integer, nullable=False)

        self.Leaderboard = Leaderboard
        with self.app.app_context():
            self.db.create_all()

    def setup_routes(self):
        @self.app.route('/leaderboard', methods=['POST'])
        def add_or_update_entry():
            data = request.get_json()
            if not data or 'id' not in data or 'name' not in data or 'score' not in data:
                return jsonify({'error': 'Invalid data'}), 400

            with self.db.session() as session:
                entry = session.get(self.Leaderboard, data['id'])
                if entry:
                    entry.name = data['name']
                    entry.score = data['score']
                else:
                    entry = self.Leaderboard(id=data['id'], name=data['name'], score=data['score'])
                    session.add(entry)

                session.commit()
            return jsonify({'message': 'Entry added/updated successfully'})

        @self.app.route('/leaderboard', methods=['GET'])
        def get_leaderboard():
            limit = request.args.get('limit', default=10, type=int)
            entries = self.Leaderboard.query.order_by(self.Leaderboard.score.desc()).limit(limit).all()
            result = [{'id': entry.id, 'name': entry.name, 'score': entry.score} for entry in entries]
            return jsonify(result)

    def run(self):
        self.app.run()

if __name__ == "__main__":
    api = ShkoloTweaksAPI()
    api.run()
