#
# Creates a container registry on Azure
# 
resource "azurerm_container_registry" "container_registry" {
  name                = var.app_name
  resource_group_name = azurerm_resource_group.part4.name
  location            = var.location
  admin_enabled       = true
  sku                 = "Basic"
}