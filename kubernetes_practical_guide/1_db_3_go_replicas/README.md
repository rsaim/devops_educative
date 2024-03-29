### Manifest for 1 replica of the Mondo DB service.

```yaml
$ cat go-demo-2-db-rs.yml
apiVersion:  apps/v1
kind: ReplicaSet
metadata:
  name: go-demo-2-db
spec:
  selector:
    matchLabels:
      type: db
      service: go-demo-2
  template:
    metadata:
      labels:
        type: db
        service: go-demo-2
        vendor: MongoLabs
    spec:
      containers:
      - name: db
        image: mongo:3.3
        ports:
        - containerPort: 28017
```

```bash
$ k create -f go-demo-2-db-rs.yml
replicaset.apps/go-demo-2-db created

$ k get pods
NAME                 READY   STATUS    RESTARTS   AGE
go-demo-2-db-wbwjz   1/1     Running   0          34s
```

##### The next one is the Service for the Pod we just created through the ReplicaSet.

```bash
$ cat go-demo-2-db-svc.yml
apiVersion: v1
kind: Service
metadata:
  name: go-demo-2-db
spec:
  ports:
  - port: 27017
  selector:
    type: db
    service: go-demo-2

$ k create -f k8s-specs/svc/vc.yml
service/go-demo-2-db created

$ k get pods
NAME                 READY   STATUS    RESTARTS   AGE
go-demo-2-db-wbwjz   1/1     Running   0          3m47s

$ k get services
NAME           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)     AGE
go-demo-2-db   ClusterIP   10.100.246.86   <none>        27017/TCP   8s
kubernetes     ClusterIP   10.96.0.1       <none>        443/TCP     4h1m
```

##### We are finished with the database. The ReplicaSet will make sure that the Pod is (almost) always up-and-running and the Service will allow other Pods to communicate with it through a fixed DNS.

## Backend API

Create the backend Go service with 3 replicas.

```bash
$ cat go-demo-2-api-rs.yml
apiVersion:  apps/v1
kind: ReplicaSet
metadata:
  name: go-demo-2-api
spec:
  replicas: 3
  selector:
    matchLabels:
      type: api
      service: go-demo-2
  template:
    metadata:
      labels:
        type: api
        service: go-demo-2
        language: go
    spec:
      containers:
      - name: api
        image: vfarcic/go-demo-2
        env:
        - name: DB
          value: go-demo-2-db
        readinessProbe:
          httpGet:
            path: /demo/hello
            port: 8080
          periodSeconds: 1
        livenessProbe:
          httpGet:
            path: /demo/hello
            port: 8080

$ k create -f k8s-specs/svc/rs.yml
replicaset.apps/go-demo-2-api created
```

Define service to expose the GO api to outside world using port **8080** using `NodePort`.

```bash
$ cat go-demo-2-api-svc.yml
apiVersion: v1
kind: Service
metadata:
  name: go-demo-2-api
spec:
  type: NodePort
  ports:
  - port: 8080
  selector:
    type: api
    service: go-demo-2

$ k create -f k8s-specs/svc/svc.yml
service/go-demo-2-api created
```

The 4 created pods/services and everything else in the cluster.

```bash
$ k get all
NAME                      READY   STATUS    RESTARTS   AGE
pod/go-demo-2-api-p5jmq   1/1     Running   0          2m57s
pod/go-demo-2-api-p8cv8   1/1     Running   0          2m57s
pod/go-demo-2-api-pghcg   1/1     Running   0          2m57s
pod/go-demo-2-db-wbwjz    1/1     Running   0          26m

NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/go-demo-2-api   NodePort    10.99.211.103   <none>        8080:31881/TCP   74s
service/go-demo-2-db    ClusterIP   10.100.246.86   <none>        27017/TCP        23m
service/kubernetes      ClusterIP   10.96.0.1       <none>        443/TCP          4h24m

NAME                            DESIRED   CURRENT   READY   AGE
replicaset.apps/go-demo-2-api   3         3         3       2m57s
replicaset.apps/go-demo-2-db    1         1         1       26m
```

Hitting service from outside:

```bash
$ minikube ip
192.168.59.100

$ kubectl get svc go-demo-2-api -o jsonpath="{.spec.ports[0].nodePort}"
31881

$ curl -i "http://192.168.59.100:31881/demo/hello"
HTTP/1.1 200 OK
Date: Sat, 18 Jun 2022 22:51:41 GMT
Content-Length: 14
Content-Type: text/plain; charset=utf-8

hello, world!
```

We have used 4 yaml files to create the cluster with 3 replicas of the backed api and 1 replica of the database.

```bash
$ kubectl delete -f go-demo-2-db-rs.yml
replicaset.apps "go-demo-2-db" deleted

$ kubectl delete -f k8s-specs/svc/vc.yml
service "go-demo-2-db" deleted

$ kubectl delete -f k8s-specs/svc/go-demo-2-api-set.apps "go-demo-2-api" deleted

$ kubectl delete -f k8s-specs/svc/go-demo-2-api-svc.yml
servicpi" deleted
```

Status of the cluster after deletion:

```bash
$ k get all
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   4h42m
```