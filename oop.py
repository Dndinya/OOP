def calculate_score(participants):
    scores = []
    for participant in participants:
        score = participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2
        scores.append({'name': participant['name'], 'score': score})
    sorted_scores = sorted(scores, key=lambda x: (-x['score'], x['name']))
    return sorted_scores

# Example usage:
participants = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

scoreboard = calculate_score(participants)
print(scoreboard)
