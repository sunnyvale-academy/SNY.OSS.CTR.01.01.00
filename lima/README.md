
Start Lima VM from template

```console
$ limactl start ./podman-vm.yaml
...
```

To run `podman` on the host (assumes podman-remote is installed), run the following commands:

```console
$ lpodman system connection add lima-podman-vm "unix:///Users/denismaggiorotto/.lima/podman-vm/sock/podman.sock"
$ podman system connection default lima-podman-vm
$ podman run quay.io/podman/hello
```

To use docker command against podman, create an alias:

```console
$ alias "docker=podman"
```