resource "azurerm_key_vault" "kv" {
  name                        = "fintech-kv"
  location                    = azurerm_resource_group.main.location
  resource_group_name         = azurerm_resource_group.main.name
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  sku_name                    = "standard"
  purge_protection_enabled    = true
  soft_delete_retention_days  = 7
}

data "azurerm_client_config" "current" {}

resource "azurerm_key_vault_secret" "db_password" {
  name         = "db-password"
  value        = "AdminPass123!"
  key_vault_id = azurerm_key_vault.kv.id
}
