```sh
> sraza @ sraza0522mac ~/code/devops_educative/03_jsimage_node 18:25:55
$ docker build -t jsimage .
[+] Building 0.3s (7/7) FINISHED                                                                                                              
 => [internal] load build definition from Dockerfile                                                                                     0.0s
 => => transferring dockerfile: 110B                                                                                                     0.0s
 => [internal] load .dockerignore                                                                                                        0.0s
 => => transferring context: 2B                                                                                                          0.0s
 => [internal] load metadata for docker.io/library/node:11-alpine                                                                        0.2s
 => CACHED [1/2] FROM docker.io/library/node:11-alpine@sha256:8bb56bab197299c8ff820f1a55462890caf08f57ffe3b91f5fa6945a4d505932           0.0s
 => [internal] load build context                                                                                                        0.0s
 => => transferring context: 164B                                                                                                        0.0s
 => [2/2] COPY compute.js .                                                                                                              0.0s
 => exporting to image                                                                                                                   0.0s
 => => exporting layers                                                                                                                  0.0s
 => => writing image sha256:dbbb158c023ed697c2be1fb1a289847dda84d8c870825c6d53acb2d05ce20698                                             0.0s
 => => naming to docker.io/library/jsimage                                                                                               0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them

> sraza @ sraza0522mac ~/code/devops_educative/03_jsimage_node 18:26:19
$ docker run jsimage
Area of a 2 cm disk:
    12.566370614359172 cm²
```
