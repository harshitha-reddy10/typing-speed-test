import time
import random
sentences = [
    "Python is a powerful programming language.",
    "Typing speed tests help improve accuracy.",
    "Artificial Intelligence is shaping the future.",
    "Practice makes a person perfect.",
    "Data Science involves statistics and coding."
]
def typing_speed_test():
    sentence = random.choice(sentences)
    print("\n--- Typing Speed Test ---")
    print("Type this sentence:\n")
    print(sentence)
    print()
    input("Press Enter to start typing...")
    start_time = time.time()
    typed_text = input("\nNow type here:\n")
    end_time = time.time()
    time_taken = end_time - start_time
    time_taken = round(time_taken, 2)
    sentence_words = sentence.split()
    typed_words = typed_text.split()
    wpm = len(typed_words) / (time_taken / 60)
    correct = 0
    for i in range(min(len(sentence_words), len(typed_words))):
        if sentence_words[i] == typed_words[i]:
            correct += 1
    accuracy = (correct / len(sentence_words)) * 100
    print("\n--- Results ---")
    print(f"Time Taken: {time_taken} seconds")
    print(f"Your Speed: {round(wpm, 2)} words per minute")
    print(f"Accuracy: {round(accuracy, 2)}%")
typing_speed_test()
