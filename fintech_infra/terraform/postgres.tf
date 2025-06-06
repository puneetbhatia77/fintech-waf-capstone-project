resource "azurerm_postgresql_flexible_server" "pg" {
  name                   = "fintechpg"
  resource_group_name    = azurerm_resource_group.main.name
  location               = azurerm_resource_group.main.location
  administrator_login    = "adminuser"
  administrator_password = "AdminPass123!"
  version                = "12"
  sku_name               = "B1ms"

  storage_mb             = 32768
  backup_retention_days  = 7
  geo_redundant_backup_enabled = false

  authentication {
    active_directory_auth_enabled = false
    password_auth_enabled         = true
  }
}
