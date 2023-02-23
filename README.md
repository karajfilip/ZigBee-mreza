# Uspostavljanje ZigBee komunikacije
Ovaj rad je dio projekta na diplomskom studiju na [FER-u](https://www.fer.unizg.hr/). U projektu su korišteni DIGI XBee moduli za uspostavljanje komunikacije, te Raspberry Pi 4 Model B. 

## Uspostavljanje komunikacije

### Povezivanje Raspebbry Pi-jeva

Raspberry Pi se s računalom povezuju preko Wi-Fi mobilne pristupne točke preko ssh. Također se tako povezuje i više Raspberry Pi-jeva. Najprije se na Raspberry Pi-jevima napravi i podesi wpa_supplicant.conf konfiguracijska datoteka. Unutar datoteke postavlja se zemlja i podatci o mreži na koju će se pristupiti. Za pristup Raspberry Pi-ju koji se zove rpi8 upiše se sljedeća naredba:

```bash
ssh pi$rpi8.local
```

### Konfiguracija XBee modula

Za ZigBee ili Digi Mesh mrežu potrebno je konfigurirati XBee module preko [DIGI XCTU](https://www.digi.com/products/embedded-systems/digi-xbee/digi-xbee-tools/xctu) programa. U XCTU se postavljaju konfiguracijski parametri za mrežu, adresiranje, sigurnost i stanje mirovanja, te je moguće vizualizirati poslane i primljene poruke i topologiju mreže. U ovom projektu su postavljeni sljedeći parametri:

| | Koordinator | Usmjerivač | Krajnji uređaj |
| --- | --- | --- | --- |
| ID (PAN ID) | 555 | 555 | 555 |
|SC (Scan Channels) | 3FFF | 3FFF | 3FFF |
|NI (Node Identifier) | Coordinator | Router_n | End_Device |
|CE (Coordinator Enable) | Enable | Disable | Disable |
|SP (Cyclic Sleep Period) | 3E8 | 3E8 | 3E8|
|SM (Sleep Mode) | - | - | Cyclic sleep [4]|
|AP (API Enable) | Enable | Enable | Enable |

### Komunikacija između XBee modula

Za komunikaciju XBee modula korištena je Python biblioteka [*XBee Python Library*](https://xbplib.readthedocs.io/en/latest/). Datoteka *broadcast.py* je primjer korištenja python biblioteke.


### Komunikacija XBee modula preko serijskog porta Raspberry Pi-a
XBee moduli su tvornički podešeni na protokol 802.15.4 te su svi moduli jednakog prioriteta. Datoteke *receiver.py* i *transmitter.py* su korištene za komunikaciju Raspberry Pi-jeva preko serijskog porta u koje je spojen XBee modul.