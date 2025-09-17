import csv

csv_file_path = "./FlightRecords/CSVFile/Aug-24th-2025-04-42PM-Flight-Airdata.csv"
kml_file_path = "dji_flight_path.kml"
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    clean_headers = [h.replace('\n', ' ').strip() for h in headers]
    dict_reader = csv.DictReader(csvfile, fieldnames=clean_headers)
    
    # Initialize list for the coordinates
    coordinates = []
    
    for row in dict_reader:
        if all(not (v and v.strip()) for v in row.values()):
            continue

        lat = row['latitude']
        lon = row['longitude']
        amsl = row['altitude_above_seaLevel(feet)']
        amsl_float = float(amsl)
        amsl_meters = amsl_float * 0.3048

        
        # Append each latitude and longitude as a string "longitude,latitude,0" to the coordinates list
        coordinates.append(f"{lon},{lat},{amsl_meters}")
    
    # Create the KML content for the path (LineString)
    kml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Flight Path</name>
    <Placemark>
      <name>Flight Path</name>
      <description>
        <![CDATA[This is the path of the flight from the start to end.]]>
      </description>
      <LineString>
        <altitudeMode>relativeToGround</altitudeMode>
        <coordinates>
          {" ".join(coordinates)}  <!-- Coordinates separated by space -->
        </coordinates>
      </LineString>
    </Placemark>
  </Document>
</kml>"""
with open(kml_file_path, 'w', encoding='utf-8') as kmlfile:
    kmlfile.write(kml_content)

print(f"KML file created: {kml_file_path}")