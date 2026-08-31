# remote-barcode-scanner-mqtt

Turn your phones into a remote barcode scanner that scans barcodes to desktop devices.

Usage:

1. Open the [Web App](https://tony-xlh.github.io/remote-barcode-scanner-mqtt/web/) with your phone.
2. Start the server on your PC devices: `python python/server.py`. Install dependencies first: `pip install -r python/requirements.txt`.
3. Open the app you need to enter your data and then use your phone to scan barcodes. The barcode result will be passed to the app.

It uses MQTT for communication and [Dynamsoft Barcode Reader Bundle for JavaScript](https://www.npmjs.com/package/dynamsoft-barcode-reader-bundle) (`dynamsoft-barcode-reader-bundle@11.6.3000`, loaded from the jsDelivr CDN) to scan barcodes. The web app decodes camera frames through `CaptureVisionRouter` with the `ReadBarcodes_Default` template restricted to a middle-band ROI, then publishes the decoded text to the `barcode` MQTT topic via `broker.emqx.io` (`ws://broker.emqx.io:8083/mqtt` or `wss://broker.emqx.io:8084/mqtt`; the Python receiver uses TCP port 1883). Edit `python/config.py` and the `connect()` host in `web/index.html` to point both at your own broker instead.

## Demo video which scans to Excel

<https://user-images.githubusercontent.com/5462205/220531632-00f16525-0145-4abe-b589-6ffb994aeca7.mp4>
