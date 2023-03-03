class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        positive_indexes = []
        max_digit = -float('inf')
        for indx, digit in enumerate(input_list):
            if digit > 0:
                positive_indexes.append(indx)
            if max_digit < digit:
                max_digit = digit
        for indx in positive_indexes:
            input_list[indx] = max_digit
        return input_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        minimal, maximum = 0, len(input_list) - 1

        middle = int(abs((minimal - maximum)) // 2)
        while minimal < maximum:
            middle = int(abs((minimal - maximum)) // 2)
            if input_list[middle] == query:
                return middle
            if input_list[middle] < query:
                minimal = middle + 1
            else:
                maximum = middle - 1

        return middle
