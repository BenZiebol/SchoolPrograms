#ifndef DRONE_H_
#define DRONE_H_

#include <vector>

#include "IEntity.h"
#include "math/vector3.h"

class Package;

class Drone : public IEntity {
 public:
  Drone(const JsonObject& obj);

  ~Drone();

  void getNextDelivery();

  void update(double dt);

  Drone(const Drone& drone) = delete;

  Drone& operator=(const Drone& drone) = delete;

 private:
  bool available = false;
  bool pickedUp = false;
  Package* package = nullptr;
};

#endif
