#ifndef ROBOT_H
#define ROBOT_H

#include <vector>

#include "IEntity.h"
#include "math/vector3.h"
#include "util/json.h"

class Package;

class Robot : public IEntity {
 public:

  Robot(const JsonObject& obj);

  void update(double dt);

  void receive(Package* p);

  bool requestedDelivery=true;

 protected:
  Package* package = nullptr;
};

#endif  // ROBOT_H
