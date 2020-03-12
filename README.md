# High Low Game
## Inspiration
One day I was playing cards with my friends, and we wondered what the expected score was for a game of "High Low." For those unfamilar the rules are simple.
<ol type="1">
  <li>
    Flip over the top card of the deck
  </li>
  <li>
    For each of the remaining cards:
    <ol>
      <li>
        Guess whether the card is higher or lower than the previous (face up) card
      </li>
      <li> 
        Flip over the card to check you guess
        <ul type="a">
          <li>
            If right: Add one to your scrore
          </li>
          <li>
            If wrong: Score remains the same
          </li>
        </ul>
      </li>
      <li>
        The current card becomes the next face up card
      </li>
    </ol>
  </li>
  <li>
    Record your score, if you so wish
  </li>
</ol> 
I wondered about the expected score for this game, and so I created this script

## What It Does
I simulate 40 000 trials of three different players playing the same High-Low game.
One player is like a normal human player. They choose "HIGHER" if the previous (face up) card is low and "LOWER" if the previous (face up) card is high. However, there are 13 ranks in a deck of card. Using Aces low, if a 7 is the face up card, we face a problem. There are 6 (A-6) cards below a 7 and 6 (8-K) cards above a 7. We have to guess.

The next player addresses this, while still being human-implementable. We track the number of high and low cards by assigning (-1) to cards A-6 and (+1) to cards 8-K, and keep a running count of the cards we've seen. For example if the sequence we've seen is A, 5, 9, 4, 2, the count would be (-1) + (-1) + 1 + (-1) + (-1) = -3. If the count is negative and the previous card is a 7, then we choose "HIGHER" because we have expended the lower cards. If the count is positive and the previous card is a 7, then we choose "LOWER" for similar reasons. Note that this strategy is feasable as only one number needs to be tracked. In fact, many card counters employ a [similar strategy](https://www.blackjack.org/blackjack-strategies/hi-lo-count/) to beat Blackjack.

The final player is perfectly optimal. We know that in a fresh deck there are 4 cards of each rank. We construct a dictionary storing how many of each rank remain in the deck. Everytime a card is exposed we decrement the dictionary entry of its rank. Then, when deciding whether to guess higher or lower, we count all the remaining cards higher than the previous (face up) card. We also count all the remaining cards lower the previous (face up) card. If there are more cards higher, we guess "HIGHER." Otherwise, we guess "LOWER"
## How I Built It
I used Python to simulate 40 000 trials of each method and comapared their average results.
## Challenges I Ran Into
As the number of trials increased, so did the amount to time Python took to process it. For the final optimized player, I used a hash-table (dictionary) to optimize the time complexity.
## Results:
As expected, the Naive (Normal) player performed worse than the Human-Best player, who played worse than the optimized player. However, the Naive strategy was much better than I thought it would be. The results are summarize below
| Player        | Average Score |
| ------------- |:-------------:| 
| Normal        | 36.9      | 
| Human-Best    | 37.2      |  
| Perfect n     | 37.7      | 
## What's Next
More statistical analysis of the data. I would be interested in other measures of central tendancy such as the median or mode, as well as measures of spread such as the standard deviation. This data could also be nicely visualized in a graph
