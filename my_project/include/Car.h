/**
 * @file Car.h
 * @brief Defines the Car class.
 */

#ifndef CAR_H
#define CAR_H

#include <string>

/**
 * @class Car
 * @brief A simple Car class.
 *
 * Demonstrates how to generate docs with
 * Doxygen + Sphinx + Breathe.
 */
class Car {
public:
    /**
     * @brief Construct a new Car object.
     * @param brand Car brand name.
     * @param year Year of manufacture.
     */
    Car(const std::string& brand, int year);

    /**
     * @brief Start the engine.
     * @return true if started successfully, false otherwise.
     */
    bool startEngine();

    /// Stop the engine.
    void stopEngine();

    /// Get the car brand.
    std::string getBrand() const;

private:
    std::string brand_; ///< Brand of the car.
    int year_;          ///< Year of manufacture.
    bool running_;      ///< Engine status.
};

#endif // CAR_H
