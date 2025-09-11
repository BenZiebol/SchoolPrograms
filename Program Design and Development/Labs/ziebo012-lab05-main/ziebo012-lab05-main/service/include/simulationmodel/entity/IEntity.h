#ifndef ENTITY_H_
#define ENTITY_H_

#include <vector>

#include "graph.h"
#include "math/vector3.h"
#include "util/json.h"

class SimulationModel;

class IEntity {
  public:
  IEntity();

  IEntity(const JsonObject& details);

  virtual ~IEntity();

  virtual void linkModel(SimulationModel* model);

  virtual int getId() const;

  virtual Vector3 getPosition() const;

  virtual Vector3 getDirection() const;

  virtual const JsonObject& getDetails() const;

  virtual std::string getColor() const;

  virtual std::string getName() const;

  virtual double getSpeed() const;

  virtual void setPosition(Vector3 pos_);

  virtual void setDirection(Vector3 dir_);

  virtual void setColor(std::string col_);

  virtual void rotate(double angle);

  virtual void update(double dt) = 0;

 protected:
  SimulationModel* model =nullptr;
  int id = -1;
  JsonObject details;
  Vector3 position;
  Vector3 direction;
  std::string color;
  std::string name;
  double speed = 0;
};

#endif
