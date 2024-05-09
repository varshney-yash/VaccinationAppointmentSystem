class User:
    def __init__(self, user_id, name, gender, age, state, district):
        self.user_id = user_id
        self.name = name
        self.gender = gender
        self.age = age
        self.state = state
        self.district = district

class VaccinationCenter:
    def __init__(self, state, district, center_id):
        self.state = state
        self.district = district
        self.center_id = center_id
        self.capacity = {}

    def add_capacity(self, day, capacity):
        self.capacity[day] = capacity

class BookingSystem:
    def __init__(self):
        self.users = {}
        self.centers = {}
        self.bookings = {}

    def add_user(self, user_id, name, gender, age, state, district):
        if age < 18:
            raise ValueError("Users below 18 years are not eligible.")
        self.users[user_id] = User(user_id, name, gender, age, state, district)

    def add_vaccination_center(self, state, district, center_id):
        self.centers[center_id] = VaccinationCenter(state, district, center_id)

    def add_capacity_to_center(self, center_id, day, capacity):
        if center_id in self.centers:
            self.centers[center_id].add_capacity(day, capacity)
        else:
            raise ValueError("Center not found.")

    def book_vaccination(self, center_id, day, user_id):
        if user_id in self.users and center_id in self.centers:
            if day in self.centers[center_id].capacity and self.centers[center_id].capacity[day] > 0:
                self.centers[center_id].capacity[day] -= 1
                booking_id = f"{center_id}_{day}_{user_id}"
                self.bookings[booking_id] = (center_id, day, user_id)
                return booking_id
            else:
                raise ValueError("No available capacity.")
        else:
            raise ValueError("Invalid center ID or user ID.")

    def cancel_booking(self, center_id, booking_id, user_id):
        if booking_id in self.bookings:
            center_id, day, user_id = self.bookings[booking_id]
            self.centers[center_id].capacity[day] += 1
            del self.bookings[booking_id]
        else:
            raise ValueError("Booking not found.")

    def list_bookings(self, center_id, day):
        return [booking.__dict__ for booking in self.bookings.values() if booking[0] == center_id and booking[1] == day]

    def list_vaccination_centers(self, district):
        return [center.__dict__ for center in self.centers.values() if center.district == district]

if __name__ == '__main__':
    system = BookingSystem()
    system.add_vaccination_center("Karnataka", "Bangalore", "VC123")
    system.add_user("U1", "Harry", "Male", 35, "Karnataka", "Bangalore")
    system.add_capacity_to_center("VC123", "2024-05-10", 10)
    booking_id = system.book_vaccination("VC123", "2024-05-10", "U1")
    print(f"Booking ID: {booking_id}")