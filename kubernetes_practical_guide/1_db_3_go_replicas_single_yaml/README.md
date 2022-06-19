```bash
$ cat go-demo-2.yml
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

---

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

---

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

---

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

$ k create -f go-demo-2.yml
replicaset.apps/go-demo-2-db created
service/go-demo-2-db created
replicaset.apps/go-demo-2-api created
service/go-demo-2-api created

$ k get -f go-demo-2.yml
NAME                           DESIRED   CURRENT   READY   AGE
replicaset.apps/go-demo-2-db   1         1         1       26s

NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)     AGE
service/go-demo-2-db   ClusterIP   10.99.176.120   <none>        27017/TCP   26s

NAME                            DESIRED   CURRENT   READY   AGE
replicaset.apps/go-demo-2-api   3         3         3       26s

NAME                    TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/go-demo-2-api   NodePort   10.105.125.125   <none>        8080:31846/TCP   26s

$ k get all
NAME                      READY   STATUS    RESTARTS   AGE
pod/go-demo-2-api-cgr4n   1/1     Running   0          40s
pod/go-demo-2-api-qw2bn   1/1     Running   0          40s
pod/go-demo-2-api-stjx6   1/1     Running   0          40s
pod/go-demo-2-db-nmqq9    1/1     Running   0          40s

NAME                    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/go-demo-2-api   NodePort    10.105.125.125   <none>        8080:31846/TCP   40s
service/go-demo-2-db    ClusterIP   10.99.176.120    <none>        27017/TCP        40s
service/kubernetes      ClusterIP   10.96.0.1        <none>        443/TCP          4h50m

NAME                            DESIRED   CURRENT   READY   AGE
replicaset.apps/go-demo-2-api   3         3         3       40s
replicaset.apps/go-demo-2-db    1         1         1       40s

$ curl -i "http://192.168.59.100:31881/demo/hello"
curl: (7) Failed to connect to 192.168.59.100 port 31881: Connection refused

$ kubectl get svc go-demo-2-api -o jsonpath="{.spec.ports[0].nodePort}"
31846

$ curl -i "http://192.168.59.100:31846/demo/hello"
HTTP/1.1 200 OK
Date: Sat, 18 Jun 2022 23:14:24 GMT
Content-Length: 14
Content-Type: text/plain; charset=utf-8

hello, world!
```

### Delete minikube

```bash
$ minikube delete
🔥  Deleting "minikube" in virtualbox ...
💀  Removed all traces of the "minikube" cluster.
```