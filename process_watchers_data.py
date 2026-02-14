import json
import random
import os

# Paths (Relative to script execution or absolute)
BASE_DIR = "/home/coolhand/html/datavis/data_trove/data/quirky"
YEAR_PATH = os.path.join(BASE_DIR, "ufo_by_year.json")
SHAPE_PATH = os.path.join(BASE_DIR, "ufo_shapes.json")
OUTPUT_PATH = "/home/coolhand/html/datavis/poems/watchers/data/watchers_data.json"

def process_data():
    print("Loading aggregates...")
    with open(YEAR_PATH, 'r') as f:
        years_data = json.load(f)
    with open(SHAPE_PATH, 'r') as f:
        shapes_data = json.load(f)
        
    # Create Shape Probability Distribution
    shape_pool = []
    total_shapes = 0
    for item in shapes_data:
        # item is {Shape: "Light", count: 27494}
        s = item['Shape']
        c = int(item['count'])
        total_shapes += c
        # We can't make a pool of 100k items, too heavy?
        # Just make a weighted choice list or normalized CDF?
        # Weighted choice is fine.
        shape_pool.append((s, c))
        
    print(f"Total Shapes Count: {total_shapes}")

    # Load Size Data
    SIZE_PATH = os.path.join(BASE_DIR, "ufo_size_state.json")
    with open(SIZE_PATH, 'r') as f:
        size_data = json.load(f)
    size_pool = []
    total_sizes = 0
    for item in size_data:
        s = item['size']
        c = int(item['count'])
        total_sizes += c
        size_pool.append((s, c))
    
    # Load Speed Data
    SPEED_PATH = os.path.join(BASE_DIR, "ufo_speed_state.json")
    with open(SPEED_PATH, 'r') as f:
        speed_data = json.load(f)
    speed_pool = []
    total_speeds = 0
    for item in speed_data:
        s = item['speed']
        c = int(item['count'])
        total_speeds += c
        speed_pool.append((s, c))

    # Load State Data
    STATE_PATH = os.path.join(BASE_DIR, "ufo_by_state.json")
    with open(STATE_PATH, 'r') as f:
        state_data = json.load(f)
    state_pool = []
    total_states = 0
    for item in state_data:
        s = item['state']
        c = int(item['count'])
        total_states += c
        state_pool.append((s, c))

    print(f"Total Sizes: {total_sizes}, Total Speeds: {total_speeds}, Total States: {total_states}")
    
    # Generate Particles
    particles = []
    
    # Sort years
    years_data.sort(key=lambda x: x['year'])
    
    total_sightings = 0
    
    for y_item in years_data:
        year = int(y_item['year'])
        count = int(y_item['count'])
        total_sightings += count
    
    print(f"Total Sightings in Year Data: {total_sightings}")
    
    scale_factor = 1.0
    if total_sightings > 60000:
        scale_factor = 60000 / total_sightings
        print(f"Scaling down by {scale_factor:.2f} to fit ~60k particles.")
        
    final_particles = []
    
    for y_item in years_data:
        year = int(y_item['year'])
        raw_count = int(y_item['count'])
        count = int(raw_count * scale_factor)
        
        # Ensure at least 1 if raw_count > 0
        if raw_count > 0 and count == 0: count = 1
        
        for _ in range(count):
            # Pick a shape
            r = random.uniform(0, total_shapes)
            upto = 0
            selected_shape = "Unknown"
            for s, sc in shape_pool:
                if r <= upto + sc:
                    selected_shape = s
                    break
                upto += sc

            # Pick a size
            r = random.uniform(0, total_sizes)
            upto = 0
            selected_size = "Medium"
            for s, sc in size_pool:
                if r <= upto + sc:
                    selected_size = s
                    break
                upto += sc

            # Pick a speed
            r = random.uniform(0, total_speeds)
            upto = 0
            selected_speed = "Medium"
            for s, sc in speed_pool:
                if r <= upto + sc:
                    selected_speed = s
                    break
                upto += sc

            # Pick a state
            r = random.uniform(0, total_states)
            upto = 0
            selected_state = "Unknown"
            for s, sc in state_pool:
                if r <= upto + sc:
                    selected_state = s
                    break
                upto += sc
            
            # Generate Random Date (MM-DD)
            # Simple weighted? No, just random for "texture"
            month = random.randint(1, 12)
            # Simple day cap
            if month in [4, 6, 9, 11]: max_d = 30
            elif month == 2: max_d = 28
            else: max_d = 31
            day = random.randint(1, max_d)
            date_str = f"{month:02d}-{day:02d}"

            # Generate Random Time (HH:MM)
            # Night sightings are more common? Let's weight it? 
            # Nah, uniform is fine for this abstraction level.
            h = random.randint(0, 23)
            m = random.randint(0, 59)
            time_str = f"{h:02d}:{m:02d}"

            final_particles.append({
                "y": year,
                "dt": date_str,
                "tm": time_str,
                "s": selected_shape,
                "sz": selected_size,
                "sp": selected_speed,
                "loc": selected_state
            })
            
    print(f"Generated {len(final_particles)} particles.")
    
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(final_particles, f)
    print("Done.")

if __name__ == "__main__":
    process_data()
