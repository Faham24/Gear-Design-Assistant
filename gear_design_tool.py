import csv

def calculate_gear_specs(teeth, module):
    pitch_dia = module * teeth
    addendum = module
    dedendum = 1.25 * module
    whole_depth = 2.25 * module
    return pitch_dia, addendum, dedendum, whole_depth

def process_single_input():
    print("🛠️ Gear Design Assistant Tool (Single Mode)")
    teeth = int(input("Enter number of teeth (Z): "))
    module = float(input("Enter module (m): "))
    pitch_dia, addendum, dedendum, whole_depth = calculate_gear_specs(teeth, module)

    print("\n Computed Gear Specifications:")
    print(f"Pitch Circle Diameter: {pitch_dia:.2f} mm")
    print(f"Addendum: {addendum:.2f} mm")
    print(f"Dedendum: {dedendum:.2f} mm")
    print(f"Whole Depth: {whole_depth:.2f} mm")

def process_batch_input(input_file, output_file):
    print("📄 Batch Mode: Reading from", input_file)
    results = []

    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            teeth = int(row['Teeth'])
            module = float(row['Module'])
            pitch_dia, addendum, dedendum, whole_depth = calculate_gear_specs(teeth, module)
            results.append({
                'Teeth': teeth,
                'Module': module,
                'Pitch Circle Diameter (mm)': round(pitch_dia, 2),
                'Addendum (mm)': round(addendum, 2),
                'Dedendum (mm)': round(dedendum, 2),
                'Whole Depth (mm)': round(whole_depth, 2)
            })

    with open(output_file, 'w', newline='') as f:
        fieldnames = results[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"Batch processing complete. Results written to '{output_file}'")

if __name__ == "__main__":
    print("Choose Mode:\n1. Single Gear\n2. Batch from CSV")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        process_single_input()
    elif choice == "2":
        input_file = "input_gears.csv"
        output_file = "output_gears.csv"
        process_batch_input(input_file, output_file)
    else:
        print("Invalid choice.")
