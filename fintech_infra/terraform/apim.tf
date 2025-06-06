resource "azurerm_api_management" "apim" {
  name                = "fintech-apim"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  publisher_name      = "Fintech Corp"
  publisher_email     = "admin@fintech.com"
  sku_name            = "Developer_1"
}
