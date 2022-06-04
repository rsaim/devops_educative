Ref: https://docs.docker.com/engine/swarm/swarm-tutorial/deploy-service/

```sh
> sraza @ sraza0522mac ~/code/devops_educative/docker_swarm 15:43:27
$ docker swarm init
Swarm initialized: current node (48f8b8d6mmkp2dejhuyaj8pvh) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-35d3v30ayy9zw9nizvdnmjhrftn1g72agnmvd77sa8689fqjq5-1msm51af644wxwfui9u91lsb0 192.168.65.3:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

```sh
> sraza @ sraza0522mac ~/code/devops_educative/docker_swarm 15:58:41
$ docker node ls
ID                            HOSTNAME         STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
48f8b8d6mmkp2dejhuyaj8pvh *   docker-desktop   Ready     Active         Leader           20.10.14
```

> sraza @ sraza0522mac ~/code/devops_educative/docker_swarm 16:02:54
$ docker service create --replicas 1 --name helloworld alpine ping docker.com
tzhfgnd2ivbhmc8ez95npflj4
overall progress: 1 out of 1 tasks
1/1: running   [==================================================>]
verify: Service converged

> sraza @ sraza0522mac ~/code/devops_educative/docker_swarm 16:03:21
$ docker service ls
ID             NAME         MODE         REPLICAS   IMAGE           PORTS
tzhfgnd2ivbh   helloworld   replicated   1/1        alpine:latest
> sraza @ sraza0522mac ~/code/devops_educative/docker_swarm 16:03:42
$ docker service inspect helloworld
[
    {
        "ID": "tzhfgnd2ivbhmc8ez95npflj4",
        "Version": {
            "Index": 732
        },
        "CreatedAt": "2022-06-03T20:03:05.794909755Z",
        "UpdatedAt": "2022-06-03T20:03:05.794909755Z",
        "Spec": {
            "Name": "helloworld",
            "Labels": {},
            "TaskTemplate": {
                "ContainerSpec": {
                    "Image": "alpine:latest@sha256:686d8c9dfa6f3ccfc8230bc3178d23f84eeaf7e457f36f271ab1acc53015037c",
                    "Args": [
                        "ping",
                        "docker.com"
                    ],
                    "Init": false,
                    "StopGracePeriod": 10000000000,
                    "DNSConfig": {},
                    "Isolation": "default"
                },
                "Resources": {
                    "Limits": {},
                    "Reservations": {}
                },
                "RestartPolicy": {
                    "Condition": "any",
                    "Delay": 5000000000,
                    "MaxAttempts": 0
                },
                "Placement": {
                    "Platforms": [
                        {
                            "Architecture": "amd64",
                            "OS": "linux"
                        },
                        {
                            "OS": "linux"
                        },
                        {
                            "OS": "linux"
                        },
                        {
                            "Architecture": "arm64",
                            "OS": "linux"
                        },
                        {
                            "Architecture": "386",
                            "OS": "linux"
                        },
                        {
                            "Architecture": "ppc64le",
                            "OS": "linux"
                        },
                        {
                            "Architecture": "s390x",
                            "OS": "linux"
                        }
                    ]
                },
                "ForceUpdate": 0,
                "Runtime": "container"
            },
            "Mode": {
                "Replicated": {
                    "Replicas": 1
                }
            },
            "UpdateConfig": {
                "Parallelism": 1,
                "FailureAction": "pause",
                "Monitor": 5000000000,
                "MaxFailureRatio": 0,
                "Order": "stop-first"
            },
            "RollbackConfig": {
                "Parallelism": 1,
                "FailureAction": "pause",
                "Monitor": 5000000000,
                "MaxFailureRatio": 0,
                "Order": "stop-first"
            },
            "EndpointSpec": {
                "Mode": "vip"
            }
        },
        "Endpoint": {
            "Spec": {}
        }
    }
]
> sraza @ sraza0522mac ~/code/devops_educative/docker_swarm 16:04:49
$ docker service ps helloworld
ID             NAME           IMAGE           NODE             DESIRED STATE   CURRENT STATE            ERROR     PORTS
rwsxqhl0e49d   helloworld.1   alpine:latest   docker-desktop   Running         Running 22 minutes ago> sraza @ sraza0522mac ~/code/devops_educative/docker_swarm 17:20:37
$ docker service scale helloworld=3
helloworld scaled to 3
overall progress: 3 out of 3 tasks
1/3: running   [==================================================>]
2/3: running   [==================================================>]
3/3: running   [==================================================>]
verify: Service converged> sraza @ sraza0522mac ~/code/devops_educative/docker_swarm 17:20:57
$ docker service ls
ID             NAME         MODE         REPLICAS   IMAGE           PORTS
tzhfgnd2ivbh   helloworld   replicated   3/3        alpine:latest