```bash
> sraza @ sraza0522mac ~/code/devops_educative/docker_compose 15:54:44
$ docker-compose up --build
[+] Building 0.9s (16/16) FINISHED
 => [docker_compose_database internal] load build definition from Dockerfile-db                  0.0s
 => => transferring dockerfile: 34B                                                              0.0s
 => [docker_compose_web internal] load build definition from Dockerfile                          0.0s
 => => transferring dockerfile: 32B                                                              0.0s
 => [docker_compose_database internal] load .dockerignore                                        0.0s
 => => transferring context: 2B                                                                  0.0s
 => [docker_compose_web internal] load .dockerignore                                             0.0s
 => => transferring context: 2B                                                                  0.0s
 => [docker_compose_database internal] load metadata for docker.io/mysql/mysql-server:5.7        0.7s
 => [docker_compose_web internal] load metadata for docker.io/library/python:3.9-rc-buster       0.6s
 => [auth] mysql/mysql-server:pull token for registry-1.docker.io                                0.0s
 => [auth] library/python:pull token for registry-1.docker.io                                    0.0s
 => [docker_compose_web 1/5] FROM docker.io/library/python:3.9-rc-buster@sha256:f408cb42e8ffc4d4faa15eaa7f79bff7f289e3d1802ee738738be06de5b7f60f       0.0s
 => [docker_compose_web internal] load build context                                             0.0s
 => => transferring context: 1.80kB                                                              0.0s
 => CACHED [docker_compose_web 2/5] WORKDIR /exercise_3                                          0.0s
 => CACHED [docker_compose_web 3/5] COPY requirements.txt requirements.txt                       0.0s
 => CACHED [docker_compose_web 4/5] RUN pip3 install -r requirements.txt                         0.0s
 => [docker_compose_web 5/5] COPY . .                                                            0.0s
 => CACHED [docker_compose_database 1/1] FROM docker.io/mysql/mysql-server:5.7@sha256:c6a77862b9daddb0bd91dfdae324cb8d6aff983788be0c8e6c6ba0a1657731e  0.0s
 => [docker_compose_web] exporting to image                                                      0.0s
 => => exporting layers                                                                          0.0s
 => => writing image sha256:b74fa5b7aefbbc9363f557487ba9066307fba2182f69637ccb237f908211a9d7     0.0s
 => => naming to docker.io/library/docker_compose_database                                       0.0s
 => => writing image sha256:05d96aeb5baa672349d8b53236b387e900119625b9dcd419036cbe17db092e88     0.0s
 => => naming to docker.io/library/docker_compose_web                                            0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
[+] Running 2/2
 ⠿ Container docker_compose-database-1  Running                                                  0.0s
 ⠿ Container docker_compose-web-1       Recreated                                                0.1s
Attaching to docker_compose-database-1, docker_compose-web-1
docker_compose-web-1       |  * Serving Flask app 'app.py' (lazy loading)
docker_compose-web-1       |  * Environment: development
docker_compose-web-1       |  * Debug mode: on
docker_compose-web-1       |  * Running on all addresses (0.0.0.0)
docker_compose-web-1       |    WARNING: This is a development server. Do not use it in a production deployment.
docker_compose-web-1       |  * Running on http://127.0.0.1:5000
docker_compose-web-1       |  * Running on http://172.20.0.3:5000 (Press CTRL+C to quit)
docker_compose-web-1       |  * Restarting with stat
docker_compose-web-1       |  * Debugger is active!
docker_compose-web-1       |  * Debugger PIN: 421-824-353
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:58:36] code 400, message Bad request version ('localhost\x00\x17\x00\x00ÿ\x01\x00\x01\x00\x00')
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:58:36] "ü`wàÇ°xüW&¦CiÉt�"S|ÅÁ ×HpQêüId!ýÜá=Ãö§Húhê2 ZZÀ+À/À,À0Ì©Ì¨ÀÀ/5ªª
                                                                                                                                                	localhostÿ" HTTPStatus.BAD_REQUEST -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:58:36] code 400, message Bad request version ('localhost\x00\x17\x00\x00ÿ\x01\x00\x01\x00\x00')
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:58:36] "üH×k©bÊÐ.ÉâA!aÿ¡íÏ¥Á ,½È¯ÐÜà¶*ûÒK®Tâ{ß5[úª«w)¢së£6 ZZÀ+À/À,À0Ì©Ì¨ÀÀ/5ZZ
                                                                                                                                                      	localhostÿ" HTTPStatus.BAD_REQUEST -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:58:36] code 400, message Bad request version ('localhost\x00\x17\x00\x00ÿ\x01\x00\x01\x00\x00')
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:58:36] "ü¢ÝâÉ2zë¬ÅYø¼ö¢(Ökÿ+;[~I "<	ÙEïQy#ÌÚ
                                                                                                                 tÁ(Ò¯'ju²ÿö/ ªªÀ+À/À,À0Ì©Ì¨ÀÀ/5
                                                                                                                                                     	localhostÿ" HTTPStatus.BAD_REQUEST -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:58:36] code 400, message Bad request version ('ÊÊ\x13\x01\x13\x02\x13\x03À+À/À,À0Ì©Ì¨À\x13À\x14\x00\x9c\x00\x9d\x00/\x005\x01\x00\x01\x93')
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:58:36] "üwÃ3Ë<1ÿfs¼¨ .×>ã¶[¥7l
? ÊÊÀ+À/À,À0Ì©Ì¨ÀÀ/5" HTTPStatus.BAD_REQUEST -                                                 Îmkù& ÊÒìn¢~j%Â¤/PmÊÐ®P
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:01] code 400, message Bad request version ('localhost\x00\x17\x00\x00ÿ\x01\x00\x01\x00\x00')
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:01] "üê·ÜýQuW¥[Oðwí»¨ÿÖìjÙ,öý
                                                                                             ó¯' jÒ#_!Ò©`QnðiO+ì°#ë	nÎ ::À+À/À,À0Ì©Ì¨ÀÀ/5êê
                                                                                                                                                          	localhostÿ" HTTPStatus.BAD_REQUEST -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:01] code 400, message Bad HTTP/0.9 request type ('\x16\x03\x01\x02\x00\x01\x00\x01ü\x03\x03õGÈ')
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:01] "üõGÈ ·hÃsÈÝ'x7ºÁ-7Ê%" HTTPStatus.BAD_REQUEST -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:01] code 400, message Bad request version ('localhost\x00\x17\x00\x00ÿ\x01\x00\x01\x00\x00')
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:01] ":¶ÝdF]%®á}>áÊß]béÞÓù'/# "¬e)²]á=m3îsáòU9õÄÞÀ«øO*üuú **À+À/À,À0Ì©Ì¨ÀÀ/5ÚÚ
                                                                                                                                                      	localhostÿ" HTTPStatus.BAD_REQUEST -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:01] code 400, message Bad request version ('localhost\x00\x17\x00\x00ÿ\x01\x00\x01\x00\x00')
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:01] "üÐ¼,ÒT	9TÞ¼O{¹Ï6â1ÉzÝ¶eçU d{êð=1F-{th~ 6çâs=yt+ãë3jX ZZÀ+À/À,À0Ì©Ì¨ÀÀ/5zz
                                                                                                                                                         	localhostÿ" HTTPStatus.BAD_REQUEST -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:13] code 400, message Bad request version ('\x8a\x8a\x13\x01\x13\x02\x13\x03À+À/À,À0Ì©Ì¨À\x13À\x14\x00\x9c\x00\x9d\x00/\x005\x01\x00\x01\x93zz\x00\x00\x00\x17\x00\x00ÿ\x01\x00\x01\x00\x00')
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:13] "üÒö>©C2ã³<]VÍQ£_]àÖ	<rßF-_Õ× \`iØÑß°x¬DþíÍÌ]ÞUÄ²ÓM. À+À/À,À0Ì©Ì¨ÀÀ/5zzÿ" HTTPStatus.BAD_REQUEST -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:13] code 400, message Bad request version ('jj\x13\x01\x13\x02\x13\x03À+À/À,À0Ì©Ì¨À\x13À\x14\x00\x9c\x00\x9d\x00/\x005\x01\x00\x01\x93jj\x00\x00\x00\x17\x00\x00ÿ\x01\x00\x01\x00\x00')
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:13] "fåÓU,"m?½ÝëîÜIyÎHvÔÉ`Â,úZ^9 ó£,¸|ôrUÃq üì)RÉÚZ[C jjÀ+À/À,À0Ì©Ì¨ÀÀ/5jjÿ" HTTPStatus.BAD_REQUEST -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:13] code 400, message Bad request version ('\x92\x1a¶«Ça')
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:13] "üþ?ò##éÕä2Ë77
                                                                                   ¶«Ça" HTTPStatus.BAD_REQUEST -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:13] code 400, message Bad request version ('\x9a\x9a\x13\x01\x13\x02\x13\x03À+À/À,À0Ì©Ì¨À\x13À\x14\x00\x9c\x00\x9d\x00/\x005\x01\x00\x01\x93\x1a\x1a\x00\x00\x00\x17\x00\x00ÿ\x01\x00\x01\x00\x00')
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:13] "üSI|ä¤i¨KÃoÝÝµÈ>`-)TEf å eExÀbW~¯Ë\Èè¹¬¡.f$|ÿÃ¨ À+À/À,À0Ì©Ì¨ÀÀ/5ÿ" HTTPStatus.BAD_REQUEST -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:21] "GET / HTTP/1.1" 200 -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:21] "GET /favicon.ico HTTP/1.1" 404 -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:33] "POST / HTTP/1.1" 200 -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:39] "GET / HTTP/1.1" 200 -
docker_compose-web-1       | 172.20.0.1 - - [30/May/2022 19:59:41] "GET / HTTP/1.1" 200 -
```

- Accessing `http://127.0.0.1:5001/` works but `localhost:5001/` shows bad request as shown above