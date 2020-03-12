# The rules are simple. Given a 52 card deck, expose the top card
# For each of the next 51 cards, guess whether the card will be greater
# or less than the previous card
# We will always guess smart. For example, if a King (12) is the previous card,
# we will guess lower
# Note: aces(0) are considered low
# Note #2: We lose ties
# The question: how many points can we expect to score
# What strategies (card counting) can improve out score, and by how much?

import random

# Naive approach: No memory, just based on the last card
num_iterations = 40000  # Change to modify the number or iterations
total_score = 0

for i in range(num_iterations):
    deck = [i % 13 for i in range(52)]  # 52 cards, each numbered, 0 - 12
    random.shuffle(deck)

    prev_card = deck.pop()
    score = 0
    while deck:
        guess_higher = prev_card <= 6  # True if we are going to guess "HIGHER"
        if guess_higher and deck[-1] > prev_card:
            score += 1
        if not(guess_higher) and deck[-1] < prev_card:
            score += 1
        prev_card = deck.pop()
    total_score += score


# +/- approach approach:
# Note: In the previous version, we had an issue if the previous card was a 6
# There are 6 cards above a 6 (7, 8, 9, 10, 11, 12) and 6 below (0, 1, 2, 3, 4, 5)
# Note: We want to make a good decision in this case
# We track how many "high" cards appear (7, 8, 9, 10, 11, 12) and how many "low" cards appear (0, 1, 2, 3, 4, 5)
# We assign high cards +1 and low cards -1
# If we see a 6 and the count is +, then we should guess "lower" because we have expended high cards, leaving low cards in the deck
# If we see a 6 and the count is -, we do the opposite
# If count is 0, we have to guess
# Note: A human can easily track this count. Thus, this is a viable human approach

total_score_plus_minus = 0
for i in range(num_iterations):
    deck = [i % 13 for i in range(52)]  # 52 cards, each numbered, 0 - 12
    random.shuffle(deck)


    prev_card = deck.pop()
    score = 0
    count = 0
    if prev_card < 6:
        count -= 1
    if prev_card > 6:
        count += 1
    while deck:
        guess_higher = False  # True if we are going to guess "HIGHER"
        if prev_card < 6:
            guess_higher = True
        elif prev_card > 6:
            guess_higher = False
        else:
            guess_higher = count < 0

        if guess_higher and deck[-1] > prev_card:
            score += 1
        if not(guess_higher) and deck[-1] < prev_card:
            score += 1
        
        prev_card = deck.pop()
        if prev_card > 6:
            count += 1
        elif prev_card < 6:
            count -= 1

    total_score_plus_minus += score

# The optimal approach:
# We remember the number of cards of each rank that are left in the deck
# Every time we see a card we update this information
# We then find the number of cards above and below the previous card's rank
# We choose the option which has the greater chance of success
# Note: this is optimal play, but would be difficult for a human to implement

total_score_optimal = 0
for i in range(num_iterations):
    deck = [i % 13 for i in range(52)]  # 52 cards, each numbered, 0 - 12
    random.shuffle(deck)


    prev_card = deck.pop()
    score = 0
    left = {}  # map ranks to number of cards per ranks
    for i in range(13):
        left[i] = 4
    left[prev_card] = 3

    while deck:
        num_higher = 0
        for i in range(prev_card + 1, 13):
            num_higher += left[i]
        num_lower = 0
        for i in range(0, prev_card):
            num_lower += left[i]
        guess_higher = num_higher > num_lower  # True if we are going to guess "HIGHER"

        if guess_higher and deck[-1] > prev_card:
            score += 1
        if not(guess_higher) and deck[-1] < prev_card:
            score += 1

        prev_card = deck.pop()
        left[prev_card] -= 1
    total_score_optimal += score

print("Naive Approach: ")
print(total_score/num_iterations)
print()
print("+/- Approach: ")
print(total_score_plus_minus/num_iterations)
print()
print("Optimal Approach: ")
print(total_score_optimal/num_iterations)
