> sraza @ sraza0522mac ~/code/devops_educative 16:53:46
$ docker build -t hello_img .
[+] Building 4.2s (5/5) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                            0.0s
 => => transferring dockerfile: 85B                                                                                                                             0.0s
 => [internal] load .dockerignore                                                                                                                               0.0s
 => => transferring context: 2B                                                                                                                                 0.0s
 => [internal] load metadata for docker.io/library/debian:11                                                                                                    0.9s
 => [1/1] FROM docker.io/library/debian:11@sha256:3f1d6c17773a45c97bd8f158d665c9709d7b29ed7917ac934086ad96f92e4510                                              3.1s
 => => resolve docker.io/library/debian:11@sha256:3f1d6c17773a45c97bd8f158d665c9709d7b29ed7917ac934086ad96f92e4510                                              0.0s
 => => sha256:3f1d6c17773a45c97bd8f158d665c9709d7b29ed7917ac934086ad96f92e4510 1.85kB / 1.85kB                                                                  0.0s
 => => sha256:1623b714f66926243b9b946d59d200082a1b86043169f4d6602b6e64bc20a38a 529B / 529B                                                                      0.0s
 => => sha256:e38a1b1bebd53396928bac3000fcc9fee3970cd022eae1e79fbd08d46a1a6ea8 1.48kB / 1.48kB                                                                  0.0s
 => => sha256:d794814721d57f8aaec06ab3652e90212cc3beccf5ff5c87f6ecf8375784bcc8 53.70MB / 53.70MB                                                                1.4s
 => => extracting sha256:d794814721d57f8aaec06ab3652e90212cc3beccf5ff5c87f6ecf8375784bcc8                                                                       1.6s
 => exporting to image                                                                                                                                          0.0s
 => => exporting layers                                                                                                                                         0.0s
 => => writing image sha256:36c955cb44b56743e117debb0100a09da10fb47d594dd880cb5b32dc0ded98c5                                                                    0.0s
 => => naming to docker.io/library/hello_img                                                                                                                    0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them

> sraza @ sraza0522mac ~/code/devops_educative 16:59:08
$ docker run --rm hello_img
Hello World

> sraza @ sraza0522mac ~/code/devops_educative 17:00:41
$ cat Dockerfile
FROM debian:11