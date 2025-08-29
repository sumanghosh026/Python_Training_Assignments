# Create an empty list to store scores.
scores = []

# Append the scores: 85, 90, 78, 92, 88
scores.append(85)
scores.append(90)
scores.append(78)
scores.append(92)
scores.append(88)
print("Scores after appending:", scores)

#Insert the score 80 at index 5
scores.insert(5, 80)
print("Scores after inserting 80 at index 5:", scores)

# Remove the score 92 from the list
scores.remove(92)
print("Scores after removing 92:", scores)

# Sort the scores in ascending order
scores.sort()
print("Scores after sorting:", scores)

#Reverse the list
scores.reverse()
print("Scores after reversing:", scores)

#Find and print the maximum and minimum score
max_score = max(scores)
min_score = min(scores)
print("Maximum score:", max_score)
print("Minimum score:", min_score)

# Check if 90 is in the list
is_90_present = 90 in scores
print("Is 90 in the list?", is_90_present)

# Print the total number of scores
total_scores = len(scores)
print("Total number of scores:", total_scores)

#Slice and print the first three scores
first_three = scores[:3]
print("First three scores:", first_three)

# Find the last element from the list
last_element = scores[-1]
print("Last element in the list:", last_element)

#Replace the score at index 2 with a new score
scores[2] = 95
print("Scores after replacing index 2 with 95:", scores)

# Create a new copied list
copied_scores = scores.copy()
print("Copied list of scores:", copied_scores)
