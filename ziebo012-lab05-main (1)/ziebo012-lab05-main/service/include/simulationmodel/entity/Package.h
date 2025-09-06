#ifndef PACKAGE_H
#define PACKAGE_H

#include <vector>

#include "IEntity.h"
#include "math/vector3.h"
#include "util/json.h"

class Robot;

class Package : public IEntity {
 public:

  Package(const JsonObject& obj);

  Vector3 getDestination() const;

  std::string getStrategyName() const;

  void setStrategyName(std::string strategyName_);

  void update(double dt);

  void initDelivery(Robot* owner);

  void handOff();

  bool requiresDelivery = true;

 private:
  Vector3 destination;
  std::string strategyName;
  Robot* owner = nullptr;
};

#endif  // PACKAGE_H
