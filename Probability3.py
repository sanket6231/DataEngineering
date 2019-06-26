# Pack of cards contains total 52 cards
total_cards = 52

# There are total 4 ace cards
ace_cards = 4
king_cards = 4

# Probability of drawing an ace from pack of cards
p1 = ace_cards / total_cards

# After drawing king card on first row Probability is
p2 = king_cards / (total_cards - 1)

# So the final probability is
p = p1 * p2

print('Probability = ', p)

