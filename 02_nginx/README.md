> sraza @ sraza0522mac ~/code/devops_educative/02_nginx 17:18:26
$ docker build -t webserver .
[+] Building 4.0s (7/7) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                            0.0s
 => => transferring dockerfile: 96B                                                                                                                             0.0s
 => [internal] load .dockerignore                                                                                                                               0.0s
 => => transferring context: 2B                                                                                                                                 0.0s
 => [internal] load metadata for docker.io/library/nginx:1.15                                                                                                   0.9s
 => [internal] load build context                                                                                                                               0.0s
 => => transferring context: 363B                                                                                                                               0.0s
 => [1/2] FROM docker.io/library/nginx:1.15@sha256:23b4dcdf0d34d4a129755fc6f52e1c6e23bb34ea011b315d87e193033bcd1b68                                             2.8s
 => => resolve docker.io/library/nginx:1.15@sha256:23b4dcdf0d34d4a129755fc6f52e1c6e23bb34ea011b315d87e193033bcd1b68                                             0.0s
 => => sha256:29b80961214d7f0c89081fe8134e6e8e14ccfa1afe001357539f59930ff9e3ef 20.33MB / 20.33MB                                                                1.0s
 => => sha256:07b8ab2ff3246c40fe66f24efebd358bf04e3ede8390b714cd952930ed07ac52 21.63MB / 21.63MB                                                                1.3s
 => => sha256:ba4f63a9ae5b25d5bb002467d8d9464349c64b1081302b515db10dfc52cc3179 205B / 205B                                                                      0.2s
 => => sha256:23b4dcdf0d34d4a129755fc6f52e1c6e23bb34ea011b315d87e193033bcd1b68 1.41kB / 1.41kB                                                                  0.0s
 => => sha256:322d209ca0e9dcd69cf1bb9354cb2c573255e96689f31b0964753389b780269c 948B / 948B                                                                      0.0s
 => => sha256:f6d22dec9931b638b2f67c7197732e2bd1b9311877c2d7a1df7136f952fe8fc7 6.03kB / 6.03kB                                                                  0.0s
 => => extracting sha256:29b80961214d7f0c89081fe8134e6e8e14ccfa1afe001357539f59930ff9e3ef                                                                       0.9s
 => => extracting sha256:07b8ab2ff3246c40fe66f24efebd358bf04e3ede8390b714cd952930ed07ac52                                                                       0.6s
 => => extracting sha256:ba4f63a9ae5b25d5bb002467d8d9464349c64b1081302b515db10dfc52cc3179                                                                       0.0s
 => [2/2] COPY index.html /usr/share/nginx/html                                                                                                                 0.1s
 => exporting to image                                                                                                                                          0.0s
 => => exporting layers                                                                                                                                         0.0s
 => => writing image sha256:592bcebd51547d472abc4a989f9bd1fc92c2dff1e80e1adf68da2fee8cf1554e                                                                    0.0s
 => => naming to docker.io/library/webserver                                                                                                                    0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them

> sraza @ sraza0522mac ~/code/devops_educative/02_nginx 17:18:38
$ docker run --rm -it -p 8082:80 webserver
172.17.0.1 - - [29/May/2022:21:19:24 +0000] "GET / HTTP/1.1" 200 324 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36" "-"
2022/05/29 21:19:24 [error] 8#8: *2 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8082", referrer: "http://localhost:8082/"
172.17.0.1 - - [29/May/2022:21:19:24 +0000] "GET /favicon.ico HTTP/1.1" 404 556 "http://localhost:8082/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36" "-"