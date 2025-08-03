
import heapq

# Graph with distances and speed breakers
graph = {
    "Mangalore": {
        "Udupi": {"distance": 55, "speed_breakers": 3},
        "Madikeri": {"distance": 135, "speed_breakers": 6},
        "Karwar": {"distance": 270, "speed_breakers": 10}
    },
    "Udupi": {
        "Mangalore": {"distance": 55, "speed_breakers": 3},
        "Kundapura": {"distance": 36, "speed_breakers": 2},
        "Shimoga": {"distance": 150, "speed_breakers": 7}
    },
    "Kundapura": {
        "Udupi": {"distance": 36, "speed_breakers": 2},
        "Bhatkal": {"distance": 45, "speed_breakers": 2}
    },
    "Bhatkal": {
        "Kundapura": {"distance": 45, "speed_breakers": 2},
        "Honnavar": {"distance": 35, "speed_breakers": 1}
    },
    "Honnavar": {
        "Bhatkal": {"distance": 35, "speed_breakers": 1},
        "Karwar": {"distance": 90, "speed_breakers": 3}
    },
    "Karwar": {
        "Honnavar": {"distance": 90, "speed_breakers": 3},
        "Hubli": {"distance": 170, "speed_breakers": 5},
        "Mangalore": {"distance": 270, "speed_breakers": 10}
    },
    "Bangalore": {
        "Tumkur": {"distance": 70, "speed_breakers": 3},
        "Mandya": {"distance": 100, "speed_breakers": 5},
        "Kolar": {"distance": 66, "speed_breakers": 3}
    },
    "Mandya": {
        "Bangalore": {"distance": 100, "speed_breakers": 5},
        "Mysore": {"distance": 45, "speed_breakers": 2}
    },
    "Mysore": {
        "Mandya": {"distance": 45, "speed_breakers": 2},
        "Chamarajanagar": {"distance": 60, "speed_breakers": 3},
        "Madikeri": {"distance": 120, "speed_breakers": 6}
    },
    "Chamarajanagar": {
        "Mysore": {"distance": 60, "speed_breakers": 3},
        "Kollegal": {"distance": 40, "speed_breakers": 2}
    },
    "Kollegal": {
        "Chamarajanagar": {"distance": 40, "speed_breakers": 2},
        "Hassan": {"distance": 140, "speed_breakers": 7}
    },
    "Madikeri": {
        "Mangalore": {"distance": 135, "speed_breakers": 6},
        "Mysore": {"distance": 120, "speed_breakers": 6},
        "Hassan": {"distance": 110, "speed_breakers": 5}
    },
    "Hassan": {
        "Madikeri": {"distance": 110, "speed_breakers": 5},
        "Tumkur": {"distance": 130, "speed_breakers": 6},
        "Chikmagalur": {"distance": 60, "speed_breakers": 3}
    },
    "Chikmagalur": {
        "Hassan": {"distance": 60, "speed_breakers": 3},
        "Shimoga": {"distance": 100, "speed_breakers": 4}
    },
    "Shimoga": {
        "Chikmagalur": {"distance": 100, "speed_breakers": 4},
        "Udupi": {"distance": 150, "speed_breakers": 6},
        "Davangere": {"distance": 105, "speed_breakers": 4}
    },
    "Davangere": {
        "Shimoga": {"distance": 105, "speed_breakers": 4},
        "Hubli": {"distance": 140, "speed_breakers": 5}
    },
    "Hubli": {
        "Davangere": {"distance": 140, "speed_breakers": 5},
        "Belgaum": {"distance": 105, "speed_breakers": 4},
        "Karwar": {"distance": 170, "speed_breakers": 6},
        "Dharwad": {"distance": 20, "speed_breakers": 1}
    },
    "Belgaum": {
        "Hubli": {"distance": 105, "speed_breakers": 4},
        "Gokak": {"distance": 70, "speed_breakers": 3}
    },
    "Gokak": {
        "Belgaum": {"distance": 70, "speed_breakers": 3},
        "Bagalkot": {"distance": 90, "speed_breakers": 4}
    },
    "Bagalkot": {
        "Gokak": {"distance": 90, "speed_breakers": 4},
        "Bijapur": {"distance": 83, "speed_breakers": 4}
    },
    "Bijapur": {
        "Bagalkot": {"distance": 83, "speed_breakers": 4},
        "Gulbarga": {"distance": 165, "speed_breakers": 6}
    },
    "Gulbarga": {
        "Bijapur": {"distance": 165, "speed_breakers": 6},
        "Raichur": {"distance": 185, "speed_breakers": 7},
        "Yadgir": {"distance": 80, "speed_breakers": 3}
    },
    "Raichur": {
        "Gulbarga": {"distance": 185, "speed_breakers": 7},
        "Hospet": {"distance": 130, "speed_breakers": 5}
    },
    "Hospet": {
        "Raichur": {"distance": 130, "speed_breakers": 5},
        "Bellary": {"distance": 60, "speed_breakers": 3}
    },
    "Bellary": {
        "Hospet": {"distance": 60, "speed_breakers": 3},
        "Chitradurga": {"distance": 95, "speed_breakers": 4}
    },
    "Chitradurga": {
        "Bellary": {"distance": 95, "speed_breakers": 4},
        "Tumkur": {"distance": 130, "speed_breakers": 6}
    },
    "Tumkur": {
        "Chitradurga": {"distance": 130, "speed_breakers": 6},
        "Hassan": {"distance": 130, "speed_breakers": 6},
        "Bangalore": {"distance": 70, "speed_breakers": 3}
    },
    "Kolar": {
        "Bangalore": {"distance": 66, "speed_breakers": 2}
    },
    "Dharwad": {
        "Hubli": {"distance": 20, "speed_breakers": 1}
    },
    "Yadgir": {
        "Gulbarga": {"distance": 80, "speed_breakers": 3}
    }
}

# Metadata for each city
city_metadata = {
    "Bagalkot": {"risk_level": "🟢", "washroom": True, "fuel_station": True, "network": True, "hospital": False},
    "Bangalore": {"risk_level": "🟢", "washroom": True, "fuel_station": True, "network": True, "hospital": True},
    "Belgaum": {"risk_level": "🟠", "washroom": True, "fuel_station": True, "network": True, "hospital": True},
    "Bellary": {"risk_level": "🟢", "washroom": True, "fuel_station": True, "network": True, "hospital": True},
    "Bhatkal": {"risk_level": "🔴", "washroom": True, "fuel_station": True, "network": False, "hospital": False},
    "Bijapur": {"risk_level": "🟢", "washroom": True, "fuel_station": True, "network": True, "hospital": True},
    "Chamarajanagar": {"risk_level": "🟠", "washroom": True, "fuel_station": True, "network": True, "hospital": False},
    "Chikmagalur": {"risk_level": "🔴", "washroom": True, "fuel_station": True, "network": False, "hospital": False},
    "Chitradurga": {"risk_level": "🟠", "washroom": True, "fuel_station": True, "network": True, "hospital": False},
    "Davangere": {"risk_level": "🟢", "washroom": True, "fuel_station": True, "network": True, "hospital": True},
    "Dharwad": {"risk_level": "🟢", "washroom": True, "fuel_station": True, "network": True, "hospital": False},
    "Gokak": {"risk_level": "🟠", "washroom": True, "fuel_station": True, "network": True, "hospital": False},
    "Gulbarga": {"risk_level": "🟢", "washroom": True, "fuel_station": True, "network": True, "hospital": True},
    "Hassan": {"risk_level": "🟠", "washroom": True, "fuel_station": True, "network": True, "hospital": True},
    "Honnavar": {"risk_level": "🔴", "washroom": True, "fuel_station": True, "network": False, "hospital": False},
    "Hospet": {"risk_level": "🟢", "washroom": True, "fuel_station": True, "network": True, "hospital": False},
    "Hubli": {"risk_level": "🟢", "washroom": True, "fuel_station": True, "network": True, "hospital": True},
    "Karwar": {"risk_level": "🔴", "washroom": True, "fuel_station": True, "network": False, "hospital": False},
    "Kolar": {"risk_level": "🟠", "washroom": True, "fuel_station": True, "network": True, "hospital": False},
    "Kollegal": {"risk_level": "🟠", "washroom": True, "fuel_station": True, "network": True, "hospital": False},
    "Kundapura": {"risk_level": "🔴", "washroom": True, "fuel_station": True, "network": False, "hospital": False},
    "Madikeri": {"risk_level": "🔴", "washroom": True, "fuel_station": True, "network": False, "hospital": False},
    "Mandya": {"risk_level": "🟢", "washroom": True, "fuel_station": True, "network": True, "hospital": False},
    "Mangalore": {"risk_level": "🟢", "washroom": True, "fuel_station": True, "network": True, "hospital": True},
    "Mysore": {"risk_level": "🟢", "washroom": True, "fuel_station": True, "network": True, "hospital": True},
    "Raichur": {"risk_level": "🟢", "washroom": True, "fuel_station": True, "network": True, "hospital": False},
    "Shimoga": {"risk_level": "🔴", "washroom": True, "fuel_station": True, "network": False, "hospital": True},
    "Tumkur": {"risk_level": "🟢", "washroom": True, "fuel_station": True, "network": True, "hospital": True},
    "Udupi": {"risk_level": "🔴", "washroom": True, "fuel_station": True, "network": False, "hospital": True},
    "Yadgir": {"risk_level": "🟠", "washroom": True, "fuel_station": True, "network": True, "hospital": False}
}

# Modified Dijkstra's algorithm to track both distance and speed breakers
def dijkstra(graph, start, end):
    distances = {city: float('inf') for city in graph}
    speed_breakers = {city: 0 for city in graph}
    distances[start] = 0

    queue = [(0, 0, start)]  # (distance, speed_breakers, city)
    parents = {start: None}

    while queue:
        current_distance, current_sb, current_city = heapq.heappop(queue)

        if current_city == end:
            break

        for neighbor, info in graph[current_city].items():
            dist = info['distance']
            sb = info['speed_breakers']

            total_dist = current_distance + dist
            total_sb = current_sb + sb

            if total_dist < distances[neighbor]:
                distances[neighbor] = total_dist
                speed_breakers[neighbor] = total_sb
                parents[neighbor] = current_city
                heapq.heappush(queue, (total_dist, total_sb, neighbor))

    path = []
    city = end
    while city:
        path.insert(0, city)
        city = parents.get(city)

    return path, distances[end], speed_breakers[end] if distances[end] != float('inf') else None

# UI
print("🚀 Welcome to Karnataka Route Finder!\n")
print("🧭 Available cities:\n")
print(", ".join(sorted(graph.keys())))
print("\n")

source = input("Enter starting city: ").strip()
destination = input("Enter destination city: ").strip()

if source not in graph or destination not in graph:
    print("\n❌ Invalid city entered. Please check spelling and try again.")
else:
    path, distance, total_sb = dijkstra(graph, source, destination)
    if distance is None:
        print("\n❌ No route found between the selected cities.")
    else:
        print(f"\n✅ Shortest route from {source} to {destination}:")
        print(" ➡️  " + " -> ".join(path))
        print(f"📏 Total distance: {distance} km")
        print(f"🕳️ Total speed breakers: {total_sb}")

        print("\n📍 Properties at each stop:\n")
        for city in path:
            print(f"🛣️ {city}")
            metadata = city_metadata.get(city)
            if metadata:
                print(f"   Risk Level     : {metadata['risk_level']}")
                print(f"   Washroom       : {'✅' if metadata['washroom'] else '❌'}")
                print(f"   Fuel Station   : {'✅' if metadata['fuel_station'] else '❌'}")
                print(f"   Network        : {'✅' if metadata['network'] else '❌'}")
                print(f"   Hospital Nearby: {'✅' if metadata['hospital'] else '❌'}")
            else:
                print("   ⚠️  No metadata available for this city.")
            print()
