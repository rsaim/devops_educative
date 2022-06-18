```shell
>saim @ Saims-MacBook-Pro.local ~ 14:12:50
$ minikube start --vm-driver=virtualbox
😄 minikube v1.24.0 on Darwin 11.6
✨ Using the virtualbox driver based on existing profile
👍 Starting control plane node minikube in cluster minikube
🤷 virtualbox "minikube" VM is missing, will recreate.
🔥 Creating virtualbox VM (CPUs=2, Memory=2200MB, Disk=20000MB) ...
🐳 Preparing Kubernetes v1.22.3 on Docker 20.10.8 ...
 ▪ Generating certificates and keys ...
 ▪ Booting up control plane ...
 ▪ Configuring RBAC rules ...
 ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟 Enabled addons: storage-provisioner, default-storageclass
🔎 Verifying Kubernetes components...
🏄 Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default> saim @ Saims-MacBook-Pro.local ~/github/devops_educative/kubernetes_practical_guide 14:24:52 $ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured> saim @ Saims-MacBook-Pro.local ~/github/devops_educative/kubernetes_practical_guide 14:33:35
$ minikube dashboard
🔌 Enabling dashboard ...
 ▪ Using image kubernetesui/dashboard:v2.3.1
 ▪ Using image kubernetesui/metrics-scraper:v1.0.7
🤔 Verifying dashboard health ...
🚀 Launching proxy ...
🤔 Verifying proxy health ...
🎉 Opening http://127.0.0.1:64864/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ in your default browser...
^Z
[1]+ Stopped minikube dashboard> saim @ Saims-MacBook-Pro.local ~/github/devops_educative/kubernetes_practical_guide 15:02:22 
```

```bash
$ minikube ssh 
 _ _
 _ _ ( ) ( )
 ___ ___ (_) ___ (_)| |/') _ _ | |_ __
/' _ ` _ `\| |/' _ `\| || , < ( ) ( )| '_`\ /'__`\
| ( ) ( ) || || ( ) || || |\`\ | (_) || |_) )( ___/
(_) (_) (_)(_)(_) (_)(_)(_) (_)`\___/'(_,__/'`\____)$ ls 
$ pwd
/home/docker
$ ls -la
total 0
drwxr-xr-x 3 docker docker 60 Jun 18 18:22 .
drwxr-xr-x 3 root root 60 Oct 27 2021 ..
drwx------ 2 docker docker 80 Jan 1 1970 .ssh
```

```bash
> saim @ Saims-MacBook-Pro.local ~/github/devops_educative/kubernetes_practical_guide/k8s-specs 15:27:48
$ git remote -v
origin    https://github.com/vfarcic/k8s-specs.git (fetch)
origin    https://github.com/vfarcic/k8s-specs.git (push)
```

We evaluated `minikube` variables so that our local Docker client is using Docker server running inside the VM. Further on, we listed all the containers based on the `mongo` image.

```bash
> saim @ Saims-MBP ~/github/devops_educative/kubernetes_practical_guide 15:43:29
$ eval $(minikube docker-env)

> saim @ Saims-MBP ~/github/devops_educative/kubernetes_practical_guide 15:43:34
$ docker container ls -f ancestor=mongo
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
4a1ed88935f6   mongo     "docker-entrypoint.s…"   33 minutes ago   Up 33 minutes             k8s_db_db_default_c849369f-c453-41cf-bcac-bab96dddb551_0

> saim @ Saims-MBP ~/github/devops_educative/kubernetes_practical_guide 15:43:35
$ minikube docker-env
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.59.100:2376"
export DOCKER_CERT_PATH="/Users/saim/.minikube/certs"
export MINIKUBE_ACTIVE_DOCKERD="minikube"

# To point your shell to minikube's docker-daemon, run:
# eval $(minikube -p minikube docker-env)
```

```
saim @ Saims-MBP ~/github/devops_educative/kubernetes_practical_guide 15:45:30
$ k delete pod db
pod "db" deleted
```

## Executing a New Process[#](https://www.educative.io/module/lesson/a-practical-guide-to-kubernetes/7no445Y6Oy8#Executing-a-New-Process)

Just as with Docker, we can execute a new process inside a running container inside a Pod. 
Run a command `ps aux` in the `db` pod

```
kubectl exec db ps aux
```

The **output** will be similar as follows.

```
USER PID %CPU %MEM    VSZ   RSS TTY STAT START TIME COMMAND

root 1 0.5 2.9 967452 59692 ? Ssl 21:47 0:03 mongod --rest --httpinterface

root 31 0.0 0.0 17504 1980 ? Rs 21:58 0:00 ps aux
```

> kubectl exec -it db sh

We’re inside the `sh` process inside the container. Since the container hosts a Mongo database, we can, for example, execute `db.stats()` to confirm that the database is indeed running.

>  echo 'db.stats()' | mongo localhost:27017/test

We used `mongo` client to execute `db.stats()` for the database `test` running on `localhost:27017`. Since we’re not trying to learn Mongo, the only purpose of this exercise was to prove that the database is up-and-running. Let’s get out of the container.

Logs from a pod:

```bash
> saim @ Saims-MBP ~/github/devops_educative/kubernetes_practical_guide 15:58:15
$ k logs db
2022-06-18T19:57:08.472+0000 I CONTROL  [initandlisten] MongoDB starting : pid=1 port=27017 dbpath=/data/db 64-bit host=db
2022-06-18T19:57:08.472+0000 I CONTROL  [initandlisten] db version v3.3.15
2022-06-18T19:57:08.472+0000 I CONTROL  [initandlisten] git version: 520f5571d039b57cf9c319b49654909828971073
2022-06-18T19:57:08.472+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.1t  3 May 2016
2022-06-18T19:57:08.472+0000 I CONTROL  [initandlisten] allocator: tcmalloc
2022-06-18T19:57:08.472+0000 I CONTROL  [initandlisten] modules: none
2022-06-18T19:57:08.472+0000 I CONTROL  [initandlisten] build environment:
2022-06-18T19:57:08.472+0000 I CONTROL  [initandlisten]     distmod: debian81
2022-06-18T19:57:08.472+0000 I CONTROL  [initandlisten]     distarch: x86_64
2022-06-18T19:57:08.472+0000 I CONTROL  [initandlisten]     target_arch: x86_64
2022-06-18T19:57:08.472+0000 I CONTROL  [initandlisten] options: { net: { http: { RESTInterfaceEnabled: true, enabled: true } } }
2022-06-18T19:57:08.477+0000 I STORAGE  [initandlisten]
2022-06-18T19:57:08.477+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2022-06-18T19:57:08.477+0000 I STORAGE  [initandlisten] See http://dochub.mongodb.org/core/prodnotes-filesystem
2022-06-18T19:57:08.477+0000 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=555M,session_max=20000,eviction=(threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),checkpoint=(wait=60,log_size=2GB),statistics_log=(wait=0),
2022-06-18T19:57:08.498+0000 I CONTROL  [initandlisten]
2022-06-18T19:57:08.499+0000 I CONTROL  [initandlisten] ** NOTE: This is a development version (3.3.15) of MongoDB.
2022-06-18T19:57:08.499+0000 I CONTROL  [initandlisten] **       Not recommended for production.
2022-06-18T19:57:08.499+0000 I CONTROL  [initandlisten]
2022-06-18T19:57:08.499+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2022-06-18T19:57:08.499+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2022-06-18T19:57:08.499+0000 I CONTROL  [initandlisten] ** WARNING: You are running this process as the root user, which is not recommended.
2022-06-18T19:57:08.499+0000 I CONTROL  [initandlisten]
2022-06-18T19:57:08.499+0000 I NETWORK  [websvr] admin web console waiting for connections on port 28017
2022-06-18T19:57:08.503+0000 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/data/db/diagnostic.data'
2022-06-18T19:57:08.509+0000 I INDEX    [initandlisten] build index on: admin.system.version properties: { v: 2, key: { version: 1 }, name: "incompatible_with_version_32", ns: "admin.system.version" }
2022-06-18T19:57:08.509+0000 I INDEX    [initandlisten]      building index using bulk method
2022-06-18T19:57:08.510+0000 I INDEX    [initandlisten] build index done.  scanned 0 total records. 0 secs
2022-06-18T19:57:08.510+0000 I NETWORK  [thread1] waiting for connections on port 27017
```

Accessing environment variables of a pod:

```bash
$ k exec pod/go-demo-2-db-nmqq9 env
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=go-demo-2-db-nmqq9
GO_DEMO_2_DB_PORT=tcp://10.99.176.120:27017
GO_DEMO_2_API_PORT_8080_TCP_ADDR=10.105.125.125
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PORT=443
GO_DEMO_2_DB_SERVICE_PORT=27017
GO_DEMO_2_DB_PORT_27017_TCP_PORT=27017
GO_DEMO_2_API_PORT_8080_TCP_PROTO=tcp
GO_DEMO_2_API_PORT_8080_TCP_PORT=8080
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_SERVICE_PORT=443
KUBERNETES_PORT_443_TCP_PROTO=tcp
GO_DEMO_2_DB_SERVICE_HOST=10.99.176.120
GO_DEMO_2_DB_PORT_27017_TCP_ADDR=10.99.176.120
GO_DEMO_2_API_SERVICE_HOST=10.105.125.125
GO_DEMO_2_API_PORT=tcp://10.105.125.125:8080
GO_DEMO_2_API_PORT_8080_TCP=tcp://10.105.125.125:8080
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
GO_DEMO_2_DB_PORT_27017_TCP=tcp://10.99.176.120:27017
GO_DEMO_2_DB_PORT_27017_TCP_PROTO=tcp
GO_DEMO_2_API_SERVICE_PORT=8080
GOSU_VERSION=1.7
MONGO_MAJOR=3.3
MONGO_VERSION=3.3.15
MONGO_PACKAGE=mongodb-org-unstable
HOME=/root
```

Accessing external IP of a svc:



```bash


```