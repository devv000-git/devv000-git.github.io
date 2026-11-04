# Sanitised resource map adapted from the original Terraform configuration.
# Reference only. Cloud provisioning is NOT required for the public demo.
# Pass identifiers and credentials using a secure deployment process.

variable "subscription_id" {
  type      = string
  sensitive = true
}
variable "location" {
  type    = string
  default = "australiaeast"
}
variable "resource_group_name" { type = string }
variable "storage_account_name" { type = string }
variable "function_app_name" { type = string }
variable "service_plan_name" { type = string }
variable "static_web_app_name" { type = string }

terraform {
  required_version = ">= 1.6.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}
provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
}

resource "azurerm_resource_group" "portfolio" {
  name = var.resource_group_name
  location = var.location
}
resource "azurerm_storage_account" "portfolio" {
  name = var.storage_account_name
  resource_group_name = azurerm_resource_group.portfolio.name
  location = azurerm_resource_group.portfolio.location
  account_tier = "Standard"
  account_replication_type = "LRS"
  min_tls_version = "TLS1_2"
  allow_nested_items_to_be_public = false
}
resource "azurerm_storage_table" "tasks" {
  name = "placementtasks"
  storage_account_id = azurerm_storage_account.portfolio.id
}
resource "azurerm_storage_container" "evidence" {
  name = "evidence"
  storage_account_id = azurerm_storage_account.portfolio.id
  container_access_type = "private"
}
resource "azurerm_service_plan" "functions" {
  name = var.service_plan_name
  resource_group_name = azurerm_resource_group.portfolio.name
  location = azurerm_resource_group.portfolio.location
  os_type = "Linux"
  sku_name = "Y1"
}
resource "azurerm_linux_function_app" "portfolio" {
  name = var.function_app_name
  resource_group_name = azurerm_resource_group.portfolio.name
  location = azurerm_resource_group.portfolio.location
  service_plan_id = azurerm_service_plan.functions.id
  storage_account_name = azurerm_storage_account.portfolio.name
  storage_account_access_key = azurerm_storage_account.portfolio.primary_access_key
  https_only = true
  functions_extension_version = "~4"
  app_settings = {
    FUNCTIONS_WORKER_RUNTIME = "python"
    AZURE_STORAGE_CONNECTION_STRING = azurerm_storage_account.portfolio.primary_connection_string
    TABLE_NAME = azurerm_storage_table.tasks.name
  }
  site_config {
    application_stack { python_version = "3.12" }
  }
}
resource "azurerm_static_web_app" "frontend" {
  name = var.static_web_app_name
  resource_group_name = azurerm_resource_group.portfolio.name
  location = "East Asia"
}

# Azure storage credentials can still reside in the Terraform state.
# Never commit tfstate, even when resource names are anonymised.
# This excerpt does not implement Entra ID or front-end API authentication.
