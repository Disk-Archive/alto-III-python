ALTO III SDK (Python)
======================


Welcome to the Python SDK for the Alto III.

Usage
------

```python
    import alto
    import ipaddress
    
    a = alto.AltoIII(ip_address=ipaddress.ip_address("<alto_ip_address>"), port=6480)
    print(a.system_name)
```