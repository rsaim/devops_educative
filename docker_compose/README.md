# Docker
Docker and Docker compose for developers.


```sh
> sraza @ sraza0522mac ~/code/Docker 11:26:38
$ docker-compose up --build
[+] Building 0.4s (10/10) FINISHED                                       
 => [internal] load build definition from Dockerfile                0.0s
 => => transferring dockerfile: 32B                                 0.0s
 => [internal] load .dockerignore                                   0.0s
 => => transferring context: 2B                                     0.0s
 => [internal] load metadata for docker.io/library/python:3.9-rc-b  0.2s
 => [internal] load build context                                   0.0s
 => => transferring context: 3.33kB                                 0.0s
 => [1/5] FROM docker.io/library/python:3.9-rc-buster@sha256:f408c  0.0s
 => CACHED [2/5] WORKDIR /code                                      0.0s
 => CACHED [3/5] COPY requirements.txt requirements.txt             0.0s
 => CACHED [4/5] RUN pip3 install -r requirements.txt               0.0s
 => [5/5] COPY . .                                                  0.0s
 => exporting to image                                              0.0s
 => => exporting layers                                             0.0s
 => => writing image sha256:0be7012959865e102f470710c444465ce83684  0.0s
 => => naming to docker.io/library/docker_web                       0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
[+] Running 2/2
 ⠿ Container docker-database-1  Ru...                               0.0s
 ⠿ Container docker-web-1       Recreat...                          0.1s
Attaching to docker-database-1, docker-web-1
docker-database-1  | 2022-05-30T15:26:54.421544Z 0 [Note] InnoDB: Shutdown completed; log sequence number 12135787
docker-database-1  | 2022-05-30T15:26:54.424303Z 0 [Note] InnoDB: Removed temporary tablespace data file: "ibtmp1"
docker-database-1  | 2022-05-30T15:26:54.424609Z 0 [Note] Shutting down plugin 'MEMORY'
docker-database-1  | 2022-05-30T15:26:54.424682Z 0 [Note] Shutting down plugin 'CSV'
docker-database-1  | 2022-05-30T15:26:54.424711Z 0 [Note] Shutting down plugin 'sha256_password'
docker-database-1  | 2022-05-30T15:26:54.424718Z 0 [Note] Shutting down plugin 'mysql_native_password'
docker-database-1  | 2022-05-30T15:26:54.425261Z 0 [Note] Shutting down plugin 'binlog'
docker-database-1  | 2022-05-30T15:26:54.432026Z 0 [Note] mysqld: Shutdown complete
docker-database-1  | 
docker-web-1       |  * Serving Flask app 'app.py' (lazy loading)
docker-web-1       |  * Environment: development
docker-web-1       |  * Debug mode: on
docker-web-1       |  * Running on all addresses (0.0.0.0)
docker-web-1       |    WARNING: This is a development server. Do not use it in a production deployment.
docker-web-1       |  * Running on http://127.0.0.1:5000
docker-web-1       |  * Running on http://172.18.0.3:5000 (Press CTRL+C to quit)
docker-web-1       |  * Restarting with stat
docker-web-1       |  * Debugger is active!
docker-web-1       |  * Debugger PIN: 535-884-979
docker-database-1  | [Entrypoint] Server shut down
docker-database-1  | 
docker-database-1  | [Entrypoint] MySQL init process done. Ready for start up.
docker-database-1  | 
docker-database-1  | [Entrypoint] Starting MySQL 5.7.38-1.2.8-server
docker-database-1  | 2022-05-30T15:26:55.404321Z 0 [Warning] TIMESTAMP with implicit DEFAULT value is deprecated. Please use --explicit_defaults_for_timestamp server option (see documentation for more details).
docker-database-1  | 2022-05-30T15:26:55.410168Z 0 [Note] mysqld (mysqld 5.7.38) starting as process 1 ...
docker-database-1  | 2022-05-30T15:26:55.450590Z 0 [Note] InnoDB: PUNCH HOLE support available
docker-database-1  | 2022-05-30T15:26:55.453173Z 0 [Note] InnoDB: Mutexes and rw_locks use GCC atomic builtins
docker-database-1  | 2022-05-30T15:26:55.453294Z 0 [Note] InnoDB: Uses event mutexes
docker-database-1  | 2022-05-30T15:26:55.453842Z 0 [Note] InnoDB: GCC builtin __atomic_thread_fence() is used for memory barrier
docker-database-1  | 2022-05-30T15:26:55.453960Z 0 [Note] InnoDB: Compressed tables use zlib 1.2.11
docker-database-1  | 2022-05-30T15:26:55.454028Z 0 [Note] InnoDB: Using Linux native AIO
docker-database-1  | 2022-05-30T15:26:55.460188Z 0 [Note] InnoDB: Number of pools: 1
docker-database-1  | 2022-05-30T15:26:55.462476Z 0 [Note] InnoDB: Using CPU crc32 instructions
docker-database-1  | 2022-05-30T15:26:55.464729Z 0 [ERROR] InnoDB: Linux Native AIO interface is not supported on this platform. Please check your OS documentation and install appropriate binary of InnoDB.
docker-database-1  | 2022-05-30T15:26:55.464981Z 0 [Note] InnoDB: You can disable Linux Native AIO by setting innodb_use_native_aio = 0 in my.cnf
docker-database-1  | 2022-05-30T15:26:55.465366Z 0 [Warning] InnoDB: Linux Native AIO disabled.
docker-database-1  | 2022-05-30T15:26:55.469448Z 0 [Note] InnoDB: Initializing buffer pool, total size = 128M, instances = 1, chunk size = 128M
docker-database-1  | 2022-05-30T15:26:55.526455Z 0 [Note] InnoDB: Completed initialization of buffer pool
docker-database-1  | 2022-05-30T15:26:55.547688Z 0 [Note] InnoDB: If the mysqld execution user is authorized, page cleaner thread priority can be changed. See the man page of setpriority().
docker-database-1  | 2022-05-30T15:26:55.571743Z 0 [Note] InnoDB: Highest supported file format is Barracuda.
docker-database-1  | 2022-05-30T15:26:55.652447Z 0 [Note] InnoDB: Creating shared tablespace for temporary tables
docker-database-1  | 2022-05-30T15:26:55.654307Z 0 [Note] InnoDB: Setting file './ibtmp1' size to 12 MB. Physically writing the file full; Please wait ...
docker-database-1  | 2022-05-30T15:26:55.671937Z 0 [Note] InnoDB: File './ibtmp1' size is now 12 MB.
docker-database-1  | 2022-05-30T15:26:55.678821Z 0 [Note] InnoDB: 96 redo rollback segment(s) found. 96 redo rollback segment(s) are active.
docker-database-1  | 2022-05-30T15:26:55.678973Z 0 [Note] InnoDB: 32 non-redo rollback segment(s) are active.
docker-database-1  | 2022-05-30T15:26:55.695044Z 0 [Note] InnoDB: Waiting for purge to start
docker-database-1  | 2022-05-30T15:26:55.746458Z 0 [Note] InnoDB: 5.7.38 started; log sequence number 12135787
docker-database-1  | 2022-05-30T15:26:55.750735Z 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/ib_buffer_pool
docker-database-1  | 2022-05-30T15:26:55.756886Z 0 [Note] Plugin 'FEDERATED' is disabled.
docker-database-1  | 2022-05-30T15:26:55.811867Z 0 [Note] InnoDB: Buffer pool(s) load completed at 220530 15:26:55
docker-database-1  | 2022-05-30T15:26:55.816485Z 0 [Note] Found ca.pem, server-cert.pem and server-key.pem in data directory. Trying to enable SSL support using them.
docker-database-1  | 2022-05-30T15:26:55.816586Z 0 [Note] Skipping generation of SSL certificates as certificate files are present in data directory.
docker-database-1  | 2022-05-30T15:26:55.816692Z 0 [Warning] A deprecated TLS version TLSv1 is enabled. Please use TLSv1.2 or higher.
docker-database-1  | 2022-05-30T15:26:55.816736Z 0 [Warning] A deprecated TLS version TLSv1.1 is enabled. Please use TLSv1.2 or higher.
docker-database-1  | 2022-05-30T15:26:55.836275Z 0 [Warning] CA certificate ca.pem is self signed.
docker-database-1  | 2022-05-30T15:26:55.837804Z 0 [Note] Skipping generation of RSA key pair as key files are present in data directory.
docker-database-1  | 2022-05-30T15:26:55.841991Z 0 [Note] Server hostname (bind-address): '*'; port: 3306
docker-database-1  | 2022-05-30T15:26:55.843517Z 0 [Note] IPv6 is available.
docker-database-1  | 2022-05-30T15:26:55.844143Z 0 [Note]   - '::' resolves to '::';
docker-database-1  | 2022-05-30T15:26:55.845038Z 0 [Note] Server socket created on IP: '::'.
docker-database-1  | 2022-05-30T15:26:55.908384Z 0 [Note] Event Scheduler: Loaded 0 events
docker-database-1  | 2022-05-30T15:26:55.910573Z 0 [Note] mysqld: ready for connections.
docker-database-1  | Version: '5.7.38'  socket: '/var/lib/mysql/mysql.sock'  port: 3306  MySQL Community Server (GPL)
docker-web-1       | 172.18.0.1 - - [30/May/2022 15:27:28] "GET / HTTP/1.1" 200 -
docker-web-1       | 172.18.0.1 - - [30/May/2022 15:27:28] "GET /favicon.ico HTTP/1.1" 404 -
```
> sraza @ sraza0522mac ~/code/Docker 11:40:01
$ docker pull venky8283/flask_app:3.0
3.0: Pulling from venky8283/flask_app
7e2b2a5af8f6: Pull complete 
09b6f03ffac4: Pull complete 
dc3f0c679f0f: Pull complete 
fd4b47407fc3: Pull complete 
b32f6bf7d96d: Pull complete 
3940e1b57073: Pull complete 
d940571110ef: Pull complete 
0a915c90c91d: Pull complete 
8d88f981c5ec: Pull complete 
e61682d8bc36: Pull complete 
9f572989020b: Pull complete 
266ab62b50ee: Pull complete 
beda54dd88ef: Pull complete 
d450b9e72e73: Pull complete 
28b56e85de59: Pull complete 
8b6b0fae1d18: Pull complete 
Digest: sha256:8f55557333526897254e69b57e049ee9a3d39a4df1305e57963684a5619acb18
Status: Downloaded newer image for venky8283/flask_app:3.0
docker.io/venky8283/flask_app:3.0