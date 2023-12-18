def get_year_list(start_year:int, end_year:int) -> list[int]:
    """   
    Generates a list of years starting from "start_year"
    and ending with "end_year", inclusive.

    Args:
        start_year (int): The first year to include in the list (inclusive).
        end_year (int): The last year to include in the list (inclusive).

    Returns:
        list: A list of integers representing years from start_year to end_year.
    """
    year_list = [year for year in range(start_year, end_year+1)]

    return year_list

    