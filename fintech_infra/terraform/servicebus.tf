resource "azurerm_servicebus_namespace" "sb" {
  name                = "fintech-sb"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  sku                 = "Basic"
}

resource "azurerm_servicebus_topic" "topic" {
  name                = "application-events"
  namespace_name      = azurerm_servicebus_namespace.sb.name
  resource_group_name = azurerm_servicebus_namespace.sb.resource_group_name
}
