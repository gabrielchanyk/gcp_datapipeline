resource "google_storage_bucket_object" "composer_dags_py"{
    name   = "dags/transform/transform.py"
    source = "dags/transform/transform.py"
    bucket = var.bucket
    metadata = {
      owner = var.owner
    }
}

resource "google_storage_bucket_object" "yaml_files" {
  for_each = fileset("dags/transform/maps", "*.yaml")  # Discover all YAML files in the directory

  name   = "dags/transform/maps/${each.value}"  # Preserve the same path in the bucket
  source = "dags/transform/maps/${each.value}"  # Local path to the file
  bucket = var.bucket                  # GCS bucket name

  metadata = {
    owner = var.owner
  }
}