```shell
>saim @ Saims-MacBook-Pro.local ~ 14:12:50
$ minikube start --vm-driver=virtualbox
😄 minikube v1.24.0 on Darwin 11.6
✨ Using the virtualbox driver based on existing profile
👍 Starting control plane node minikube in cluster minikube
🤷 virtualbox "minikube" VM is missing, will recreate.
🔥 Creating virtualbox VM (CPUs=2, Memory=2200MB, Disk=20000MB) ...
🐳 Preparing Kubernetes v1.22.3 on Docker 20.10.8 ...
 ▪ Generating certificates and keys ...
 ▪ Booting up control plane ...
 ▪ Configuring RBAC rules ...
 ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟 Enabled addons: storage-provisioner, default-storageclass
🔎 Verifying Kubernetes components...
🏄 Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default> saim @ Saims-MacBook-Pro.local ~/github/devops_educative/kubernetes_practical_guide 14:24:52 $ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured> saim @ Saims-MacBook-Pro.local ~/github/devops_educative/kubernetes_practical_guide 14:33:35
$ minikube dashboard
🔌 Enabling dashboard ...
 ▪ Using image kubernetesui/dashboard:v2.3.1
 ▪ Using image kubernetesui/metrics-scraper:v1.0.7
🤔 Verifying dashboard health ...
🚀 Launching proxy ...
🤔 Verifying proxy health ...
🎉 Opening http://127.0.0.1:64864/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ in your default browser...
^Z
[1]+ Stopped minikube dashboard> saim @ Saims-MacBook-Pro.local ~/github/devops_educative/kubernetes_practical_guide 15:02:22 

```



```bash
$ minikube ssh 
 _ _
 _ _ ( ) ( )
 ___ ___ (_) ___ (_)| |/') _ _ | |_ __
/' _ ` _ `\| |/' _ `\| || , < ( ) ( )| '_`\ /'__`\
| ( ) ( ) || || ( ) || || |\`\ | (_) || |_) )( ___/
(_) (_) (_)(_)(_) (_)(_)(_) (_)`\___/'(_,__/'`\____)$ ls 
$ pwd
/home/docker
$ ls -la
total 0
drwxr-xr-x 3 docker docker 60 Jun 18 18:22 .
drwxr-xr-x 3 root root 60 Oct 27 2021 ..
drwx------ 2 docker docker 80 Jan 1 1970 .ssh
```

```

```