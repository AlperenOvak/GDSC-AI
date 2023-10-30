# Get valid exam scores from the user
scores = []
while True:
    try:
        score = float(input("Enter an exam score (0-100, or -1 to finish): "))
        if score == -1:
            break
        if score < 0 or score > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
        else:
            scores.append(score)
    except ValueError:
        print("Invalid input. Please enter a numeric score.")

# Calculate the average score
if len(scores) == 0:
    average_score = 0
else:
    average_score = sum(scores) / len(scores)

# Determine the final letter grade
if 90 <= average_score <= 100:
    letter_grade = "AA"
elif 85 <= average_score < 90:
    letter_grade = "BA"
elif 80 <= average_score < 85:
    letter_grade = "BB"
elif 70 <= average_score < 80:
    letter_grade = "CB"
elif 60 <= average_score < 70:
    letter_grade = "CC"
elif 50 <= average_score < 60:
    letter_grade = "DC"
elif 40 <= average_score < 50:
    letter_grade = "DD"
else:
    letter_grade = "FF"

# Display the results
print(f"Average Score: {average_score:.2f}")
print(f"Final Letter Grade: {letter_grade}")