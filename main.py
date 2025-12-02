# main.py

def summarize_adoptions(adoptions):
    summary = {}
    for animal in adoptions:
        summary[animal] = summary.get(animal, 0) + 1
    return summary
