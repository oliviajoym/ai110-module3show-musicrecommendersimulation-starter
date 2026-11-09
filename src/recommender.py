from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: int
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    target_energy: float
    acoustic_lvl: float
    valence_lvl: float

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Song]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")

    songs = []

    with open(csv_path, mode="r", newline="",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append(Song(
                id= int(row["id"]),
                title= row["title"].strip(),
                artist= row["artist"].strip(),
                genre= row["genre"].strip(),
                mood= row["mood"].strip(),
                energy= float(row["energy"]),
                tempo_bpm= int(row["tempo_bpm"]),
                valence= float(row["valence"]),
                danceability= float(row["danceability"]),
                acousticness= float(row["acousticness"]),
            ))
    print(f"Loaded songs:  {len(songs)}")

    return songs


def score_song(user_prefs: UserProfile, song: Song) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    if isinstance(user_prefs, dict):
        user_prefs = UserProfile(**user_prefs)
        
    score = 0.0
    reasons: List[str] = []

    # Genre: 3 points on an exact match
    if song.genre == user_prefs.favorite_genre:
        score += 3
        reasons.append("genre match (+3)")

    # Energy: up to 2 points, less as the difference grows
    energy_points = 2 * (1 - abs(song.energy - user_prefs.target_energy))
    score += energy_points
    reasons.append(f"energy closeness (+{energy_points:.2f})")

    # Valence: up to 1 point
    valence_points = 1 * (1 - abs(song.valence - user_prefs.valence_lvl))
    score += valence_points
    reasons.append(f"valence closeness (+{valence_points:.2f})")

    # Acousticness: up to 1 point
    acoustic_points = 1 * (1 - abs(song.acousticness - user_prefs.acoustic_lvl))
    score += acoustic_points
    reasons.append(f"acousticness closeness (+{acoustic_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: UserProfile, songs: List[Song], k: int = 6) -> List[Tuple[Song, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, "; ".join(reasons)))

    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
