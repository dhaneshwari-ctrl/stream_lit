import streamlit as st
import json

# Sample data for travel recommendations
travel_data = {
    "Paris": {
        "budget": 2000,
        "activities": [
            {"name": "Eiffel Tower visit", "cost": 50},
            {"name": "Louvre Museum", "cost": 60},
            {"name": "Seine River Cruise", "cost": 70}
        ]
    },
    "New York": {
        "budget": 1500,
        "activities": [
            {"name": "Statue of Liberty", "cost": 40},
            {"name": "Broadway Show", "cost": 120},
            {"name": "Central Park", "cost": 0}
        ]
    },
    "Tokyo": {
        "budget": 1800,
        "activities": [
            {"name": "Tokyo Tower", "cost": 30},
            {"name": "Sensoji Temple", "cost": 10},
            {"name": "Shibuya Crossing", "cost": 0}
        ]
    }
}

def get_recommendations(destination, budget):
    if destination in travel_data:
        data = travel_data[destination]
        if budget >= data["budget"]:
            return data
        else:
            return None
    return None

def generate_itinerary(destination_data):
    activities = sorted(destination_data["activities"], key=lambda x: x["cost"])
    itinerary = []
    total_cost = 0
    
    for activity in activities:
        if total_cost + activity["cost"] <= destination_data["budget"]:
            itinerary.append(activity["name"])
            total_cost += activity["cost"]
    
    return itinerary, total_cost

def main():
    st.title("Travel Recommendations App")
    
    destination = st.selectbox("Select your destination:", options=list(travel_data.keys()))
    budget = st.number_input("Enter your budget in USD:", min_value=0.0, step=0.01)
    
    if st.button("Get Recommendations"):
        destination_data = get_recommendations(destination, budget)
        
        if destination_data:
            st.subheader(f"Recommended activities for {destination} within your budget of ${budget}:")
            itinerary, total_cost = generate_itinerary(destination_data)
            
            if itinerary:
                st.write("Your itinerary:")
                for activity in itinerary:
                    st.write(f"- {activity}")
                st.write(f"Estimated total cost: ${total_cost:.2f}")
            else:
                st.write("Sorry, there are no activities within your budget.")
        else:
            st.write("Sorry, we don't have information for that destination or your budget is too low.")

if __name__ == "__main__":
    main()
