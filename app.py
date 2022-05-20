import os

from flask import Flask, request, jsonify

from pizzabot_core.utils.parser import ParseError, Parser
from pizzabot_core.pizzabot import get_movement_instructions

app = Flask(__name__)

app.config['SECRET'] = os.environ.get('SECRET', '12345')


@app.route('/pizzabot', methods=['POST'])
def get_instructions():
    data = request.get_json()
    input_string = data.get('pizzabot', None)
    if input_string is None:
        return jsonify({'message': 'You must provide "pizzabot" key'}), 400

    try:
        size, points = Parser.parse_input_data(input_string)
    except ParseError as e:
        return jsonify({'message': e.args[0]}), 400

    success, result = get_movement_instructions(size[0], size[1], points, 'D')

    if not success:
        return jsonify({'message': result}), 400

    return jsonify({'instructions': ''.join(result)}), 200


if __name__ == '__main__':
    app.run()
