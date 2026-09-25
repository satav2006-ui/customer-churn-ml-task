
from pathlib import Path
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = [
    "space mission satellite orbit rocket nasa astronaut",
    "rocket launch spacecraft planet astronomy telescope",
    "astronauts study galaxies and space exploration",
    "satellite communication orbit science mission",
    "baseball pitcher batter home run inning league",
    "the baseball team won the game with a home run",
    "pitcher struck out the batter in the final inning",
    "baseball season player batting average championship",
]
labels = [
    "sci.space", "sci.space", "sci.space", "sci.space",
    "rec.sport.baseball", "rec.sport.baseball",
    "rec.sport.baseball", "rec.sport.baseball"
]

model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), lowercase=True)),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42))
])
model.fit(texts, labels)

Path("model").mkdir(exist_ok=True)
joblib.dump(model, "model/text_classifier.joblib")
print("Saved model/text_classifier.joblib")
