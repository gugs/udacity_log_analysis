import psycopg2

DATABASE_NAME = "news"

# What are the most popular three articles of all time?


def top3_articles():

    output = [('Path', 'Count')]
    db = psycopg2.connect(dbname=DATABASE_NAME)
    session = db.cursor()
    # Query
    session.execute("select path, count(*) as count from log group by path" +
                    " order by count desc limit 3 offset 1;")
    output += session.fetchall()
    db.close()

    return output

# Who are the most read writers?


def top5_articles_writers():
    print "Who are the most read writers?"
    output = [('Path', 'Count')]
    db = psycopg2.connect(dbname=DATABASE_NAME)
    session = db.cursor()
    # Using join between tables to uses the stats from log table
    session.execute("select au.name, count(au.name) as count from authors au" +
                    " inner join articles a on au.id = a.author inner join" +
                    " log l on '/article/' || a.slug = l.path group by" +
                    " au.name order by count desc limit 4;")
    output += session.fetchall()
    db.close()

    return output

# What days have reached more than 1% on requests with errors?


def access_error_stats():

    print "What days have reached more than 1% on requests with errors?"
    output = [('Day', 'Error Percentage')]
    db = psycopg2.connect(dbname=DATABASE_NAME)
    session = db.cursor()
    # Creating a view to break the query
    session.execute("create or replace view error as select date(time)," +
                    " count(*) as count from log where status =" +
                    " '404 NOT FOUND' group by date(time) order by" +
                    " count desc;")
    session.execute("create or replace view successful as select date(time)," +
                    " count(*) as count from log where status ='200 OK' " +
                    "  group by date(time) order by count desc;")
    # Query to calculate the percentage
    session.execute("select e.date, (100 * cast(e.count as decimal) /" +
                    " cast(s.count as decimal)) as percentage from error e" +
                    " inner join successful s on e.date = s.date order" +
                    " by e.count desc;")
    output += session.fetchall()
    db.close()

    return output

# Function used to define string output format: Option1 to
# views and Option2 to Error


def print_list(option, list):
    if option == 'OPCAO1':
        for x in range(len(list)):
            print "%s views  %s " % list[x]
    elif option == 'OPCAO2':
        for x in range(len(list)):
            print "day %s error percentage %s" % list[x]
    else:
        print "Error: Option not found!"


def main():

    print
    print_list('OPCAO1', top3_articles())
    print
    print_list('OPCAO1', top5_articles_writers())
    print
    print_list('OPCAO2', access_error_stats())
    print

if __name__ == "__main__":
    # execute only if run as a script
    main()
