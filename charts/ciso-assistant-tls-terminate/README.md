## Installation 

### Pulling default values

```
helm show values . > ../custom-values.yaml
```

### Creating a dedicated namespace

```
kubectl create ns ciso-assistant
```

### Install

```
helm install my-release . -f ../custom-values.yaml -n ciso-assistant
```

### Uninstall

```
helm uninstall my-release -n ciso-assistant
```
### Nginx ingress controller configuration

In this setup, it is necessary to add the following variables to the configmap of Nginx ingress controller:
```
  proxy-buffering: "on"
  proxy-buffers: 4 "512k"
  proxy-buffer-size: "256k"
```

Additionally, for a production environment, a valid certificate shall be added to NGINX, instead of the implicit self-signed certificate that is generated in this setup.

## Upgrading

When upgrading, make sure to:
1. Backup your persistent volumes
2. Update any custom values
3. Run: helm upgrade my-release . --set global.appVersion=<new_version>
