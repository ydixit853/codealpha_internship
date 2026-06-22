# hangman game - flask backend
# made by - YASH DIXIT
# date - 14 june 2026

from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # allows hangman.html to talk to this server

# 5 words list (same as your original python code)
words = ["python", "cricket", "mango", "bhopal", "music"]

# game state stored in memory
game = {}

def new_game():
    game["word"]    = random.choice(words)
    game["guessed"] = []
    game["tries"]   = 0

# start a game on server boot
new_game()

def build_state():
    word    = game["word"]
    display = [l if l in game["guessed"] else "_" for l in word]
    won     = all(l in game["guessed"] for l in word)
    lost    = game["tries"] >= 6
    return jsonify({
        "display":  display,        # e.g. ["p","_","t","h","_","n"]
        "guessed":  game["guessed"],
        "tries":    game["tries"],
        "won":      won,
        "lost":     lost,
        "word":     word if (won or lost) else None  # reveal only at end
    })

# GET /state  →  return current game state
@app.route("/state")
def state():
    return build_state()

# POST /guess  body: {"letter": "a"}  →  process guess, return new state
@app.route("/guess", methods=["POST"])
def guess():
    data   = request.get_json(silent=True) or {}
    letter = data.get("letter", "").strip().lower()

    # condition 1 - already guessed
    if not letter or letter in game["guessed"]:
        return jsonify({"error": "already guessed or invalid"}), 400

    game["guessed"].append(letter)

    # condition 2 - correct  /  condition 3 - wrong
    if letter not in game["word"]:
        game["tries"] += 1

    return build_state()

# POST /new  →  reset and start a fresh game
@app.route("/new", methods=["POST"])
def restart():
    new_game()
    return build_state()

if __name__ == "__main__":
    print("\n  Hangman server running!")
    print("  Open hangman.html in your browser\n")
    app.run(debug=True, port=5000)