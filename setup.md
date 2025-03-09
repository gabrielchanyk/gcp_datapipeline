## Generation and Loading of Data

### MySQL Setup

1. Visit the [Aiven console](https://console.aiven.io/account/a51bc14c2e00/project/bellassignment55-04a3/services) and create a cloud based mysql database.
2. Go to `mysqldb` folder.
3. Run:
   ```sh
   python generate_data.py
   ```
4. Run:
   ```sh
   python load_data.py
   ```

### Cloud Run Job Image Setup

1. Install Docker Desktop.
2. Copy files:
   ```sh
   mkdir terraform_imp
   cd terraform_imp
   cp -r ../terraform/artifact_registry/* .
   cp ../terraform/terraform_config/terraform.tf .
   ```
3. Configure Docker with Google Cloud:
   ```sh
   gcloud auth configure-docker northamerica-northeast1-docker.pkg.dev
   ```
4. Build and tag Docker image:
   ```sh
   docker build -t "odbc" --no-cache .
   docker tag odbc:latest northamerica-northeast1-docker.pkg.dev/bellassignment-453021/docker-repo/odbc:latest
   ```
5. Push Docker image:
   ```sh
   docker push northamerica-northeast1-docker.pkg.dev/bellassignment-453021/docker-repo/odbc:latest
   ```

### Create Infrastructure

1. Copy required files:
   ```sh
   cp ../terraform/looker/* .
   cp -r ../terraform/bq/* .
   cp ../terraform/bucket/* .
   cp ../terraform/cloudrunjob/*.tf .
   cp ../terraform/composer/* .
   cp -r ../terraform/dags/* .
   cp ../terraform/looker/* .
   cp ../terraform/terraform_config/* .
   ```
2. Initialize Terraform:
   ```sh
   terraform init
   ```
3. Format Terraform files:
   ```sh
   terraform fmt
   ```
4. Plan infrastructure changes:
   ```sh
   terraform plan
   ```
5. Apply infrastructure changes:
   ```sh
   terraform apply
   ```
6. Destroy infrastructure:

   ```sh
   terraform destroy
   ```

7. Copy additional files as needed:
   ```sh
   cp -r ../bucket/_ .
   cp -r ../composer/_ .
   cp -r ../iam/* .
   cp -r ../dags/_ .
   cp -r ../cloudrunjob/_ .
   ```
