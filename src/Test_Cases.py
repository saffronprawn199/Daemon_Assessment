import unittest
from main import merge_two_dataframe_tables, calculate_ranking_of_movies, apply_sorting_to_dataframe
import pandas as pd
from pandas.testing import assert_frame_equal


class DataTransformTestCases(unittest.TestCase):
    def test_merge_functionality(self):
        df1 = pd.DataFrame({'Animals': ['cat', 'dog'], 'id': [3, 4]})
        df2 = pd.DataFrame({'Owner': ['John', 'Pete'], 'id': [3, 4]})
        df_expected = pd.DataFrame({'Animals': ['cat', 'dog'],  'id': [3, 4], 'Owner': ['John', 'Pete']})
        df_result = merge_two_dataframe_tables(df1, df2, merge_id1='id', merge_id2='id')
        assert_frame_equal(df_result, df_expected)

    def test_ranking_calculation(self):
        df_result = pd.DataFrame({'averageRating': [2, 3, 4],
                                  'averageNumberOfVotes': [10, 40, 50],
                                   'numVotes': [10, 40, 50]})

        df_expected = pd.DataFrame({'averageRating': [2, 3, 4],
                                    'averageNumberOfVotes': [10, 40, 50],
                                    'numVotes': [10, 40, 50],
                                    'ranking': [2.0, 3.0, 4.0]})

        df_result['ranking'] = df_result.apply(lambda row: calculate_ranking_of_movies(row['averageRating'],
                                                                              row['averageNumberOfVotes'],
                                                                              row['numVotes']),
                                                                                axis=1)
        assert_frame_equal(df_expected, df_result)


    def test_sorting_functionality(self):
        df_result = pd.DataFrame({'averageRating': [2, 3, 4, 5],
                                  'averageNumberOfVotes': [10, 40, 50, 60],
                                  'numVotes': [10, 40, 50, 60],
                                  'ranking': [1.0, 2.0, 3.0, 4.0]})

        df_expected = pd.DataFrame({'averageRating': [5, 4, 3, 2],
                                    'averageNumberOfVotes': [60, 50, 40, 10],
                                    'numVotes': [60, 50, 40, 10],
                                    'ranking': [4.0, 3.0, 2.0, 1.0]})
        # Ensure expected index is also in the reverse order
        df_expected.index = [3.0, 2.0, 1.0, 0.0]

        df_result = apply_sorting_to_dataframe(df_result, column_sorted_by='ranking')
        assert_frame_equal(df_expected, df_result, check_index_type=False)


if __name__ == '__main__':
    unittest.main()
