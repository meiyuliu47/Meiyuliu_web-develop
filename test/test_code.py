class EBEMS:
    def __init__(self):
        self.events = {}  # Dictionary to store all events
        self.customer_points = {}  # Dictionary to store customer loyalty points
        self.event_feedback = {}  # Dictionary to store event feedback

    """This step creates Database Structure, including:
    a. Events Database:
    Structure: A dictionary where each key is an event ID, and the value is another dictionary containing event details.
    Fields: Each event's dictionary includes event_name, speaker_name, event_date, event_time, topic, capacity, and attendees (a list of attendees' names).
    b. Customer Points Database:
    Structure: A dictionary where each key is a customer's name, and the value is their accumulated loyalty points.
    Purpose: Track loyalty points earned by customers for attending events.
    c. Event Feedback Database:
    Structure: A dictionary where each key is an event ID, and the value is a list of tuples containing attendee feedback.
    Each tuple in the feedback list includes attendee_name, feedback_score, and feedback_comment."""

    def add_event(self, event_id, event_name, speaker_name, event_date, event_time, topic, capacity):
        """Add a new event."""
        if event_id in self.events:
            print("Event ID already exists.")
            return

        self.events[event_id] = {
            "event_name": event_name,
            "speaker_name": speaker_name,
            "event_date": event_date,
            "event_time": event_time,
            "topic": topic,
            "capacity": capacity,
            "attendees": []
        }

    def update_event(self, event_id, **kwargs):
        """Update event information."""
        event = self.events.get(event_id)
        if not event:
            print("Event ID not found.")
            return

        event.update(kwargs)

    def delete_event(self, event_id):
        """Delete an event."""
        if event_id in self.events:
            del self.events[event_id]
            print(f"Event {event_id} has been deleted.")
        else:
            print("Event ID not found.")

    def register_for_event(self, event_id, customer_name):
        """Register a customer for an event."""
        event = self.events.get(event_id)
        if not event:
            print("Event ID not found.")
            return

        if len(event["attendees"]) < event["capacity"]:
            event["attendees"].append(customer_name)
            self.customer_points[customer_name] = self.customer_points.get(customer_name, 0) + 10  # Add loyalty points
            print(f"{customer_name} has been registered for {event['event_name']}.")
        else:
            print("Event has reached maximum capacity.")

    def add_attendee(self, event_id, attendee_name):
        """Add an attendee to an event."""
        event = self.events.get(event_id)
        if not event:
            print("Event ID not found.")
            return

        if attendee_name not in event["attendees"]:
            if len(event["attendees"]) < event["capacity"]:
                event["attendees"].append(attendee_name)
                print(f"{attendee_name} has been added to {event['event_name']}.")
            else:
                print("Event has reached maximum capacity.")
        else:
            print(f"{attendee_name} is already registered for the event.")

    def display_loyalty_points(self, customer_name):
        """Display the total loyalty points of a customer."""
        points = self.customer_points.get(customer_name, 0)
        print(f"{customer_name} has {points} loyalty points.")

    def get_event(self, event_id):
        """Get event information."""
        return self.events.get(event_id, "Event not found")
    
    def submit_feedback(self, event_id, attendee_name, feedback_score, feedback_comment):
        """Submit feedback for an event."""
        if event_id not in self.events:
            print("Event ID not found.")
            return

        if attendee_name not in self.events[event_id]["attendees"]:
            print(f"{attendee_name} is not registered for the event.")
            return

        self.event_feedback.setdefault(event_id, []).append((attendee_name, feedback_score, feedback_comment))
        print(f"Feedback from {attendee_name} for event {event_id} received.")

    def retrieve_feedback(self, event_id):
        """Retrieve feedback for an event."""
        if event_id not in self.event_feedback:
            print("No feedback available for this event.")
            return

        feedbacks = self.event_feedback.get(event_id, [])
        for attendee, score, comment in feedbacks:
            print(f"Attendee: {attendee}, Score: {score}, Comment: {comment}")

    def generate_event_report(self, event_id):
        """Generate a report for an event, including feedback."""
        if event_id not in self.events:
            print("Event ID not found.")
            return

        event = self.events[event_id]
        feedbacks = self.event_feedback.get(event_id, [])
        average_feedback = sum(score for _, score, _ in feedbacks) / len(feedbacks) if feedbacks else "No feedback"

        report = {
            "Event Name": event["event_name"],
            "Date": event["event_date"],
            "Total Capacity": event["capacity"],
            "Attendees Count": len(event["attendees"]),
            "Average Feedback Score": average_feedback,
            "Individual Feedback": feedbacks
        }

        for key, value in report.items():
            if key != "Individual Feedback":
                print(f"{key}: {value}")

        print("\nIndividual Feedback:")
        for attendee, score, comment in feedbacks:
            print(f"- Attendee: {attendee}, Score: {score}, Comment: {comment}")
    
    """Key decisions:
    Data Storage: Python dictionaries were chosen for their simplicity and efficiency in managing small-scale data, ideal for a prototype or a system with a limited number of events and attendees.
    Feedback Mechanism: A simple feedback system allows attendees to rate events and provide comments, enabling event organizers to gauge the success of their events and gather insights for improvement.
    Loyalty Points System: A system to incentivize and reward attendees for their participation, potentially leading to increased engagement and loyalty.
    Report Generation: Functionality to generate comprehensive reports that include attendance data, average feedback scores, and individual comments, providing a holistic view of each event's success."""


# Testing
ebems = EBEMS()
ebems.add_event(1, "Online Python Workshop", "Dr. Smith", "2024-03-15", "10:00 AM", "Python Programming", 100)
ebems.add_attendee(1, "Jane Doe")
ebems.register_for_event(1, "John Doe")
ebems.display_loyalty_points("John Doe")
ebems.submit_feedback(1, "John Doe", 8, "Great workshop with useful content!")
ebems.generate_event_report(1)
ebems.retrieve_feedback(1)
print(ebems.get_event(1))

"""The tests cover various functionalities such as event creation, attendee management, feedback submission, report generation, and feedback retrieval.

Event Creation Test
Input:
ebems.add_event(1, "Online Python Workshop", "Dr. Smith", "2024-03-15", "10:00 AM", "Python Programming", 100)
Expected Outcome:
An event with the ID 1 titled "Online Python Workshop" is created with details including the speaker, date, time, topic, and capacity.
No errors or issues are encountered during the creation process.

Attendee Addition Test
Input:
ebems.add_attendee(1, "Jane Doe")
Expected Outcome:
"Jane Doe" is added as an attendee to the event with ID 1.
The event's attendee list now includes "Jane Doe".

Event Registration and Loyalty Points Test
Input:
ebems.register_for_event(1, "John Doe")
ebems.display_loyalty_points("John Doe")
Expected Outcome:
"John Doe" is registered for the event with ID 1.
Loyalty points for "John Doe" are updated and displayed. Given this is his first event, the points should reflect the initial attendance.

Feedback Submission Test
Input:
ebems.submit_feedback(1, "John Doe", 8, "Great workshop with useful content!")
Expected Outcome:
Feedback from "John Doe" for the event with ID 1 is successfully submitted.
The feedback includes a score of 8 and a comment about the workshop.

Event Report Generation Test
Input:
ebems.generate_event_report(1)
Expected Outcome:
A comprehensive report for the event with ID 1 is generated.
The report includes details like total attendees, average feedback score, and specific feedback comments.

Feedback Retrieval Test
Input:
ebems.retrieve_feedback(1)
Expected Outcome:
All feedback for the event with ID 1 is retrieved and displayed.
This includes the feedback submitted by "John Doe".

Event Information Retrieval Test
Input:
print(ebems.get_event(1))
Expected Outcome:
Detailed information about the event with ID 1 is displayed.
This includes the current state of the event, such as the list of attendees and any other relevant details."""


