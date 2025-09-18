# dji_kml

The **dji_kml** repository is designed to take any DJI flight log in a CSV file and convert that flight log into a KML file that can be uploaded to Google Earth. The purpose of this project is to visually display the flight path in a clear and easy-to-understand way.

---

## How to Convert CSV to KML and Visualize the Data

1. Download the repository.
2. Run the program.
3. When asked to insert a relative path, make sure you provide the relative path to a DJI CSV flight log.
4. Open [Google Earth Web](https://earth.google.com/web/).
5. Click **New**, then select **Import KML file to map project**.
6. Select the file created by the Python program. The filename should be `dji_flight_path.kml`.
7. Once imported, you will see a top-down view of the flight path. You can switch between **3D** and **2D** views in the bottom right corner to see elevation changes during the flight.

---

## Notes

The flight path is color-coded into **four equal sections** based on the time of flight, from takeoff to landing. The colors represent these sections as follows:

- **Blue**
- **Cyan**
- **Green**
- **Yellow**
