import time
from concurrent import futures
from cassandra.cluster import Cluster
from random import randint

MAX_WORKERS = 30
CASSANDRA_HOST = '127.0.0.1'
CASSANDRA_PORT = 32770
CASSANDRA_KEYSPACE = 'colisiontest'
CYCLE_PER_THREAD = 1000

cluster = Cluster(
    [CASSANDRA_HOST],
    port=CASSANDRA_PORT)

#auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
#cluster = Cluster(auth_provider=auth_provider, protocol_version=2)

session = cluster.connect(CASSANDRA_KEYSPACE)

def uuid_insert(wks):
    rand = randint(0,20)
    time.sleep(rand)
    t0 = time.time()
    for num in range(0, CYCLE_PER_THREAD):
        #time.sleep(randint(0,20))
        #todo: call select uuid() from colisiontest.testeuuid limit 1; Then insert ...  IF NOT EXISTS
        session.execute("INSERT INTO {}.testeuuid(universal_id, moment) VALUES(uuid(), unixTimestampOf(now()));".format(CASSANDRA_KEYSPACE))
    elapsed = time.time() - t0
    msg = '\n Thread {} started sleep {} ;call {} inserts in {:.2f}s'.format(wks, rand, CYCLE_PER_THREAD, elapsed)
    print(msg)
    return msg

def uuid_insert_many():
    wks = list(range(MAX_WORKERS))
    t0 = time.time()
    with futures.ThreadPoolExecutor(MAX_WORKERS) as executor:
        res = executor.map(uuid_insert, wks)
    elapsed = time.time() - t0
    return elapsed

def main(uuid_insert_many):
    elapsed = uuid_insert_many()
    msg = '\n Total Time {:.2f}s'
    print(msg.format(elapsed))


if __name__ == '__main__':
    main(uuid_insert_many)


#CREATE KEYSPACE colisiontest
#WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };

#use colisiontest;

#CREATE TABLE colisiontest.testeuuid(
 #   universal_id uuid primary key,
  #                            moment timestamp);


#select * from colisiontest.testeuuid;


########################################################################################################
#Env execution: Win10 64bits; 16GB mem; i7
#Cassandra Docker https://hub.docker.com/r/spotify/cassandra/

#No colision
    #Thread 22 started sleep 0 ;call 1000 inserts in 4.02s
    #Thread 20 started sleep 1 ;call 1000 inserts in 5.33s
    #Thread 15 started sleep 2 ;call 1000 inserts in 5.94s
    #Thread 2 started sleep 3 ;call 1000 inserts in 6.63s
    #Thread 21 started sleep 3 ;call 1000 inserts in 6.64s
    #Thread 1 started sleep 3 ;call 1000 inserts in 6.68s
    #Thread 17 started sleep 4 ;call 1000 inserts in 6.79s
    #Thread 4 started sleep 4 ;call 1000 inserts in 6.86s
    #Thread 14 started sleep 4 ;call 1000 inserts in 6.95s
    #Thread 19 started sleep 5 ;call 1000 inserts in 6.37s
    #Thread 27 started sleep 5 ;call 1000 inserts in 6.43s
    #Thread 5 started sleep 7 ;call 1000 inserts in 6.07s
    #Thread 12 started sleep 8 ;call 1000 inserts in 5.81s
    #Thread 7 started sleep 8 ;call 1000 inserts in 5.85s
    #Thread 9 started sleep 8 ;call 1000 inserts in 5.87s
    #Thread 18 started sleep 9 ;call 1000 inserts in 5.27s
    #Thread 8 started sleep 10 ;call 1000 inserts in 4.81s
    #Thread 25 started sleep 11 ;call 1000 inserts in 4.33s
    #Thread 24 started sleep 12 ;call 1000 inserts in 3.88s
    #Thread 13 started sleep 13 ;call 1000 inserts in 3.53s
    #Thread 0 started sleep 15 ;call 1000 inserts in 3.48s
    #Thread 16 started sleep 16 ;call 1000 inserts in 4.34s
    #Thread 28 started sleep 17 ;call 1000 inserts in 4.72s
    #Thread 3 started sleep 17 ;call 1000 inserts in 4.76s
    #Thread 29 started sleep 17 ;call 1000 inserts in 4.79s
    #Thread 10 started sleep 17 ;call 1000 inserts in 4.90s
    #Thread 6 started sleep 18 ;call 1000 inserts in 4.75s
    #Thread 23 started sleep 18 ;call 1000 inserts in 4.84s
    #Thread 11 started sleep 19 ;call 1000 inserts in 4.38s
    #Thread 26 started sleep 20 ;call 1000 inserts in 4.01s

#Total Time 24.03s
    #Cassandra select count(*) from colisiontest.testeuuid;
    #30000 rows: