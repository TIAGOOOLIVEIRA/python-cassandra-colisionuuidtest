import time
from concurrent import futures
from cassandra.cluster import Cluster
from random import randint

MAX_WORKERS = 2
CASSANDRA_HOST = '127.0.0.1'
CASSANDRA_PORT = 32770
CASSANDRA_KEYSPACE = 'colisiontest'
CYCLE_PER_THREAD = 5000

cluster = Cluster(
    [CASSANDRA_HOST],
    port=CASSANDRA_PORT)

#auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
#cluster = Cluster(auth_provider=auth_provider, protocol_version=2)

session = cluster.connect(CASSANDRA_KEYSPACE)

def uuid_insert(wks):
    rand = randint(0,9)
    time.sleep(rand)
    t0 = time.time()
    for num in range(1, CYCLE_PER_THREAD):
        #time.sleep(randint(0,20))
        #todo: call select uuid() from colisiontest.testeuuid limit 1; Then insert ...  IF NOT EXISTS
        session.execute("INSERT INTO colisiontest.testeuuid(universal_id, moment) VALUES(uuid(), unixTimestampOf(now()));")
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
#Cassandra Docker

#without sleeprandon; then 10 colisions (why?)
#Thread 6 call 5000 inserts in 33.99s
#Thread 5 call 5000 inserts in 34.03s
#Thread 7 call 5000 inserts in 34.10s
#Thread 9 call 5000 inserts in 34.14s
#Thread 3 call 5000 inserts in 34.21s
#Thread 2 call 5000 inserts in 34.21s
#Thread 1 call 5000 inserts in 34.23s
#Thread 4 call 5000 inserts in 34.24s
#Thread 8 call 5000 inserts in 34.24s
#Thread 0 call 5000 inserts in 34.24s
#Total Time 34.25s
    #Cassandra select count(*) from colisiontest.testeuuid;
    #49990 rows: