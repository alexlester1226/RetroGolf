
class User:
    def __init__(self):
        data = self.get_info()
        self.coins = int(data[0][0])
        self.clubs = [int(data[0][1]), int(data[0][2]), int(data[0][3]), int(data[0][4]), int(data[0][5])]
        self.caddy = int(data[0][6])
        self.won = [self.str_to_bool(data[1][0]), self.str_to_bool(data[1][1]), self.str_to_bool(data[1][2]), self.str_to_bool(data[1][3]), self.str_to_bool(data[1][4]), self.str_to_bool(data[1][5]), self.str_to_bool(data[1][6])]

    def get_info(self):
        file_path = "user.txt"
        # Initialize an empty list to store the 2D array
        data = []

        # Open the file and read line by line
        with open(file_path, 'r') as file:
            for line in file:
                # Remove any trailing whitespace or newline characters
                line = line.strip()
                # Split the line by commas and append it to the data list
                data.append(line.split(','))

        return data

    def str_to_bool(self, s):
        return s.lower() == "true"


if __name__ == '__main__':
    menu = User()
