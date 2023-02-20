# handy-scripts

Just a collection of scripts I've written or acquired to assist my forensic investigations, log analysis, incident response, or other activities.

Scripts comprise of:
- Python
- Batch
- PowerShell

## Highlights

### Hash-It
A batch script which utilizes certutil to hash out files in a particular directory. Pair it with a different tool to automatically generate some form of intel against these hashes. 

```\handy-scripts\bat\certutil-hasher\hash-it```

### Loki Parser
Parser for the tool, Loki, released by Florian Roth for system-wide IoC sweeps. Should create a nice Excel sheet with data readily available for analysis.

```\handy-scripts\py3\parsers\loki-parser```

### sniffDNS
A simple DNS sniffer written in Scapy (py3) but easily adaptable for other protocols.

```\handy-scripts\py3\sniffers\sniffDns```