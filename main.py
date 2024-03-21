
from participant import Participant
  # Correct import statement

def calculate_score(participants):
    scores = []
    for participant in participants:
        score = participant.calculate_score()
        scores.append({'name': participant.name, 'score': score})
    sorted_scores = sorted(scores, key=lambda x: (-x['score'], x['name']))
    return sorted_scores

if __name__ == "__main__":
    participants = [
        Participant("Habanero Hillary", 5, 17, 11),
        Participant("Big Bob", 20, 4, 11)
    ]

    scoreboard = calculate_score(participants)
    print(scoreboard)

