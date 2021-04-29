import nestdeviceaccess
from datetime import datetime

nda = nestdeviceaccess.NestDeviceAccess(project_id="26f56ee1-82ee-4ab9-a225-04ba2df6a8aa", client_secret="zIMRRmP3j5g-kJ76XSxl51_K", client_id="420247776558-mh3dmldel2n6s1jb9uukscaqn4140it2.apps.googleusercontent.com", code="4/0AY0e-g5408xvxB8gyFSpFafkRf1dmC0FaKyZNGa09CCia2tqJfrad-rN0DQqLDPFXNoRQQ")
#nda.auth.access_token ="4/0AY0e-g7AdU-BKBdDDC4NEgzXQqR72lP-q3Y-tFyjjeP8XhMn-YWR8bGkxtWO0Hga1g6P7Q"
nda.login()
#nda.auth.refresh()
#devices = nda.get_devices()

for device in nda.get_devices():
    print(device.name)
    heatset = device.traits['sdm.devices.traits.ThermostatTemperatureSetpoint']['heatCelsius']
    heatcurr = device.traits['sdm.devices.traits.Temperature']['ambientTemperatureCelsius']
    print("Heat set to: " + str(heatset))
    print("Current temperature: " + str(heatcurr))