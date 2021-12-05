card_list = []

class BingoCard:
    def __init__(self, bingo_card):
        self.card = bingo_card
        self.rows = [0,0,0,0,0] #Keep count of numbers marked in each row
        self.columns = [0,0,0,0,0]
        self.sum_of_unmarked = self.calculate_sum()

    def check_number(self, new_number):
        """Check if the number is on the card. If it is not, we return None. If it is, we update rows and columns, and
        subtract the number from the sum of unmarked numbers. Checks if the board is a winner, and return the 
        product of the number and the sum of unmarked numbers on the board. If it is not a winner, we return None"""
        for i in range(5):
            for j in range(5):
                if self.card[i][j] == new_number:
                    self.rows[i] += 1
                    self.columns[j] += 1
                    self.sum_of_unmarked -= int(new_number)
                    if 5 in self.rows or 5 in self.columns:
                        return int(new_number) * self.sum_of_unmarked
        return None

    def calculate_sum(self):
        sum = 0
        for i in range(5):
            for j in range(5):
                sum += int(self.card[i][j])
        return sum


def open_file():
    file_object = open("4dec.txt", "r")
    line_counter = 0
    for line in file_object:
        if (line_counter - 1) % 6 != 0: #Empty line each 6 lines
            if line_counter > 0:
                if (line_counter - 2) % 6 == 0: #First line of a new bingo card
                    new_row_list = []
                new_row = line.split()
                new_row_list.append(new_row)
                if len(new_row_list) == 5: #Last line of the bingo card. Append it to the list of bingo cards.
                    new_card = BingoCard(new_row_list)
                    card_list.append(new_card)
            else:
                bingo_numbers = line.split(",")
        line_counter += 1
    return bingo_numbers


def play_bingo(bingo_numbers):
    """Checks numbers until someone has won"""
    for num in bingo_numbers:
        for card in card_list:
            won = card.check_number(num)
            if won is not None:
                return won

def main():
    bingo_numbers = open_file()
    won = play_bingo(bingo_numbers)
    print(won)

main()