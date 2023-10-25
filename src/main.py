import pandas as pd
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.getcwd())))
DATA_DIR = f'{ROOT_DIR}\\data'


def read_data(read_mode='tsv'):
    list_of_dataframes = []
    df_temp = None

    # List directories in the data directories folder
    directories = [d for d in os.listdir(DATA_DIR)]

    # Filter directories that end with '.tsv' - not the '.gz' directories
    tsv_directories = [d for d in directories if d.endswith('.tsv')]

    # Read relevant files into a list of pandas Dataframe objects
    for folder in tsv_directories:
        if read_mode == 'tsv':
            df_temp = pd.read_csv(f'{DATA_DIR}\\{folder}\\data.tsv', sep='\t', low_memory=False)
        elif read_mode == 'parquet':
            df_temp = pd.read_parquet(f'{DATA_DIR}\\{folder}\\data.parquet')

        print(f'Finished processing {DATA_DIR}\\{folder}')
        list_of_dataframes.append(df_temp)

    return list_of_dataframes, tsv_directories


def merge_two_dataframe_tables(df1,
                               df2,
                               merge_type="left",
                               merge_id1="tconst",
                               merge_id2="tconst"):

    merged_dataframe = pd.merge(df1, df2, how=merge_type, on=[merge_id1, merge_id2])
    return merged_dataframe


def calculate_ranking_of_movies(average_rating, average_number_of_votes, num_votes):
    ranking = ((num_votes / average_number_of_votes) * average_rating)
    return ranking


def apply_sorting_to_dataframe(df, column_sorted_by='ranking', ascending=False):
    df.sort_values(by=[column_sorted_by], ascending=ascending, inplace=True)
    return df


def main():

    # Read in data as parquet file, you can change this to "tsv" if preferred
    df_all, _ = read_data(read_mode='parquet')

    # Question A
    df = merge_two_dataframe_tables(df_all[2], df_all[6])

    # Insure values don't contain Nan values
    df['numVotes'] = df['numVotes'].fillna(0)
    df['averageRating'] = df['averageRating'].fillna(0)

    # Filter specifically on movies
    df = df.loc[df['titleType'] == 'movie']

    # Filter the votes to ensure that only cases with a minimum of 100 votes are considered.
    df = df[df["numVotes"] >= 100]

    # Get the average number of votes across all votes
    df['averageNumberOfVotes'] = df['numVotes'].mean()

    # Calculate the ranking of each movie
    df['ranking'] = df.apply(lambda row:
                        calculate_ranking_of_movies(row['averageRating'], row['averageNumberOfVotes'], row['numVotes']), axis=1)

    # Sort the movies in descending order to get the top results
    df = apply_sorting_to_dataframe(df)

    # Answer to Question A
    print("The Top 15 Movies are: ", df.head(n=15))

    # save result to csv file
    df_result = df.head(n=15)

    df_result.to_csv(f'{ROOT_DIR}\\result\\top_15_movies.csv', index=False)

    # Answer to Question B
    list_of_top_15_movies = df['primaryTitle'].tolist()[0:15]
    print("The following are the names of the top 15 movies: ", list_of_top_15_movies)


if __name__ == "__main__":
    main()
