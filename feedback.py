def generate_feedback(answer):
    length = len(answer.split())

    strengths = []
    improvements = []

    if length > 30:
        strengths.append("Provided detailed response")
    else:
        improvements.append("Add more details and examples")

    if any(word in answer.lower() for word in ["project", "team", "developed"]):
        strengths.append("Included practical experience")
    else:
        improvements.append("Mention projects or real experiences")

    return strengths, improvements
