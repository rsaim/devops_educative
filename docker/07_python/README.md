$ docker build -t rsaim/07_python .
[+] Building 0.3s (9/9) FINISHED                                                                                                              
 => [internal] load build definition from Dockerfile                      .0s
 => => transferring dockerfile: 37B                                       .0s
 => [internal] load .dockerignore                                         .0s
 => => transferring context: 2B                                           .0s
 => [internal] load metadata for docker.io/library/python:3.7-stretch     .2s
 => [1/4] FROM docker.io/library/python:3.7-stretch@sha256:f678e6659fcd0a3fd4e3426f46b0b534253b0971da34dca6ce5b0c6e49b7cd64              0.0s
 => [internal] load build context                                         .0s
 => => transferring context: 393B                                         .0s
 => CACHED [2/4] RUN pip install Flask                                    .0s
 => CACHED [3/4] COPY templates ./templates                               .0s
 => [4/4] COPY server.py .                                                .0s
 => exporting to image                                                    .0s
 => => exporting layers                                                   .0s
 => => writing image sha256:ba5264df171e7a09cb4cd0c33e2dd2e1e975629d7460e02a02e1e546513b70da                                             0.0s
 => => naming to docker.io/rsaim/07_python                                .0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them> sraza @ sraza0522mac ~/code/devops_educative/docker/07_python 23:07:23
$ docker run --rm -it -p 8087:5000 rsaim/07_python
 * Serving Flask app 'server.py' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.4:5000 (Press CTRL+C to quit)
172.17.0.1 - - [30/May/2022 03:07:32] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [30/May/2022 03:07:33] "GET /v1/square/4 HTTP/1.1" 200 -