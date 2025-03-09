Generation and Loading of Data
mysql setup
https://console.aiven.io/account/a51bc14c2e00/project/bellassignment55-04a3/services

Go to mysqldb folder
Run `python generate_data.py`
Run `python load_data.py`

Cloud run job Image Setup
Install Docker Desktop
cp -r ../artifact_registry/\* .
cp ../terraform_config/terraform.tf .
gcloud auth configure-docker northamerica-northeast1-docker.pkg.dev
docker build -t "odbc" --no-cache .
docker tag odbc:latest northamerica-northeast1-docker.pkg.dev/bellassignment-453021/docker-repo/odbc:latest
docker push northamerica-northeast1-docker.pkg.dev/bellassignment-453021/docker-repo/odbc:latest

Create Infrastructure

cp -r ../bucket/_ .
cp -r ../composer/_ .
cp -r ../iam/\* .
cp -r ../dags/_ .
cp -r ../cloudrunjob/_ .

terraform init
terraform fmt
terraform plan
terraform apply
terraform destroy

cp -r ../bucket/_ .
cp -r ../composer/_ .

cp -r ../iam/\* .

cp -r ../dags/_ .
cp -r ../cloudrunjob/_ .
