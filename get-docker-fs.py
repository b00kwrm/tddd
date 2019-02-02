import json
import subprocess
import os

docker_ps = ["docker", "ps", "-q"]
docker_inspect = ["docker", "inspect", "--format='{{.GraphDriver.Data.LowerDir}}'"]

mount_command = ["/bin/mount", "-t", "overlay", "overlay", "-o"]

link_layers = []


def get_docker_id():
    docker_ps_out = subprocess.run(docker_ps, capture_output=True)
    docker_id = str(docker_ps_out.stdout.strip(), "utf-8")
    return docker_id


def get_docker_fs(docker_id):
    docker_inspect.append(docker_id)
    docker_inspect_out = subprocess.run(docker_inspect, capture_output=True)
    lower_dir_out = str(docker_inspect_out.stdout.strip(), "utf-8")
    lower_layer_dirs = lower_dir_out.split(":")
    return lower_layer_dirs


def get_layer_links(lower_layer_dir):
    link_base = "/var/lib/docker/overlay2/l/"
    with open(lower_layer_dir + "/link") as f:
        link_dir = f.read()
    return link_base + link_dir


d_id = get_docker_id()
lower_layer_dirs = get_docker_fs(d_id)

for layer in lower_layer_dirs:
    layer_strip = layer.strip("'")
    layer_dir = layer_strip[:-5]
    link_layer = get_layer_links(layer_dir)
    link_layers.append(link_layer)

linked_layers = ":".join(link_layers)
lowerdir_c = (
    "ro,lowerdir=" + lower_layer_dirs[0][1:].replace("-init", "") + ":" + linked_layers
)
mnt_dir = "/mnt"

mount_command.append(lowerdir_c)
mount_command.append(mnt_dir)

print(mount_command)

subprocess.run(mount_command)
