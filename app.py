#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
from flask.templating import render_template
import speedtest

st = speedtest.Speedtest()
bytesInMb = 1048576

app = Flask(__name__)

@app.route("/")
def hello():
    upload = st.upload()/bytesInMb
    download = st.download()/bytesInMb
    servernames =[]
    st.get_servers(servernames)
    return render_template("index.html", downloadSpeed=download, uploadSpeed=upload, ping=st.results.ping)

# There are negative implications when running this in a docker container.  The next step will be to determine the best way to run this
# import os

# # scan available Wifi networks
# os.system('netsh wlan show networks')

# # input Wifi name
# name_of_router = input('Enter Name/SSID of the Wifi Network you wish to connect to: ')

# # connect to the given wifi network
# os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')

# print("If you're not yet connected, try connecting to a previously connected SSID again!")

# upload = st.upload()/bytesInMb
# download = st.download()/bytesInMb
# servernames =[]
# st.get_servers(servernames)
