resource "azurerm_eventgrid_topic" "app_events" {
  name                = "fintech-events"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
}
