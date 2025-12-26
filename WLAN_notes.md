
WLAN Securities
=====================
WLAN security refers to the set of technologies, protocols, and practices used to protect Wireless Local Area Networks (Wi-Fi) from unauthorized access, data theft, and attacks. It ensures that communication over Wi-Fi is confidential, authenticated, and tamper-proof.

<h3>Security protocols defines Security aspects such as</h3>
	<ul><li><b>Authentication</b>: Verifying that only authorized users/devices can connect (e.g., passwords, certificates).</li>
	<li><b>Encryption</b>: Protecting data so it cannot be read by attackers (e.g., AES-CCMP, GCMP)</li>
	<li><b>Integrity</b>: Ensuring data isn’t altered during transmission</li>
	<li><b>Management Frame Protection</b>: Preventing attacks like fake disconnects (PMF).</li>
	</ul>

<h3><b>Evolution of WLAN Security Protocols</b></h3>

        OPEN
        - No auth, no encryption
        - connect w/o pw
        - data in plain text
        - prone to attacks : eavesdropping/session hijacking/man-in-middle
        |
        | introduced encryption with static key
        |
        WEP
        - weak encryption : RC4 cipher
        - static key(40 bit or 104 bit) : same key for all packets
        	static key shared by all devices.
        	No 802.1X/EAP support → everyone used the same key.
        - shared key/ open system auth
        - no integrity protection
        - prone to key-recovery attacks
        |
        | introduced :
        |	dynamic key encryption,
        |	MIC for integrity protection
        | 
        |
        WPA
        - change key per packet
        - used TKIP encryption
        - Introduced the split into Personal and Enterprise modes.
        	WPA-Personal: Uses Pre-Shared Key (PSK) for home/SMB networks.
        	WPA-Enterprise: Uses 802.1X/EAP with a RADIUS server for corporate environments.
        - TKIP strong than wep but not strong enough to defend modern attacks
        	==> requirement for stronger encryption and standard security framework
        |
        | introduced :
        | 	stronger encryption with AES
        |	standard security framework with RSN IE
        |	.1x/EAP methods
        | 
        WPA2
        - AES-CCMP encryption
        - RSN framework
        - Continued the same model: Personal (PSK) and Enterprise (802.1X).
        - faced issues in:
        	wifi handshake capture & dictionary attack
        	management frame attack 
        	security compromise on open wifi with no encryption : easy to crack data
        	lack of forward secrecy
        - prone to bruteforce attack on wpa2-psk
        |
        | introduced solutions for attacks faced in wpa2
        |
        WPA3
        - SAE for smarter handshake
        - PMF for management frame protection
        - OWE for open wifi encryption : 
        	connect without password but data will be encrypted 
        - Forward secrecy :
        	if today's key stolen, can't read yesterday's message
        - Maintains Personal vs Enterprise distinction:
        	Personal: SAE handshake.
        	Enterprise: EAP-TLS, Suite B 192-bit security.
        	
<h3>Authentication modes</h3>

	      +----------------+----------------------+---------------------------------------------+
	      | Auth Mode      | Framework           | Methods                                    |
	      +----------------+----------------------+---------------------------------------------+
	      | Personal       | RSN (WPA/WPA2/WPA3) | WEP: Static Key (deprecated)              |
	      |                |                      | WPA/WPA2: PSK (Pre-Shared Key)            |
	      |                |                      | WPA3: SAE (Simultaneous Auth of Equals)   |
	      +----------------+----------------------+---------------------------------------------+
	      | Enterprise     | 802.1X + RSN        | EAP-TLS (cert-based), PEAP, EAP-TTLS,     |
	      |                |                      | EAP-FAST (inside 802.1X framework)        |
	      +----------------+----------------------+---------------------------------------------+
	      | Open           | None (legacy)       | No auth; WPA3 uses OWE (Enhanced Open)    |
	      +----------------+----------------------+---------------------------------------------+

<h3>Personal mode Handshakes</h3>
<ul><li> <b>WPA2 personal : PSK 4-Way Handshake</b></li>
	4-Way Handshake (EAPOL-Key Frames) - to generate encryption keys for the session<br>
    - uses PMK generated from PSK to generate session encryption keys<br>
    - (PMK = from PSK, static)                            

        	1️. AP → STA : Message 1 (ANonce)                                       
        
        	2️. STA → AP : Message 2 (SNonce + MIC)                                
        
        	3️. AP → STA : Message 3 (GTK + Install PTK)                           
        
        	4️. STA → AP : Message 4 (ACK)                                         
      
      	                                           
<li><b>WPA3 personal : SAE auth process + 4-way handshake</b></li>
   → Mutual authentication done<br>
   → PMK derived per-session (unique)

        	 SAE (Dragonfly) Authentication handshake
        
        	1. STA  →  AP : SAE Commit (Scalar, Element)
        
        	2.  AP   →  STA: SAE Commit (Scalar, Element)
        
        	3.  STA  →  AP : SAE Confirm
        
        	4.  AP   →  STA: SAE Confirm
</ul>
	

<h3><b>overview of personal handshakes in wpa2 and wpa3</b></h3>
	    	
			WPA2-PSK                             WPA3-SAE
	    	---------------------------------------------------------------
	    	[Open Auth]                          [Open Auth]
	    	[Association]                        [Association]
	    	(No key exchange)                    [SAE Commit/Confirm → PMK]
	    	[4-Way Handshake → PTK/GTK]          [4-Way Handshake → PTK/GTK]
	    	[Encrypted Data]                     [Encrypted Data]
		

<h3><b>FRAME FLOW for connection in WPA2 & WPA3 for personal profile</b></h3>

                                   WPA2-Personal (PSK)                          |                  WPA3-Personal (SAE)
        
        ----------------------------------------------------------------------------------------------------------------------------
        
       Phase 1: 802.11 MAC Authentication (Open System)                       |  Phase 1: 802.11 MAC Authentication (Open System)
        
        STA  →  AP : Authentication Request (Algorithm = 0)                    |  STA  →  AP : Authentication Request (Algorithm = 0)
        
        AP   →  STA: Authentication Response (Success)                         |  AP   →  STA: Authentication Response (Success)
        
        ----------------------------------------------------------------------------------------------------------------------------
        
        Phase 2: Association                                                   |  Phase 2: Association
        
        STA  →  AP : Association Request (RSN IE → WPA2, AKM = PSK)            |  STA  →  AP : Association Request (RSN IE → WPA3, AKM = SAE)
        
        AP   →  STA: Association Response (Success)                            |  AP   →  STA: Association Response (Success)
        
        ----------------------------------------------------------------------------------------------------------------------------
        
        	Phase 3: Authentication / Key Derivation                               |  Phase 3: SAE (Dragonfly) Authentication
        
        	(No key exchange occurs here — PMK = f(PSK, SSID))                     |  STA  →  AP : SAE Commit (Scalar, Element)
        
                                                                                |  AP   →  STA: SAE Commit (Scalar, Element)
                                          
                                                                                |  STA  →  AP : SAE Confirm
                                          
                                                                                |  AP   →  STA: SAE Confirm
                                          
                                                                                |  → Mutual authentication done
                                          
                                                                                |  → PMK derived per-session (unique)
        
        ----------------------------------------------------------------------------------------------------------------------------
        
        Phase 4: 4-Way Handshake (EAPOL-Key Frames)                            |  Phase 4: 4-Way Handshake (EAPOL-Key Frames)
        
        1️ AP → STA : Message 1 (ANonce)                                       |  1️  AP → STA : Message 1 (ANonce)
        
        2️ STA → AP : Message 2 (SNonce + MIC)                                |  2️ STA → AP : Message 2 (SNonce + MIC)
        
        3️ AP → STA : Message 3 (GTK + Install PTK)                           |  3️ AP → STA : Message 3 (GTK + Install PTK)
        
        4️ STA → AP : Message 4 (ACK)                                         |  4️ STA → AP : Message 4 (ACK)
        
        (PMK = from PSK, static)                                               |  (PMK = from SAE, fresh per session)
        
        ----------------------------------------------------------------------------------------------------------------------------
        
        Phase 5: Encrypted Data Communication                                  |  Phase 5: Encrypted Data Communication
        
        Encryption: AES-CCMP (No Forward Secrecy)                              |  Encryption: AES-GCMP (Forward Secrecy + PMF mandatory)
        
        Integrity: CBC-MAC                                                     |  Integrity: GMAC
        
        Protected bit = 1 in frame header                                      |  Protected bit = 1 in frame header

		----------------------------------------------------------------------------------------------------------------------------


	


******************************************************************************************************************************************************************
												Authored by Sreya Udayachandran
									© Copyrights reserved | Dec 2025 | sreyau7@gmail.com
