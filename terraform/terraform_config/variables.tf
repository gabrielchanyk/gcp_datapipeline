variable "projectID" {
  type = string
}

variable "region" {
  type = string
}

variable "owner" {
  type = string
}

variable "bucket" {
  type = string
}

variable "force_destroy" {
  type = bool
}

variable "bq_datasets" {
  description = "Map of BigQuery datasets and their respective tables"
  type        = map(list(string))
}