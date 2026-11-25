# Mission 7 - How computers communicate

## 1. Task / objective
Explain key computer networking terms with examples, test internet connectivity and DNS lookup safely in Terminal, and describe step by step how a browser loads a website.

## 2. Work completed

**Task 7.1 - Explain network concepts**

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| LAN | A Local Area Network connects devices within one small building or room so they can share files and internet access. | Laptops and phones connected to a home or hostel Wi-Fi network. |
| MAN | A Metropolitan Area Network links multiple local networks across a single city or large campus. | Fiber network connecting different academic blocks across a university campus. |
| WAN | A Wide Area Network spans huge distances across cities, countries, or continents. | The global internet connecting servers and users worldwide. |
| DNS | The Domain Name System acts like a phonebook that matches readable website names to numerical IP addresses. | Translating `example.com` into its numerical IPv4 and IPv6 addresses. |
| Router | A networking device that directs data traffic between a local network and outside networks like the internet. | A home or hostel Wi-Fi router forwarding traffic from my laptop to my ISP. |
| Protocol | An agreed set of rules that controls how devices format, send, and receive data over a network. | HTTPS used for loading web pages securely in a browser. |
| Packet switching | Splitting larger files or messages into small chunks called packets that travel separately across the network and get reassembled at the destination. | Streaming a video or loading a webpage as thousands of small data packets. |
| Client-server | A setup where one device or app asks for data or a service and another computer responds with it. | My web browser (client) requesting a webpage from GitHub's web server (server). |

**Task 7.2 - Observe network information**

Ran `ping -c 3 example.com` and `nslookup example.com` in Terminal (keeping my local DNS server IP redacted for privacy). The ping test sent 3 ICMP packets to `example.com` and received 3 replies back with 0.0% packet loss, confirming an active connection. The `nslookup` command resolved `example.com` to its public IPv4 and IPv6 addresses.

- **What a connectivity test helps you check:** A connectivity test (`ping`) checks whether my computer can reach another machine over the network, how fast packets travel there and back, and whether any packets are getting dropped along the way.
- **What information a DNS lookup displays:** A DNS lookup displays the DNS server handling the request (redacted here) along with the public IPv4 (`A` record) and IPv6 (`AAAA` record) addresses assigned to the domain name.
- **Role of DNS when entering a website name in a browser:** Computers locate each other using numerical IP addresses rather than English words. When I type a website name into a browser, DNS translates that human-friendly domain name into the server's actual IP address so the browser knows where to send its request.

**Task 7.3 - What happens when you open a website?**

1. I type a website address like `https://example.com` into my web browser, which acts as the **client** making the request.
2. The browser checks its cache and asks a **DNS** server to translate `example.com` into the matching numerical IP address.
3. Once the **DNS** reply returns the IP address, the browser prepares a web request following the HTTP or HTTPS **protocol**.
4. My laptop sends those data packets through my local network and **router**, which forwards them across the internet toward the target IP address.
5. The remote web **server** receives the request, processes it, and sends the webpage files (HTML, CSS, and images) back as packets using the same **protocol**.
6. My **router** delivers the returning packets to my laptop, and the browser (**client**) puts them together to display the finished webpage on my screen.

## 3. Commands / tools used
- `ping -c 3 example.com` to send three test packets and confirm network reachability without packet loss.
- `nslookup example.com` to look up the public IP addresses linked to the domain name.
- `code mission-07-networking/README.md` to edit and format the documentation in VS Code.
- `git add`, `git commit`, and `git push` to save and upload Mission 7 to GitHub.

## 4. My understanding
Every website visit relies on layered teamwork between local hardware, routing rules, and global naming systems. DNS removes the need to memorize numerical IP addresses, protocols like HTTPS keep client-server requests structured, and packet switching lets routers move data efficiently across networks. Running `ping` and `nslookup` in Terminal also shows how easy it is to diagnose basic connection issues.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `mission-07-networking/README.md` containing the network concepts table, privacy-safe lookup observations, and 6-step website loading explanation.

## 8. Commit details
- Commit message: `Explain networking concepts and website communication`
- Status: Committed and pushed to the `main` branch on GitHub.