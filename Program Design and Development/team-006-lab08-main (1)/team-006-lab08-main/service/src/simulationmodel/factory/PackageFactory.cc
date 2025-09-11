#include "PackageFactory.h"

IEntity* PackageFactory::createEntity(const JsonObject& entity) {
  std::string type = entity["type"];
  if (type.compare("package") == 0) {
    std::cout << "Package Created" << std::endl;
    return new Package(entity);
  }
  return nullptr;
}
