# VaccinationAppointmentSystem
Machine coding - Design problem

## Problem Statement

Design of Vaccination Appointment Booking System

Assumptions:
Vaccination centers are scattered across multiple states and districts.
Each district can have multiple vaccination centers, each uniquely identifiable.
Appointments are booked for a single day (24-hour duration).
Each day has a maximum capacity of appointments per vaccination center.
Citizens can book an appointment only once per vaccination dose.
Cancellation is allowed for an appointment.
Users below 18 years of age are not eligible for vaccination or using the system.

Features:
Register a user with a unique identification number.
Onboard a vaccination center with attributes such as state, district, and center ID.
Add capacity to a vaccination center for a specific day.
List all vaccination centers with day and capacity details for a given district.
Allow users to book a vaccination center in their district on a specific day, subject to availability.
List all bookings made for a particular vaccination center on a given day.
Allow users to cancel their existing bookings, freeing up the slot for others.
Enable users to search for vaccination centers available in their current district.

Commands:
ADD_USER <unique_identification> <name> <gender> <age> <current_state> <current_district>
Example: ADD_USER U123 Harry Male 35 Karnataka Bangalore
ADD_VACCINATION_CENTER <state_name> <district_name> <center_id>
Example: ADD_VACCINATION_CENTER Karnataka Bangalore VC123
ADD_CAPACITY <center_id> <day> <capacity>
Example: ADD_CAPACITY VC123 5 10
LIST_VACCINATION_CENTERS <district_name>
Example: LIST_VACCINATION_CENTERS Bangalore
BOOK_VACCINATION <center_id> <day> <user_id>
Example: BOOK_VACCINATION VC123 5 Harry
LIST_ALL_BOOKINGS <center_id> <day>
Example: LIST_ALL_BOOKINGS VC123 5
CANCEL_BOOKING <center_id> <booking_id> <user_id>
Example: CANCEL_BOOKING VC123 BK123 Harry
SEARCH_VACCINATION_CENTER <day> <district_name>
Example: SEARCH_VACCINATION_CENTER 6 Bangalore

Expectations:
The code should be demo-able and functionally complete.
Handle corner cases and invalid inputs gracefully with proper error messages.
Code should follow modular and object-oriented design principles.
Use in-memory data structures instead of databases or NoSQL stores.
Do not create a UI for the application.
Write a driver class for demo purposes, executing all commands in one place.
Prioritize code compilation, execution, and completion.
Start with the expected output and then work on the bonus features.

Example Command Sequence:
● ADD_USER U1 Harry Male 35 Karnataka Bangalore
● ADD_USER U2 Ron Male 30 Karnataka Bangalore
● ADD_USER U3 Albus Male 30 Karnataka Bangalore
● ADD_USER U4 Draco Male 15 Karnataka Bangalore
● ADD_USER U5 Dobby Male 30 Gujarat Surat
● ADD_VACCINATION_CENTER Karnataka Bangalore VC1
● ADD_VACCINATION_CENTER Karnataka Bangalore VC2
● ADD_VACCINATION_CENTER Karnataka Mysore VC3
● ADD_CAPACITY VC1 1 1
● ADD_CAPACITY VC2 1 3
● ADD_CAPACITY VC1 5 10
● ADD_CAPACITY VC3 3 4
● LIST_VACCINATION_CENTERS Bangalore
● BOOK_VACCINATION VC1 1 U1
● LIST_ALL_BOOKINGS VC1 1
● BOOK_VACCINATION VC2 1 U2
● BOOK_VACCINATION VC2 1 U3
● LIST_ALL_BOOKINGS VC2 1
● BOOK_VACCINATION VC1 1 U5
