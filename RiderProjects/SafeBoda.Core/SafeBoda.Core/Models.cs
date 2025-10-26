using System;

namespace SafeBoda.Core
{
    // Represents a location with latitude and longitude
    public record Location(double Latitude, double Longitude);

    // Represents a rider using the SafeBoda app
    public record Rider(Guid Id, string Name, string PhoneNumber);

    // Represents a driver in the SafeBoda system
    public record Driver(Guid Id, string Name, string PhoneNumber, string MotoPlateNumber);

    // Represents a trip between a rider and a driver
    public record Trip(
        Guid Id,
        Guid RiderId,
        Guid DriverId,
        Location Start,
        Location End,
        decimal Fare,
        DateTime RequestTime
    );
}