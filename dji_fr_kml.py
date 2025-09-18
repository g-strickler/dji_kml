import csv

#csv_file_path = "./FlightRecords/CSVFile/Sep-8th-2025-08-00PM-Flight-Airdata.csv"
csv_file_path = input("Enter the relative file path for the csv file: ")
kml_file_path = "dji_flight_path.kml"

# Read and process the CSV
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    clean_headers = [h.replace('\n', ' ').strip() for h in headers]
    dict_reader = csv.DictReader(csvfile, fieldnames=clean_headers)

    coordinates = []
    
    for row in dict_reader:
        if all(not (v and v.strip()) for v in row.values()):
            continue

        lat = row['latitude']
        lon = row['longitude']
        amsl = row['altitude_above_seaLevel(feet)']
        amsl_float = float(amsl)
        amsl_meters = amsl_float * 0.3048

        coordinates.append(f"{lon},{lat},{amsl_meters}")

# Split into 4 parts
total = len(coordinates)
quarter = total // 4

sections = [
    coordinates[0:quarter],
    coordinates[quarter:quarter*2],
    coordinates[quarter*2:quarter*3],
    coordinates[quarter*3:]
]

# 4 different styles/colors
styles = {
    "section1": "ffff0000",  # blue
    "section2": "ffffff00",  # cyan
    "section3": "ff00ff00",  # green
    "section4": "ff00ffff",  # aqua green
}

# Start KML content
kml_content = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Flight Path - Four Colored Sections</name>
"""

# Add styles
for name, color in styles.items():
    kml_content += f"""
    <Style id="{name}">
      <LineStyle>
        <color>{color}</color>
        <width>4</width>
      </LineStyle>
    </Style>
    """

# Add each path segment with its color
for i, segment in enumerate(sections):
    style_id = f"section{i+1}"
    kml_content += f"""
    <Placemark>
      <name>Section {i+1}</name>
      <styleUrl>#{style_id}</styleUrl>
      <LineString>
        <altitudeMode>absolute</altitudeMode>
        <coordinates>
          {" ".join(segment)}
        </coordinates>
      </LineString>
    </Placemark>
    """

# Close KML
kml_content += """
  </Document>
</kml>"""

# Write to file
with open(kml_file_path, 'w', encoding='utf-8') as kmlfile:
    kmlfile.write(kml_content)

print(f"KML file created: {kml_file_path}")
