import pandas as pd
import random

class PokerHandMarkovModel:
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.possible_hands = list(transition_matrix.keys())

    def generate_hand_sequence(self, start_hand, num_steps):
        sequence = [start_hand]
        current_hand = start_hand

        for _ in range(num_steps - 1):
            next_hand = random.choices(self.possible_hands, weights=self.transition_matrix[current_hand])[0]
            sequence.append(next_hand)
            current_hand = next_hand

        return sequence

def build_transition_matrix_from_csv(csv_file):
    # Read data from the CSV file
    data = pd.read_csv(csv_file)

    hands = data.columns.tolist()

    #transition matrix
    transition_matrix = {hand: [0] * len(hands) for hand in hands}

    # Calculate transition probabilities based on hand frequencies
    for hand in hands:
        total_count = data[hand].sum()
        for next_hand in hands:
            transition_matrix[hand][hands.index(next_hand)] = data[next_hand].sum() / total_count

    return transition_matrix

# Example usage
if __name__ == "__main__":
    # Read data from your CSV file (replace 'your_data.csv' with the actual file name)
    csv_file = "your_data.csv"
    transition_matrix = build_transition_matrix_from_csv(csv_file)

    pokerbot_model = PokerHandMarkovModel(transition_matrix)

    # Generate a sequence of poker hands starting from High Card
    generated_sequence = pokerbot_model.generate_hand_sequence(start_hand="High Card", num_steps=5)
    print("Generated hand sequence:", " -> ".join(generated_sequence))
