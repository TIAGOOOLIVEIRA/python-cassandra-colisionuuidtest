# python-cassandra-colisionuuidtest
It is just a test to ensure colision level generating uuid with parallel requesting by python.

Parameters
 Environment: Win10 64bits; 16GB mem; i7
 App: Python 3.6 (Anaconda 3.0)
 Database: Cassandra Docker;  'replication_factor' : 3 https://hub.docker.com/r/spotify/cassandra/
 
Execution Configuration
 Threads: 30
 Cycles per thread: 1000
 Sleep range at begining execution: Random 0,20
 
Besides the test not considered a long runing, it was possible to ensure in this scenario zero colision with. This scenario simulated a random behavior of users creating events for insertions in the database.

Therefore, it's recommended test a long running execution and decreasing the random range of sleep to get high parallelism, and then improve the collision probability.
 
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
