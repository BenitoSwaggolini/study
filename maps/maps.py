from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        films_count: int = 0

        def yeah():
            nonlocal films_count
            films_count += 1

        return sum(map(lambda x: x if x['rating'] not in (0, yeah()) and x['country'] >= 2 else 0,
                       list_of_movies)) / films_count

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        return sum(map(lambda film: film['name'].count('и') if film['rating'] >= rating else 0, list_of_movies))
