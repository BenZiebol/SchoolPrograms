#define _USE_MATH_DEFINES
#include "Drone.h"

#include <cmath>
#include <limits>

#include "Package.h"
#include "SimulationModel.h"

Drone::Drone(const JsonObject& obj) : IEntity(obj) {
  available = true;
}

Drone::~Drone() {}

void Drone::getNextDelivery() {
  
  // If a simulation model exists and the model has scheduled deliveries
  if (model && model->scheduledDeliveries.size() > 0) {
    
    // Grab the package from the front of the queue
    package = model->scheduledDeliveries.front();
    model->scheduledDeliveries.pop_front();

    // If we grabbed a non-null package...
    if (package) {
      available = false;
      pickedUp = false;
    }
  }
}

void Drone::update(double dt) {
  if (available) {
    getNextDelivery();
  }
}
