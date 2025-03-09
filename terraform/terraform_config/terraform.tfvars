region  = "northamerica-northeast1"
projectID = "bellassignment-453021"
force_destroy = true
owner = "gabriel"
bucket = "northamerica-northeast1-com-19fd123f-bucket"
bq_datasets = {
  "lnd"  = ["customers", "billing", "cellular_service_usage", "home_internet_usage"],
  "expl" = ["customers", "billing", "cellular_service_usage", "home_internet_usage"],
  "curated" = ["customer_usage_bill", "internet_customer_city_count", "cellular_customer_city_count"],
}