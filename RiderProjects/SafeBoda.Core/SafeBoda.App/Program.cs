using System;
using SafeBoda.Core;

namespace SafeBoda.App
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create a rider
            var rider = new Rider(Guid.NewGuid(), "Aline", "+250788888888");

            // Create a driver
            var driver = new Driver(Guid.NewGuid(), "John", "+250781111111", "RAE123C");

            // Define locations
            var start = new Location(-1.9441, 30.0619); // Kigali
            var end = new Location(-1.9501, 30.0589);

            // Create a trip
            var trip = new Trip(
                Guid.NewGuid(),
                rider.Id,
                driver.Id,
                start,
                end,
                2500m,
                DateTime.Now
            );

            // Print to console
            Console.WriteLine($"Trip started from {trip.Start} to {trip.End}");
            Console.WriteLine($"Rider: {rider.Name}, Driver: {driver.Name}");
            Console.WriteLine($"Fare: {trip.Fare} RWF");
        }
    }
}