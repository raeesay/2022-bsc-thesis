import networkx as nx
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2

# create directed graph based on twitter mentions

def create_directed_graph(data):
    g = nx.from_pandas_edgelist(data, source='lower',
                                target='lower-2',
                                create_using=nx.DiGraph())
    return g


# load data locally

def local_data():
    # load .csv file
    data = pd.read_csv('./twitter_data.csv')
    data = data.drop_duplicates(keep='last')

    # creating digraph
    g = create_directed_graph(data)
    return g


# load data remotely via PostgreSQL

def remote_data():
    print('Please enter your credentials.')
    user = input('Please enter your username: ')
    password = input('Please enter your password: ')
    # creating a string with parameters to connect to the database
    # note: please use your given credentials (replace user and password)
    conn_string = "host='adrastea.ifi.uni-heidelberg.de' dbname='ryousaf' user='" + user + "' password='" + password + "'"

    # print the connection string used to connect
    print("Connecting to database\n	->%s" % (conn_string))

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # query used to retrieve table with two columns
    # the first column contains twitter users (twitter_name) mentioning users in column2 (mentions)
    sql = '''with cte as (
                        select u.twitter_name, REGEXP_MATCHES(t.txt, '@([A-Za-z0-9_]+)', 'g') as mentions
                        from tweet as t, twitter_user as u
                        where t.author_id=u.id
                    )
                    select LOWER(twitter_name), LOWER(unnest(mentions))
                    from cte'''

    # dataframe which uses the queried data
    data = sqlio.read_sql_query(sql, conn)
    # close connection to database
    conn = None

    # creating digraph
    g = create_directed_graph(data)
    return g
