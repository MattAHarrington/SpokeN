# SpokeN: Hub-And-Spoke Networking Playground agents

This codebase is a fork of the Open Source [Bitwise's Loki repository](https://github.com/Bitwise-01/Loki). Loki is a simple **R**emote **A**ccess **T**ool.<br/>
Loki uses **RSA-2048** with **AES-256** to keep your communication with infected machines secure.<br/>

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

### Requirements

-   Python **3.6.x** | **3.7.x** | **3.8.x**

### Server tested on

-   Windows 10
-   Kali Linux
-   MacOS 10.15

### Bot tested on

-   Windows 10
-   MacOS 10.15

### Payload generator tested on

-   Windows 10
-   MacOS 10.15

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

---

### Installation

I reccommend you setup a new anaconda virtual environment for package management. As of December 2021, the best resource for installing Anaconda is downloading the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) package for your particular machine and setup.

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

---

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

After a moment or two of waiting, you should see you machine's information pop up on the CNC server front end, above the terminal window (as pictured in the screenshot above).

---

### After connection

-   You can click the id of the bot once it connects

### FYI

-   The bot will call the server using the Public IP, not the private IP
-   The bot will call the server using the port specified on the server tab

---
