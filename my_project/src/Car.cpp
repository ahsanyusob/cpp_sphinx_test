#include "Car.h"
#include <iostream>

/**
 * @brief Construct a new Car object.
 * @param brand Car brand name.
 * @param year Year of manufacture.
 */
Car::Car(const std::string& brand, int year)
    : brand_(brand), year_(year), running_(false) {}

/**
 * @brief Start the engine.
 * @return true if started successfully, false otherwise.
 */
bool Car::startEngine() {
    if (!running_) {
        running_ = true;
        std::cout << brand_ << " engine started." << std::endl;
        return true;
    }
    return false; // already running
}

/**
 * @brief Stop the engine.
 */
void Car::stopEngine() {
    if (running_) {
        running_ = false;
        std::cout << brand_ << " engine stopped." << std::endl;
    }
}

/**
 * @brief Get the car brand.
 * @return std::string Car brand.
 */
std::string Car::getBrand() const {
    return brand_;
}
