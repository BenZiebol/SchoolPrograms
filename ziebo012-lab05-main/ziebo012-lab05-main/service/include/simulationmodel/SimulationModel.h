#ifndef SIMULATION_MODEL_H_
#define SIMULATION_MODEL_H_

#include "Drone.h"
#include "IController.h"
#include "IEntity.h"
#include "Robot.h"
#include "graph.h"
#include <deque>
#include <map>
#include <set>

class SimulationModel {
 public:
  SimulationModel(IController& controller);

  ~SimulationModel();

  void setGraph(const routing::IGraph* graph);

  IEntity* createEntity(const JsonObject& entity);

  void removeEntity(int id);

  void scheduleTrip(const JsonObject& details);

  void update(double dt);

  const routing::IGraph* getGraph() const;

  std::deque<Package*> scheduledDeliveries;

 protected:
  IController& controller;
  std::map<int, IEntity*> entities;
  std::set<int> removed;
  void removeFromSim(int id);
  const routing::IGraph* graph = nullptr;
};

#endif
