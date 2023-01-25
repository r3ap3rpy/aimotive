### Welcome

This demo is supposed to work on a Fedora 37 machine with minikube installed.

The description of the task is in the **pdf** file in the **task** folder.

As a prerequisite to further develop this app you need to have [docker](https://www.docker.com/) and [minikube](https://minikube.sigs.k8s.io/docs/start/) installed on your machine.

Clone the repo.

``` bash
git clone https://github.com/r3ap3rpy/aimotive
```

Then you will find the **app.py** which is the webpp, and the **Dockerfile** that you can use to build it.

In order to build and push the app the following commands should be issued.

``` bash
docker build -t <dockerlogin>/aimotiveapp .
docker login
ocker push <dockerlogin>/aimotiveapp
```

Once we have the fresh version of the app we can use the following commands to apply the deployments and services on our kubernetes.

``` bash
minikube start
minikube dashboard
# in a separate terminal issue the following command and leave it open
minikube tunnel
```

Then navigate into the cloned directory and apply the following two commands.

``` bash
kubectl apply -f yamlz/all-deployment.yaml
kubectl apply -f yamlz/all-service.yaml
```

In the browser on the dashboard services we have to see something similar to the below image.

![interpreter](/img/dashboard.png)
