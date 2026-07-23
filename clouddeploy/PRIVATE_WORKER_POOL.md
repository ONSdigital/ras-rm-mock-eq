
# Create a private worker pool for Cloud Deploy

Reserve the ranges of ips

```bash

gcloud compute addresses create clouddeploy-worker-pool-addresses-pool --project=ras-rm-sandbox --network=ras-sandbox --prefix-length=16 --global
```

Create service networking peering

```bash
gcloud services vpc-peerings connect --service=servicenetworking.googleapis.com --network=ras-sandbox --ranges=clouddeploy-worker-pool-addresses --project=ras-rm-sandbox

gcloud services vpc-peerings update --service=servicenetworking.googleapis.com --network=ras-sandbox --ranges=clouddeploy-worker-pool-addresses
```

Create the worker pool

```bash
gcloud build worker-pools create clouddeploy-worker-pool --project=ras-rm-sandbox --region=europe-west2 --peered-network=project/625028338705/europe-west2/ras-sandbox
```

### NEW START

```bash

gcloud compute networks subnets create clouddeploy-worker-pool-subnet --project=ras-rm-sandbox --network=ras-sandbox --region=europe-west2 --range=10.10.0.0/24
```

```bash
gcloud compute addresses create clouddeploy-worker-pool-addresses --project=ras-rm-sandbox --subnet=clouddeploy-worker-pool-subnet --region europe-west2
```


gcloud services vpc-peerings connect --service=servicenetworking.googleapis.com --network=ras-sandbox --ranges=clouddeploy-worker-pool-addresses --project=ras-rm-sandbox

gcloud services vpc-peerings update --service=servicenetworking.googleapis.com --network=ras-sandbox --ranges=clouddeploy-worker-pool-addresses-pool --project=ras-rm-sandbox --force


# add range to master authorized network
(work) ➜  ras-rm-mock-eq git:(RAS-1926) ✗ gcloud compute addresses list --global
NAME                                    ADDRESS/RANGE  TYPE      PURPOSE      NETWORK      REGION  SUBNET  STATUS
clouddeploy-worker-pool-addresses-pool  10.204.0.0/16  INTERNAL  VPC_PEERING  ras-sandbox                  RESERVED
frontstage-ip                           8.228.233.101  EXTERNAL                                            IN_USE
rops-ip                                 34.54.254.143  EXTERNAL                                            IN_USE



### NOTE 

I don't think any of this is needed as we can just use the DNS endpoint of the K8s cluster if we enable that