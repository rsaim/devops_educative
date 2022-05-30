```bash
> sraza @ sraza0522mac ~/code/devops_educative/docker/06_php 22:54:48
$ docker build -t rsaim/06_php .
[+] Building 9.5s (9/9) FINISHED                                                                                                              
 => [internal] load build definition from Dockerfile                            .0s
 => => transferring dockerfile: 129B                                            .0s
 => [internal] load .dockerignore                                               .0s
 => => transferring context: 2B                                                 .0s
 => [internal] load metadata for docker.io/library/php:7.0-apache                                                                        1.0s
 => [auth] library/php:pull token for registry-1.docker.io                      .0s
 => [1/3] FROM docker.io/library/php:7.0-apache@sha256:1d34b2e491a02ba7a8d26478132015e197a5ffea37f0a93b42621d11cfe042cc                  7.8s
 => => resolve docker.io/library/php:7.0-apache@sha256:1d34b2e491a02ba7a8d26478132015e197a5ffea37f0a93b42621d11cfe042cc                  0.0s
 => => sha256:1d34b2e491a02ba7a8d26478132015e197a5ffea37f0a93b42621d11cfe042cc 2.37kB / 2.37kB                                           0.0s
 => => sha256:1a07b0163994a6d3328beeaa3400f6304e68548ffb84deefcb74427a6b65a489 20.34MB / 20.34MB                                         1.5s
 => => sha256:59be51dca15077e7f02edb4376d3e8e194896c4e706c9c03c2fd2d2af47f8cdc 57.61MB / 57.61MB                                         3.8s
 => => sha256:eff48a6242691aa24dd23434e85b0a166750d42210075bb2e2dc83a5cc73f95c 3.04kB / 3.04kB                                           0.0s
 => => sha256:1810f08f7c22d06bd0bc24f47f7e927f78ee7451baf1779e86f7d53c2fb3bc27 12.45kB / 12.45kB                                         0.0s
 => => sha256:da8dc61ccacab0c571f2793c6c5400180816557fa0140990f997519be3471012 228B / 228B                                               0.1s
 => => sha256:1f391fc42cee2e19f185ac34d4d4e8404a3209ed5c17b369dc30bdf3a0d29915 183B / 183B                                               0.2s
 => => sha256:624799215cc8ec3f277033b52eefa3e6cdee2c0371b28a4983c3722506e677a6 16.71MB / 16.71MB                                         1.5s
 => => extracting sha256:1a07b0163994a6d3328beeaa3400f6304e68548ffb84deefcb74427a6b65a489                                                1.9s
 => => sha256:1845118be0cdd364592b6079fb43ef235948f820e01b535e9b7da4187f405bd8 446B / 446B                                               1.7s
 => => sha256:10e7e30b294ed284d673effda7c4615ade5cd952cc3dee17c0116b1c0f6cd106 1.34kB / 1.34kB                                           1.7s
 => => sha256:c8e041c4002a5658f86b77e75593904c0fd11c2aa9f7ed2f36b876f5d4d54225 491B / 491B                                               1.8s
 => => sha256:73a6b1154f15b22690fa256ab1341890ac64f474ef8de184b616e0febdec4342 501B / 501B                                               1.9s
 => => sha256:c0b7948555b65a9d2d9d9f31311fc262a61ea2e63a0c482d301c2f8530e266fb 12.38MB / 12.38MB                                         3.1s
 => => sha256:12e8e47fb13ce360e3371376c201df14e62bc9e282685e02c6fa49bf4da1202e 13.09MB / 13.09MB                                         3.4s
 => => sha256:c2e806cdeee5529751cdc24bb71ce9c4871a3aceed7bd36d70bf6e74a89ae122 2.20kB / 2.20kB                                           3.3s
 => => sha256:78884ba77c453614eacc8e9f22e4f25776cc23f2ecaede13557b2c7d13994a39 905B / 905B                                               3.4s
 => => extracting sha256:da8dc61ccacab0c571f2793c6c5400180816557fa0140990f997519be3471012                                                0.0s
 => => extracting sha256:59be51dca15077e7f02edb4376d3e8e194896c4e706c9c03c2fd2d2af47f8cdc                                                2.0s
 => => extracting sha256:1f391fc42cee2e19f185ac34d4d4e8404a3209ed5c17b369dc30bdf3a0d29915                                                0.0s
 => => extracting sha256:624799215cc8ec3f277033b52eefa3e6cdee2c0371b28a4983c3722506e677a6                                                0.5s
 => => extracting sha256:10e7e30b294ed284d673effda7c4615ade5cd952cc3dee17c0116b1c0f6cd106                                                0.0s
 => => extracting sha256:1845118be0cdd364592b6079fb43ef235948f820e01b535e9b7da4187f405bd8                                                0.0s
 => => extracting sha256:c8e041c4002a5658f86b77e75593904c0fd11c2aa9f7ed2f36b876f5d4d54225                                                0.0s
 => => extracting sha256:c0b7948555b65a9d2d9d9f31311fc262a61ea2e63a0c482d301c2f8530e266fb                                                0.1s
 => => extracting sha256:73a6b1154f15b22690fa256ab1341890ac64f474ef8de184b616e0febdec4342                                                0.0s
 => => extracting sha256:12e8e47fb13ce360e3371376c201df14e62bc9e282685e02c6fa49bf4da1202e                                                0.4s
 => => extracting sha256:c2e806cdeee5529751cdc24bb71ce9c4871a3aceed7bd36d70bf6e74a89ae122                                                0.0s
 => => extracting sha256:78884ba77c453614eacc8e9f22e4f25776cc23f2ecaede13557b2c7d13994a39                                                0.0s
 => [internal] load build context                                               .0s
 => => transferring context: 869B                                               .0s
 => [2/3] RUN a2enmod rewrite                                                   .5s
 => [3/3] COPY . /var/www/html/                                                 .0s
 => exporting to image                                                          .1s
 => => exporting layers                                                         .0s
 => => writing image sha256:a305d554c3e3d9b360f52fdac10cef1b6fe65490e4e380bd816fbde2fb07e7a9                                             0.0s
 => => naming to docker.io/rsaim/06_php                                         .0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them

> sraza @ sraza0522mac ~/code/devops_educative/docker/06_php 22:55:26
$ docker run --rm -it -p 8087:80 rsaim/06_php
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.17.0.4. Set the 'ServerName' directive globally to suppress this message
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.17.0.4. Set the 'ServerName' directive globally to suppress this message
[Mon May 30 02:55:36.094134 2022] [mpm_prefork:notice] [pid 1] AH00163: Apache/2.4.25 (Debian) PHP/7.0.33 configured -- resuming normal operations
[Mon May 30 02:55:36.094184 2022] [core:notice] [pid 1] AH00094: Command line: 'apache2 -D FOREGROUND'
172.17.0.1 - - [30/May/2022:02:55:45 +0000] "GET / HTTP/1.1" 200 395 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
172.17.0.1 - - [30/May/2022:02:55:47 +0000] "GET /v1/square/4 HTTP/1.1" 200 259 "http://localhost:8087/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
```