The dji_kml repository is designed such that it will take any dji flight log in a csv file, and convert that flight log into a kml file that can be uploaded to 
google earth. The purpose of this right now is to show that the flight path can be visually displayed in a way that is easy to understand. 

To convert the csv to kml and visualize the data->
    1. download the repository
    2. run the program
    3. when aske to insert a relative path make sure you insert a relative path to a csv dji flight log
    4. open up https://earth.google.com/web/
    5. click "new", followed by "import KML file to map project"
    6. select the file that was created by the .py program. The name should be "dji_flight_path.kml"
    7. once imported you will see a top down view of the flight path, you can click switch between 3D and 2D in the bottom right
        corner. This will allow you to see elevation changes during the flight path

Notes: There are 4 different colors that display on the flight path. They split the flight into four equal sections based on time of flight. From takeoff
    to landing the colors are as follows
        ->Blue
        ->Cyan
        ->Green
        ->Yellow