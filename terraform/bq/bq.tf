resource "google_bigquery_dataset" "datasets" {
  for_each                  = var.bq_datasets
  dataset_id                = each.key
  friendly_name             = "${each.key} dataset"
  description               = "Dataset for ${each.key}"
  location                  = var.region

# can control users per dataset need to test
#   access {
#     role          = "READER"
#     user_by_email = "example-user@example.com"
#   }
}

# Create BigQuery tables
resource "google_bigquery_table" "tables" {
  deletion_protection= !var.force_destroy
  for_each = {
    for pair in flatten([
      for dataset, tables in var.bq_datasets : [
        for table in tables : {
          dataset = dataset
          table   = table
        }
      ]
    ]) : "${pair.dataset}_${pair.table}" => pair
  }

  dataset_id = google_bigquery_dataset.datasets[each.value.dataset].dataset_id
  table_id   = each.value.table

  schema = file("bq_json/${each.value.dataset}/${each.value.table}.json")
}