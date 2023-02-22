# remote-barcode-scanner-mqtt

Turn your phones into a remote barcode scanner that scans barcodes to desktop devices.

Usage:

1. Open the [Web App](https://tony-xlh.github.io/remote-barcode-scanner-mqtt/web/) with your phone.
2. Start the server on your PC devices: `python python/server.py`. Install dependencies first: `pip install -r python/requirements.txt`.
3. Open the app you need to enter your data and then use your phone to scan barcodes. The barcode result will be passed to the app.

It uses MQTT for communication and [Dynamsoft Barcode Reader](https://www.dynamsoft.com/barcode-reader/overview/) to scan barcodes.

## Demo video which scans to Excel

<https://user-images.githubusercontent.com/5462205/220531632-00f16525-0145-4abe-b589-6ffb994aeca7.mp4>
