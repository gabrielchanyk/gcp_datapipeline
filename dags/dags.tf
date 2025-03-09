resource "google_storage_bucket_object" "composer_dags_py"{
    name   = "dags/transform.py"
    source = "dags/transform.py"
    bucket = var.bucket
    metadata = {
      owner = var.owner
    }
}