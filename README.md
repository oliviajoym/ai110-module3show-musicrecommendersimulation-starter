# 🎵 Music Recommender Simulation

## Project Summary

This project is a small music recommender system. The goal is to have the system recommend songs that are geared towards the users preference.

## How The System Works

Real World music recommendations are based on a mix of collaborative and content-based filtering.

#### Content-Based Filtering

This is filtering based on the metadata and raw audio of a song. The metadata depends on the algorithm used and range from the song title to primary language. The raw audio of a song is where terms like danceability and energy come in. These terms reflect the sound of a song. The variables can be scored various ways an algorithm can find the best song for each user. Through content-based filttering, the best songs are found relying on the details and essense of songs.

#### Collaborative Filtering

Collaborative filtering relies on behavior of multiple users. It goes deeper than just saying that two users like the same song. It is finding the similar patterns in users who interact with the same song. If there is a pattern that user X and Y follow (like having that songs with similar songs on the same playlist), then the system can then recommend user Z the same song based on all the users combined interest and interactions.

\
With the mix of "what do people enjoy?" and "what is the song like?", recommenders can filter what songs to send to each unique user. 

Based on the dataset of songs given, features I will use in my system are energy, valence, genre, and acousticness. 

For the recommender, I will have two dataclases, `Song` and `UserProfile`. The information in the `Song` class includes the metadata of each song, like title, energy, and genre. For the `UserProfile` class, the infomation consist of the preferences of the users, like thier favorite genre and energy level.

The recommender will choose songs based on score rankings based on the user's profile and preference.

My simple system is on a linear point scale, which means that the score is determined by finding the difference in each feature (except genre since it's a string).

Point Scale
- Genre: 3pt
- Energy: 2pt
- Vibe (Valance) and Acoustics: 1pt


## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```


## Sample Recommendation Output

```
Loading songs from data/songs.csv...
Loaded songs:  18

Top recommendations:

Sunrise City - Score: 6.88
Because: genre match (+3); energy closeness (+1.96); valence closeness (+0.94); acousticness closeness (+0.98)

Gym Hero - Score: 6.46
Because: genre match (+3); energy closeness (+1.74); valence closeness (+0.87); acousticness closeness (+0.85)

Rooftop Lights - Score: 3.68
Because: energy closeness (+1.92); valence closeness (+0.91); acousticness closeness (+0.85)

Deep Current - Score: 3.64
Because: energy closeness (+1.92); valence closeness (+0.83); acousticness closeness (+0.89)

Night Drive Loop - Score: 3.47
Because: energy closeness (+1.90); valence closeness (+0.59); acousticness closeness (+0.98)

```


## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users


## Limitations and Risks

The one big limitation is that I did the scoring in linear and didn't do more in depth scoring.




