```sh
> sraza @ sraza0522mac ~/code/devops_educative/java 21:39:25
$ docker build -t rsaim/java .
[+] Building 1.0s (12/12) FINISHED                                                                                                            
 => [internal] load build definition from Dockerfile                   .0s
 => => transferring dockerfile: 37B                                    .0s
 => [internal] load .dockerignore                                      .0s
 => => transferring context: 2B                                        .0s
 => [internal] load metadata for docker.io/library/openjdk:8-jre-alpine.1s
 => [internal] load metadata for docker.io/library/openjdk:8-jdk-alpine.2s
 => [builder 1/4] FROM docker.io/library/openjdk:8-jdk-alpine@sha256:94792824df2df33402f201713f932b58cb9de94a0cd524164a0f2283343547b3    0.0s
 => [internal] load build context                                      .0s
 => => transferring context: 169B                                      .0s
 => CACHED [stage-1 1/2] FROM docker.io/library/openjdk:8-jre-alpine@sha256:f362b165b870ef129cbe730f29065ff37399c0aa8bcab3e44b51c302938  0.0s
 => CACHED [builder 2/4] WORKDIR /out                                  .0s
 => [builder 3/4] COPY *.java .                                        .0s
 => [builder 4/4] RUN javac Hello.java                                 .6s
 => [stage-1 2/2] COPY --from=builder /out/*.class .                   .0s
 => exporting to image                                                 .0s
 => => exporting layers                                                .0s
 => => writing image sha256:4017868539cf2eaa82e74f820bfd0ad9f3721c4035ab1bf2632cbf5abf83e39b                                             0.0s
 => => naming to docker.io/rsaim/java                                  .0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them

> sraza @ sraza0522mac ~/code/devops_educative/java 21:40:31
$ docker run rsaim/java
I'm Java running in a container.
```
