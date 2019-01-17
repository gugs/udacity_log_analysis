
import psycopg2

DATABASE_NAME = "news"

#function defined to remove unecessary records or adjust useful data
def handle_data():
    db = psycopg2.connect(dbname=DATABASE_NAME)
    session = db.cursor()
    #removing data not used  
    session.execute("delete from log where path = '/'")
    session.execute("update log set path = replace(path, '/article/', '')")
    db.close()

#which are the most reads articles?
def top3_articles():
    
    output = [('Path','Count')]
    db = psycopg2.connect(dbname=DATABASE_NAME)
    session = db.cursor()
    #Query 
    session.execute("select path, count(*) as count from log group by path"+
                    " order by count desc limit 3 offset 1;")
    output += session.fetchall()
    db.close()
        
    return output

#Who are the most read writers?

def top5_articles_writers():
    
    output = [('Path','Count')]
    db = psycopg2.connect(dbname=DATABASE_NAME)
    session = db.cursor()
    #Using join between tables to uses the stats from log table 
    session.execute("select au.name, count(au.name) as count from authors"+
                    " au inner join articles a on au.id = a.author inner"+
                    " join log l on a.slug = l.path group by au.name"+
                    " order by count desc limit 4")
    output += session.fetchall()
    db.close()
    
    return output

#What days have reached more than 1% on requests with errors?

def access_error_stats():
    
    output = [('Day','Error', 'Amount of Access', 'Error Percentage')]
    db = psycopg2.connect(dbname=DATABASE_NAME)
    session = db.cursor()
    #Creating a view to break the query 
    session.execute("create or replace view incidence as select date(time),"+
                    " count(*) as count, (select count(*) from log) as total"+
                    " from log where status ='404 NOT FOUND' group by"+
                    " date(time) ORDER BY count DESC;")
    #Query to calculate the percentage
    session.execute("select i.date, i.count, i.total, (select"+
                    " (i.count/i.total)*100) as percentage from Incidence i")
    output += session.fetchall()
    db.close()
    
    return output

def print_list(list):
    for x in range(len(list)): 
        print list[x]


def main():
    
    print("which are the most reads articles?")
    print(top3_articles())
    print("Who are the most read writers?")
    print(top5_articles_writers())
    print("What days have reached more than 1% on requests with errors?")
    print(print_list(access_error_stats()))
    
if __name__ == "__main__":
    # execute only if run as a script
    handle_data()
    main()
    
    