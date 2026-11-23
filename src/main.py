"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs
from tabulate import tabulate


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"favorite_genre": "pop", "target_energy": 0.8, "acoustic_lvl": 0.2, "valence_lvl": 0.9}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    '''
    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song.title} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()
    '''
    rows = [
        [idx, song.title, f"{score:.2f}", explanation.replace("; ", "\n")]
        for idx, (song, score, explanation) in enumerate(recommendations, start=1)
    ]
    print("\nTop recommendations:\n")
    print(tabulate(rows, headers=["#", "Title", "Score", "Reasons"], tablefmt="grid"))

if __name__ == "__main__":
    main()
