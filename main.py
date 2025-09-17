movies = {
    "Action": ["Mad Max", "John Wick", "Die Hard"],
    "Comedy": ["The Mask", "Jumanji", "The Hangover"],
    "Drama": ["Forrest Gump", "The Pursuit of Happyness", "The Godfather"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"]
}

print("Welcome to the Movie Recommendation System 🎬")

print("Choose a genre:")
for i, genre in enumerate(movies.keys(), start=1):
    print(f"{i}. {genre}")

choice = int(input("Enter the number of your favorite genre: "))

genre_list = list(movies.keys())
selected_genre = genre_list[choice - 1]

print(f"\nYou chose: {selected_genre}")
print("Recommended movies for you:")
for movie in movies[selected_genre]:
    print("-", movie)
