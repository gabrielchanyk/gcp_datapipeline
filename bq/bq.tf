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
  for_each = { for dataset, tables in var.bq_datasets : "${dataset}_${tables}" => { dataset = dataset, table = tables } }
  dataset_id = google_bigquery_dataset.datasets[each.value.dataset].dataset_id
  table_id   = each.value.table

  schema = file("bq_json/${each.value.dataset}/${each.value.table}.json")
}