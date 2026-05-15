# Install commands

## Publishing Helm charts

```bash
helm push mock-eq-2.0.2.tgz oci://europe-west2-docker.pkg.dev/ras-rm-sandbox/charts
```


## Creating pipelines
```bash
gcloud deploy apply --file=clouddeploy.yaml --region=europe-west2 --project=ras-rm-sandbox
```

## Creating release
```bash
gcloud deploy releases create mock-eq-100 --source=. \
--project=ras-rm-sandbox \
--region=europe-west2 \
--delivery-pipeline=ras-rm-mock-eq
```

## Gotchas

1. Authorized networks: enable google apis
2. Images: 
   ```
    docker tag europe-west2-docker.pkg.dev/ons-ci-rmrasbs/images/mock-eq:2.0.2 europe-west2-docker.pkg.dev/ras-rm-sandbox/images/mock-eq:2.0.2 
    docker push europe-west2-docker.pkg.dev/ras-rm-sandbox/images/mock-eq:2.0.2
   ```
2. Service account - create a service account with the following permissions:
   - Cloud Deploy Editor
   - Cloud Build Editor
   - Cloud Run Admin
   - Service Account User