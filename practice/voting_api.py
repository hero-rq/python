from flask import Flask, request, jsonify

app = Flask(__name__)

votes = {}  # dictionary to store votes, with candidate names as keys and vote counts as values

@app.route('/vote', methods=['POST'])
def submit_vote():
    # get the candidate name from the request data
    data = request.get_json()
    candidate = data['candidate']

    # increment the vote count for the candidate
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1

    return jsonify({'success': True}), 201

@app.route('/results', methods=['GET'])
def get_results():
    # return the current vote counts
    return jsonify(votes)

if __name__ == '__main__':
    app.run()
