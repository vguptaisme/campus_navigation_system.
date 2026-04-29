import csv
import heapq
import os

# 1. Campus Data Definition
campus_data = """source,destination,distance
Main Gate,KRAVINGS,170
Main Gate,OAT,225
Main Gate,COS Complex,135
KRAVINGS,OAT,80
KRAVINGS,COS Complex,105
KRAVINGS,TAN Building,72
OAT,Auditorium,280
OAT,C-Block,255
COS Complex,Library,95
COS Complex,Health Centre,270
Library,Health Centre,225
Library,CSED,48
Library,G-Block,120
Library,H-Block,175
Library,Venture Lab,48
CSED,H-Block,128
CSED,TAN Building,40
G-Block,F-Block,72
G-Block,E-Block,112
G-Block,SBI Bank,160
F-Block,E-Block,48
F-Block,C-Block,80
E-Block,Auditorium,144
E-Block,Directorate,48
E-Block,ELC,48
Auditorium,Directorate,95
Directorate,C-Block,72
H-Block,Mechanical Dept,200
H-Block,TSLAS,95
Mechanical Dept,TSLAS,105
ELC,TAN Building,48
TAN Building,Health Centre,265
SBI Bank,G-Block Canteen,144
G-Block Canteen,Street,95
Street,KRAVINGS,128
Health Centre,Agira Hall,288
Agira Hall,Amritam Hall,16
Agira Hall,Neeram Hall,224
Amritam Hall,Prithvi Hall,95
Prithvi Hall,Tejas Hall,64
Tejas Hall,Vyan Hall,24
Vyan Hall,Viyat Hall,48
Viyat Hall,Vyom Hall,168
Vyom Hall,Anantam Hall,136
Anantam Hall,Ananta Hall,168
Ananta Hall,Ambaram Hall,144
Vasudha Hall E,Vasudha Hall G,48
Vasudha Hall G,Ira Hall,95
Ira Hall,Vahni Hall,64
Vahni Hall,Dhriti Hall,48
Dhriti Hall,Hostel FRF,72
Hostel FRF,Hostel FRG,48
Neeram Hall,Vasudha Hall E,304"""

# Create a dummy data directory and file for consistency with the original notebook setup
os.makedirs("data", exist_ok=True)
with open("data/tiet_campus_map.csv", "w") as f:
    f.write(campus_data)

# 2. Graph Building Functions
def build_graph(filepath):
    graph = {}
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            src  = row['source'].strip()
            dest = row['destination'].strip()
            dist = int(row['distance'])

            if src  not in graph: graph[src]  = {}
            if dest not in graph: graph[dest] = {}

            # Undirected — works both ways
            graph[src][dest]  = dist
            graph[dest][src]  = dist
    return graph

def get_all_locations(graph):
    return sorted(graph.keys())

# Build the graph and get locations
graph     = build_graph("data/tiet_campus_map.csv")
locations = get_all_locations(graph)

# 3. Dijkstra's Algorithm
def dijkstra(graph, start, end):
    distances      = {node: float('inf') for node in graph}
    distances[start] = 0
    previous       = {node: None for node in graph}
    pq             = [(0, start)]
    visited        = set()

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_node in visited:
            continue
        visited.add(curr_node)

        if curr_node == end:
            break

        for neighbor, weight in graph[curr_node].items():
            if neighbor in visited:
                continue
            new_dist = curr_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor]  = curr_node
                heapq.heappush(pq, (new_dist, neighbor))

    # Reconstruct path
    path, curr = [], end
    while curr:
        path.append(curr)
        curr = previous[curr]
    path.reverse()

    if not path or path[0] != start:
        return float('inf'), []

    return distances[end], path

# 4. Show Route and Command-Line Interface
def show_route(start, end, path, distance):
    print("\n" + "="*55)
    print("           SHORTEST ROUTE FOUND — TIET CAMPUS")
    print("="*55)
    print(f"\n   FROM   :  {start}")
    print(f"   TO     :  {end}")
    print(f"   DISTANCE: {distance} meters (~{distance//80} min walk)\n")
    print("   Step-by-step Directions:")
    print("  " + "-"*45)

    for i, loc in enumerate(path):
        if i == 0:
            print(f"    START    →  {loc}")
        elif i == len(path) - 1:
            print(f"    ARRIVE   →  {loc}")
        else:
            print(f"    Step {i:<2}  →  {loc}")

    print("  " + "-"*45)
    print(f"\n   You have arrived at {end}!")
    print("="*55)


def run_tiet_navigation():
    print("="*55)
    print("    TIET CAMPUS NAVIGATION SYSTEM FOR FRESHERS")
    print("      Thapar Institute of Engineering & Technology")
    print("="*55)

    while True:
        print("\n CAMPUS LOCATIONS:")
        print("-"*45)
        for i, loc in enumerate(locations, 1):
            print(f"  {i:2}. {loc}")
        print("-"*45)

        # Get START
        while True:
            try:
                s = int(input("\n Enter START location number: "))
                if 1 <= s <= len(locations):
                    start = locations[s-1]
                    break
                print(f"Enter 1 to {len(locations)}")
            except ValueError:
                print("Numbers only!")

        # Get DESTINATION
        while True:
            try:
                e = int(input(" Enter DESTINATION number  : "))
                if 1 <= e <= len(locations):
                    end = locations[e-1]
                    break
                print(f" Enter 1 to {len(locations)}")
            except ValueError:
                print(" Numbers only!")

        if start == end:
            print(f"\n  You are already at {start}!")
        else:
            print(f"\n Finding shortest path...")
            distance, path = dijkstra(graph, start, end)

            if distance == float('inf'):
                print(" No path found between these locations!")
            else:
                show_route(start, end, path, distance)

        again = input("\n Navigate again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            break


if __name__ == "__main__":
    
    run_tiet_navigation()
    
