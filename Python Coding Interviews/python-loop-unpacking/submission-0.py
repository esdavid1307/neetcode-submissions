from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:

    high_score = {}
    for name, score in scores:
        high_score[name] = score

    count = 0
    bestname = ""
    for name, score in high_score.items():
        if score > count:
            count = score
            bestname = name
    return bestname






# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
